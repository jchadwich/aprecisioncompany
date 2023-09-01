from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        """Return the full name of the User"""
        return f"{ self.first_name } { self.last_name }"
