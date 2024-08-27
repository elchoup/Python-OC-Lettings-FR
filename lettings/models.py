from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Represents a postal address with detailed information including the number,
    street name, city, state, and postal code.

    Attributes:
        number (int): The house or building number.
        street (str): The name of the street.
        city (str): The name of the city.
        state (str): The name of the state.
        zip_code (str): The postal code of the address.
    """

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(
        max_length=3, validators=[MinLengthValidator(3)]
    )

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Adresses"

    def __str__(self):
        return f"{self.number} {self.street}"


class Letting(models.Model):
    """
    Represents a letting (rental property) that is associated with a specific address.

    Attributes:
        title (str): The title or name of the letting.
        address (Address): The address associated with this letting.
    """

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
