from django.db import models
from django.db import models

class Student(models.Model):
    id_student = models.CharField(primary_key=True, max_length=1024)
    identification = models.CharField(max_length=1024, blank=True, null=True)
    name = models.CharField(max_length=1024, blank=True, null=True)
    middle_name = models.CharField(max_length=1024, blank=True, null=True)
    last_name = models.CharField(max_length=1024, blank=True, null=True)
    native_of = models.CharField(max_length=1024, blank=True, null=True)
    # birth_date = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=1024, blank=True, null=True)
    son_count = models.IntegerField(blank=True, null=True)
    phone = models.CharField(max_length=1024, blank=True, null=True)
    email = models.CharField(max_length=1024, blank=True, null=True)
    # higher_education_in_date = models.DateField(blank=True, null=True)
    # university_in_date = models.DateField(blank=True, null=True)
    # register_date = models.DateTimeField(blank=True, null=True)
    scale = models.FloatField(blank=True, null=True)
    academic_index = models.FloatField(blank=True, null=True)
    

    class Meta:
        managed = False
        db_table = 'student'

    class Meta:
        managed = False
        db_table = 'student'
