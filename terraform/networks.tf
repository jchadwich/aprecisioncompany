resource "aws_vpc" "default" {
  cidr_block = "10.1.0.0/16"

  tags = {
    Name    = "${local.project}-${local.env}"
    Project = local.project
  }
}

resource "aws_subnet" "public" {
  vpc_id                  = aws_vpc.default.id
  cidr_block              = "10.1.0.0/24"
  map_public_ip_on_launch = true

  tags = {
    Name    = "${local.project}-${local.env}-public"
    Project = local.project
  }
}

resource "aws_subnet" "private" {
  vpc_id                  = aws_vpc.default.id
  cidr_block              = "10.1.1.0/24"
  map_public_ip_on_launch = false

  tags = {
    Name    = "${local.project}-${local.env}-private"
    Project = local.project
  }
}

resource "aws_internet_gateway" "default" {
  vpc_id = aws_vpc.default.id

  tags = {
    Name    = "${local.project}-${local.env}"
    Project = local.project
  }
}

resource "aws_eip" "public" {
  domain = "vpc"

  depends_on = [
    aws_internet_gateway.default,
  ]

  tags = {
    Name    = "${local.project}-${local.env}"
    Project = local.project
  }
}

resource "aws_nat_gateway" "private" {
  allocation_id = aws_eip.public.id
  subnet_id     = aws_subnet.public.id

  tags = {
    Name    = "${local.project}-${local.env}-private"
    Project = local.project
  }
}

resource "aws_route_table" "public" {
  vpc_id = aws_vpc.default.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.default.id
  }

  tags = {
    Name    = "${local.project}-${local.env}-public"
    Project = local.project
  }
}

resource "aws_route_table_association" "public" {
  subnet_id      = aws_subnet.public.id
  route_table_id = aws_route_table.public.id
}

resource "aws_route_table" "private" {
  vpc_id = aws_vpc.default.id

  route {
    cidr_block     = "0.0.0.0/0"
    nat_gateway_id = aws_nat_gateway.private.id
  }

  tags = {
    Name    = "${local.project}-${local.env}-private"
    Project = local.project
  }
}

resource "aws_route_table_association" "private" {
  subnet_id      = aws_subnet.private.id
  route_table_id = aws_route_table.private.id
}

resource "aws_security_group" "default" {
  name        = "${local.project}-${local.env}"
  vpc_id      = aws_vpc.default.id
  description = "Web traffic ingress/egress"

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = [aws_vpc.default.cidr_block]
  }

  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = [aws_vpc.default.cidr_block]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name    = "${local.project}-${local.env}"
    Project = local.project
  }
}
