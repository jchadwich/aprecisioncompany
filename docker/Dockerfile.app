FROM ubuntu:22.04

WORKDIR /code
SHELL ["/bin/bash", "--login", "-c"]

# Configure the system environment
ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONDONTWRITEBYTECODE=1

# Install the system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
  build-essential \
  ca-certificates \
  curl \
  libpq-dev \
  postgresql-client \
  python3-dev \
  python3-pip

# Install the Python dependencies
COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY requirements.dev.txt .
RUN pip3 install -r requirements.dev.txt

# Copy the application code
COPY . .

# Configure the application server
CMD ["tail", "-f", "/dev/null"]
