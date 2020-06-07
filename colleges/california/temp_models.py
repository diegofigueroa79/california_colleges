# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CollegesCa(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    city = models.TextField()
    state = models.TextField()
    zip = models.TextField()
    url = models.TextField()
    adm_rate = models.FloatField()
    satvr25 = models.FloatField()
    satvr75 = models.FloatField()
    satmt25 = models.FloatField()
    satmt75 = models.FloatField()
    satwr25 = models.FloatField()
    satwr75 = models.FloatField()
    satvrmid = models.FloatField()
    satmtmid = models.FloatField()
    actcm25 = models.FloatField()
    actcm75 = models.FloatField()
    acten25 = models.FloatField()
    acten75 = models.FloatField()
    actmt25 = models.FloatField()
    actmt75 = models.FloatField()
    actwr25 = models.FloatField()
    actwr75 = models.FloatField()
    actcmmid = models.FloatField()
    actenmid = models.FloatField()
    actmtmid = models.FloatField()
    actwrmid = models.FloatField()
    sat_avg = models.FloatField()
    tuition_in = models.FloatField()
    tuition_out = models.FloatField()

    class Meta:
        managed = True
        db_table = 'colleges_ca'
