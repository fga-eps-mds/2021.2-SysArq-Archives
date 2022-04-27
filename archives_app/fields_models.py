from django.db import models
from django.core.validators import MinValueValidator


class DocumentName(models.Model):
    document_name = models.CharField(max_length=100, blank=True, null=True, unique=True)
    temporality = models.IntegerField(blank=True, null=True)
    isPermanent = models.BooleanField(blank=True, null=True)


class PublicWorker(models.Model):
    name = models.CharField(max_length=150)
    cpf = models.CharField(max_length=11, unique=True)


class Unity(models.Model):
    unity_name = models.CharField(max_length=100, blank=True, null=True, unique=True)
    unity_abbreviation = models.CharField(max_length=20, blank=True, null=True)
    administrative_bond = models.CharField(max_length=100, blank=True, null=True)
    bond_abbreviation = models.CharField(max_length=20, blank=True, null=True)
    municipality = models.CharField(max_length=100, blank=True, null=True)
    telephone_number = models.CharField(max_length=11, blank=True, null=True)
    notes = models.CharField(max_length=300, blank=True, null=True)


class BoxAbbreviations(models.Model):
    number = models.CharField(max_length=100, blank=True, null=True)
    abbreviation = models.CharField(max_length=20, blank=True, null=True, unique=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1900)])


class Shelf(models.Model):
    number = models.IntegerField(validators=[MinValueValidator(0)], unique=True)


class Rack(models.Model):
    number = models.IntegerField(validators=[MinValueValidator(0)], unique=True)


class FileLocation(models.Model):
    file = models.CharField(max_length=100, unique=True)


class FrontCover(models.Model):
    box_abbreviation = models.CharField(max_length=30, blank=True, null=True)
