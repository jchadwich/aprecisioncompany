from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    full_name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.full_name

    def save(self, **kwargs):
        self.full_name = f"{self.first_name} {self.last_name}"
        return super().save(**kwargs)
