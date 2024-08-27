from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Represents a user profile that extends the base user model with additional information.

    Attributes:
        user (User): The user associated with this profile.
        favorite_city (str): The user's favorite city.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.user.username
