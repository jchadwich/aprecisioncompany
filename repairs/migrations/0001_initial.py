# Generated by Django 4.2.4 on 2023-08-30 18:38

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("management", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Measurement",
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
                ("object_id", models.IntegerField()),
                (
                    "stage",
                    models.CharField(
                        choices=[("INITIAL", "Initial"), ("FINAL", "Final")],
                        max_length=10,
                    ),
                ),
                ("address", models.CharField(max_length=255)),
                ("city", models.CharField(max_length=100)),
                ("state", models.CharField(max_length=2)),
                ("country", models.CharField(max_length=50)),
                ("zip_code", models.CharField(max_length=6)),
                (
                    "quick_description",
                    models.CharField(
                        blank=True,
                        choices=[("S", "Small"), ("M", "Medium"), ("L", "Large")],
                        max_length=10,
                        null=True,
                    ),
                ),
                (
                    "special_case",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("AP", "Aprons"),
                            ("AS", "Asphalt"),
                            ("BHC", "Bottom HC"),
                            ("C2B", "C2B"),
                            ("CB", "Catch Basin"),
                            ("C", "Curb"),
                            ("D", "Driveway"),
                            ("GP", "Gutter Pan"),
                            ("L", "Leadwalk"),
                            ("ME", "Meters"),
                            ("MI", "Missed"),
                            ("R", "Replace"),
                            ("SW2C", "SW2C"),
                        ],
                        max_length=10,
                        null=True,
                    ),
                ),
                ("h1", models.FloatField()),
                ("h2", models.FloatField()),
                ("location", django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ("length", models.FloatField()),
                ("width", models.FloatField()),
                ("lineal_feet", models.FloatField()),
                ("inch_feet", models.FloatField()),
                ("cost", models.FloatField()),
                ("quality", models.FloatField(blank=True, null=True)),
                ("note", models.TextField(blank=True, null=True)),
                ("measured_at", models.DateTimeField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "created_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="measurements",
                        to="management.project",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="MeasurementImage",
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
                ("url", models.URLField(max_length=255)),
                ("captured_at", models.DateTimeField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "measurement",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images",
                        to="repairs.measurement",
                    ),
                ),
            ],
        ),
    ]
