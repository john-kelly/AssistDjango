# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Articulation(models.Model):
    #https://docs.djangoproject.com/en/dev/ref/models/fields/URLField
    link = models.CharField(max_length=100, blank=True)
    major = models.ForeignKey('Major',primary_key=True)
    community_college = models.ForeignKey('CommunityCollege',primary_key=True)
    #https://docs.djangoproject.com/en/dev/ref/models/fields/#ref-manytomanythrough fields
    #https://docs.djangoproject.com/en/dev/ref/models/fields/#django.db.models.ForeignKey.related_namelimit_choice_to 

    class Meta:
        managed = False
        db_table = 'articulation'


class CommunityCollege(models.Model):
    id = models.IntegerField(primary_key=True)  
    name = models.CharField(max_length=100, blank=True)
    
    class Meta:
        managed = False
        db_table = 'community_college'
    
    def __unicode__(self):
        return self.name


class Discipline(models.Model):
    id = models.IntegerField(primary_key=True) 
    name = models.CharField(max_length=100, blank=True)
    studies = models.ManyToManyField('Study',through='StudyDiscipline')
    majors = models.ManyToManyField('Major',through='DisciplineMajor')

    class Meta:
        managed = False
        db_table = 'discipline'

    def __unicode__(self):
        return self.name


class DisciplineMajor(models.Model):
    discipline = models.ForeignKey('Discipline',primary_key=True)
    major = models.ForeignKey('Major',primary_key=True)

    class Meta:
        managed = False
        db_table = 'discipline_major'


class Major(models.Model):
    id = models.IntegerField(primary_key=True)  
    name = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=100, blank=True)
    university = models.ForeignKey('University', blank=True, null=True)
    disciplines = models.ManyToManyField('Discipline',through='DisciplineMajor')

    class Meta:
        managed = False
        db_table = 'major'

    def __unicode__(self):
        return self.name[:20]


class Study(models.Model):
    id = models.IntegerField(primary_key=True)  
    name = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=100, blank=True)
    disciplines = models.ManyToManyField('Discipline',through='StudyDiscipline')

    class Meta:
        managed = False
        db_table = 'study'

    def __unicode__(self):
        return self.name



class StudyDiscipline(models.Model):
    study = models.ForeignKey('Study',primary_key=True)
    discipline = models.ForeignKey('Discipline',primary_key=True)

    class Meta:
        managed = False
        db_table = 'study_discipline'


class University(models.Model):
    id = models.IntegerField(primary_key=True)  
    name = models.CharField(max_length=100, blank=True)
    abbrev = models.CharField(max_length=100, blank=True)

    class Meta:
        managed = False
        db_table = 'university'
