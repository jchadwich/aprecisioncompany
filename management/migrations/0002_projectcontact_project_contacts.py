# Generated by Django 4.2.4 on 2023-08-30 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("management", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProjectContact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("order", models.PositiveIntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "contact",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="management.contact",
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="management.project",
                    ),
                ),
            ],
            options={
                "unique_together": {("project", "contact")},
            },
        ),
        migrations.AddField(
            model_name="project",
            name="contacts",
            field=models.ManyToManyField(
                through="management.ProjectContact", to="management.contact"
            ),
        ),
    ]
