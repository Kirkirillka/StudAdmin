from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

# Create your models here.


class Speciality(models.Model):
    name=models.CharField(max_length=120)
    code=models.CharField(max_length=12)

    def __str__(self):
        return "{0}:{1}".format(self.code,self.name,)


class Habits(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Student(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField()
    mobile=models.CharField(max_length=12,blank=True)
    speciality=models.ForeignKey(Speciality,on_delete=models.DO_NOTHING)
    room = models.IntegerField(default=0)
    entry_date=models.DateField(default=timezone.now)
    graduation_time=models.DateField()
    ticket=models.IntegerField(default=0)
    about = models.TextField(unique=False, blank=True)
    habits=models.ManyToManyField(Habits,default=None,blank=True)


    def __str__(self):
        return '%s %s'%(self.first_name,self.last_name)

    class Meta:
        ordering=['first_name','last_name','speciality']

class Staff(models.Model):
    user=models.OneToOneField(User,default=None)
    student=models.OneToOneField(Student,on_delete=models.DO_NOTHING)
    position=models.CharField(max_length=200)
    start_date=models.DateField(default=timezone.now)


    def __str__(self):
        return self.student.__str__()

class Violation(models.Model):
    name=models.CharField(max_length=200)
    punishment=models.IntegerField()
    student=models.OneToOneField(Student,default=None,unique=False)
    start_date=models.DateField(default=timezone.now)
    expity_time=models.DateField()
    is_forgiven=models.BooleanField(default=False)
    the_head=models.ForeignKey(Staff,related_name='head_violation')

    def __str__(self):
        return '[%s]:%s'%(self.punishment,self.name)

class Promotion(models.Model):
    name=models.CharField(max_length=200)
    promotion=models.IntegerField()
    student=models.ManyToManyField(Student,default=None)
    start_date=models.DateField(default=timezone.now)
    the_head=models.ForeignKey(Staff,related_name='head_promotion')

    def __str__(self):
        return '[%s]:%s'%(self.promotion,self.name)