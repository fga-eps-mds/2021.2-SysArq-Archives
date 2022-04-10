from django.db import models
from django.contrib.postgres.fields import ArrayField
from archives_app.fields_models import (BoxAbbreviations, DocumentName, Shelf,
                                        Unity, Rack, PublicWorker)
from django.core.validators import MinValueValidator


class Document(models.Model):
    process_number = models.CharField(max_length=20)
    sender_unity = models.ForeignKey(Unity, on_delete=models.PROTECT)
    notes = models.CharField(max_length=300, blank=True, null=True)
    filer_user = models.CharField(max_length=150)
    is_filed = models.BooleanField(blank=True, null=True)
    is_eliminated = models.BooleanField(blank=True, null=True)
    send_date = models.DateField(blank=True, null=True)
    unity_id = models.ForeignKey(Unity, on_delete=models.PROTECT, blank=True,
                                 null=True, related_name='unfiled_unity')


class Relation(Document):
    received_date = models.DateField()


class OriginBoxSubject(models.Model):
    name = models.CharField(max_length=100)
    dates = ArrayField(models.DateField())


class OriginBox(models.Model):
    number = models.CharField(max_length=20)
    year = models.IntegerField(validators=[MinValueValidator(1900)])
    subject = models.ManyToManyField(OriginBoxSubject)


class DocumentNames(models.Model):
    document_name_id = models.ForeignKey(DocumentName, on_delete=models.PROTECT)
    year = models.IntegerField(validators=[MinValueValidator(1900)])
    month = models.CharField(max_length=3, blank=True, null=True)
    temporality_date = models.IntegerField(validators=[MinValueValidator(1900)])


class BoxArchiving(Relation):
    abbreviation_id = models.ForeignKey(BoxAbbreviations, on_delete=models.PROTECT,
                                        blank=True, null=True)
    shelf_id = models.ForeignKey(Shelf, on_delete=models.PROTECT, blank=True,
                                 null=True)
    rack_id = models.ForeignKey(Rack, on_delete=models.PROTECT, blank=True,
                                null=True)
    origin_box_id = models.ForeignKey(OriginBox, on_delete=models.PROTECT,
                                      blank=True, null=True)
    document_url = models.URLField(blank=True, null=True)
    box_process_number = models.CharField(max_length=15, blank=True, null=True)
    cover_sheet = models.CharField(max_length=100, blank=True, null=True)
    document_names = models.ManyToManyField(DocumentNames)


class FrequencyRelation(Relation):
    reference_period = ArrayField(models.CharField(max_length=8))
    temporality_date = models.IntegerField(validators=[MinValueValidator(1900)],
                                           blank=True, null=True)
    document_name_id = models.ForeignKey(DocumentName, on_delete=models.PROTECT,
                                         blank=True, null=True)
    sender_id = models.ForeignKey(PublicWorker, on_delete=models.PROTECT,
                                  blank=True, null=True, related_name='sender_publicworker')
    sender_cpf = models.CharField(max_length=11)
    receiver_id = models.ForeignKey(PublicWorker, on_delete=models.PROTECT,
                                    blank=True, null=True, related_name='receiver_publicworker')
    receiver_cpf = models.CharField(max_length=11)


class FrequencySheet(models.Model):
    person_id = models.ForeignKey(PublicWorker, on_delete=models.PROTECT,
                                  blank=True, null=True)
    cpf = models.CharField(max_length=11)
    role = models.CharField(max_length=100)
    category = models.CharField(max_length=100, blank=True, null=True)
    workplace = models.ForeignKey(on_delete=models.PROTECT, to='archives_app.unity')
    municipal_area = models.CharField(max_length=100)
    reference_period = models.DateField()
    document_name_id = models.ForeignKey(DocumentName, on_delete=models.PROTECT,
                                         blank=True, null=True)
    notes = models.CharField(max_length=300, blank=True, null=True)
    process_number = models.CharField(max_length=20, blank=True, null=True)
    temporality_date = models.IntegerField(validators=[MinValueValidator(1900)],
                                           blank=True, null=True)


class AdministrativeProcess(Document):
    notice_date = models.DateField()
    interested = models.CharField(max_length=150)
    document_name_id = models.ForeignKey(DocumentName, on_delete=models.PROTECT,
                                         blank=True, null=True)
    reference_month_year = models.DateField(blank=True, null=True)
    sender_user = models.ForeignKey(PublicWorker, on_delete=models.PROTECT,
                                    blank=True, null=True)
    archiving_date = models.DateField(blank=True, null=True)
    administrative_process_number = models.CharField(max_length=15, blank=True, null=True)
    temporality_date = models.IntegerField(validators=[MinValueValidator(1900)],
                                           blank=True, null=True)
