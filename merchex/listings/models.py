from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Band(models.Model):
	class Genre(models.TextChoices):
		HIP_HOP = "HH"
		SYNTH_POP = "SP"
		ALTERNATIVE_ROCK = "AR"

	name = models.fields.CharField(max_length=100)
	genre = models.fields.CharField(choices=Genre.choices, max_length=5)
	biography = models.fields.CharField(max_length=1000)
	year_formed = models.fields.IntegerField(
		validators=[MinValueValidator(1900), MaxValueValidator(2021)]
		)
	active = models.fields.BooleanField(default=True)
	official_homepage = models.fields.URLField(null=True, blank=True)
	like_new = models.fields.BooleanField(default=False)
	hometown = models.fields.CharField(max_length=100, null=True)
	record_company = models.fields.CharField(max_length=100, null=True, blank=True)

	def __str__(self):
		return f"{self.name}"




class Advert(models.Model):
	title = models.fields.CharField(max_length=280)


class Listing(models.Model):
	class TypeListing(models.TextChoices):
		RECORDS = "Records"
		CLOTHING = "Clothing"
		POSTERS = "Posters"
		MISCELLANEOUS = "Miscellaneous"

	description = models.fields.CharField(max_length=280)
	sold = models.fields.BooleanField(default=False)
	year = models.fields.IntegerField(
		validators=[MinValueValidator(1900), MaxValueValidator(2021)]
		)
	type_listing = models.CharField(choices=TypeListing.choices, max_length=26)
	band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL) 