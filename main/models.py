from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Authors(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    author = models.CharField(max_length=10485760)

    class Meta:
        managed = False
        db_table = 'Authors'


class Bookpoint(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    cbs = models.ForeignKey('Region', models.DO_NOTHING, db_column='cbs')
    name = models.CharField(max_length=10485760)
    adress = models.CharField(max_length=10485760)
    eisk = models.FloatField()

    class Meta:
        managed = False
        db_table = 'BookPoint'


class Catalog(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    autfk = models.ForeignKey(Authors, models.DO_NOTHING, db_column='autFK')  # Field name made lowercase.
    title = models.CharField(max_length=10485760)
    place = models.CharField(max_length=10485760)
    publ = models.CharField(max_length=10485760)
    year = models.CharField(max_length=4)
    lan = models.CharField(max_length=3)
    rubrics = models.CharField(max_length=10485760)
    person = models.CharField(max_length=10485760)
    serial = models.CharField(max_length=10485760)
    material = models.CharField(max_length=10485760)
    biblevel = models.CharField(max_length=10485760)
    ager = models.CharField(max_length=4)

    class Meta:
        managed = False
        db_table = 'Catalog'


class Circulation(models.Model):
    cirid = models.AutoField(db_column='cirID', primary_key=True)  # Field name made lowercase.
    catalogfk = models.ForeignKey(Catalog, models.DO_NOTHING, db_column='catalogFK')  # Field name made lowercase.
    barcode = models.CharField(max_length=10485760)
    startdate = models.DateField(db_column='startDate')  # Field name made lowercase.
    finishdate = models.DateField(db_column='finishDate')  # Field name made lowercase.
    readerfk = models.ForeignKey('Readers', models.DO_NOTHING, db_column='readerFK')  # Field name made lowercase.
    bookpointfk = models.ForeignKey(Bookpoint, models.DO_NOTHING, db_column='bookPointFK')  # Field name made lowercase.
    state = models.CharField(max_length=10485760)

    class Meta:
        managed = False
        db_table = 'Circulation'


class Fond(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    catfk = models.ForeignKey(Catalog, models.DO_NOTHING, db_column='catFK')  # Field name made lowercase.
    siglafk = models.ForeignKey('Siglas', models.DO_NOTHING, db_column='siglaFK')  # Field name made lowercase.
    inventorynumber = models.IntegerField(db_column='inventoryNumber')  # Field name made lowercase.
    barcode = models.CharField(db_column='barCode', max_length=10485760)  # Field name made lowercase.
    trackindex = models.CharField(db_column='trackIndex', max_length=10485760)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Fond'


class Readers(models.Model):
    abisid = models.AutoField(db_column='abisID', primary_key=True)  # Field name made lowercase.
    dateofbirth = models.DateField(db_column='dateOfBirth')  # Field name made lowercase.
    adress = models.CharField(max_length=10485760)

    class Meta:
        managed = False
        db_table = 'Readers'


class Region(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=10485760)

    class Meta:
        managed = False
        db_table = 'Region'


class Siglas(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    cbs = models.ForeignKey(Region, models.DO_NOTHING, db_column='cbs')
    name = models.CharField(max_length=10485760)
    adress = models.CharField(max_length=10485760)
    eisk = models.FloatField()

    class Meta:
        managed = False
        db_table = 'Siglas'


class Siglasnic(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    bookpointfk = models.ForeignKey(Bookpoint, models.DO_NOTHING, db_column='bookpointFK')  # Field name made lowercase.
    siglasfk = models.ForeignKey(Siglas, models.DO_NOTHING, db_column='siglasFK')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Siglasnic'
