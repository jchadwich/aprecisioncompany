# Generated by Django 4.2.4 on 2023-09-01 15:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("repairs", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="status",
            field=models.CharField(
                choices=[
                    ("S", "Started"),
                    ("I", "In Progress"),
                    ("C", "Complete"),
                    ("X", "Canceled"),
                ],
                default="S",
                max_length=1,
            ),
        ),
    ]
