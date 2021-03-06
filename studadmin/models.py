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
    first_name=models.CharField(max_length=100,verbose_name='Фамилия')
    last_name=models.CharField(max_length=100,verbose_name='Имя')
    email=models.EmailField()
    mobile=models.CharField(max_length=12,blank=True,verbose_name='Мобильный телефон')
    speciality=models.ForeignKey(Speciality,on_delete=models.DO_NOTHING,verbose_name='Направление')
    room = models.IntegerField(default=0,verbose_name='Комната проживания')
    entry_date=models.DateField(default=timezone.now,verbose_name='Дата начала обучения')
    graduation_time=models.DateField(default=timezone.datetime(day=29,month=8,year=2020),verbose_name='Дата окончания обучения')
    ticket=models.IntegerField(default=0,verbose_name='Студенческий билет')
    about = models.TextField(unique=False, blank=True,verbose_name='О себе')
    habits=models.ManyToManyField(Habits,default=None,blank=True,verbose_name='Увлечения')


    def __str__(self):
        return '%s %s'%(self.first_name,self.last_name)

    class Meta:
        ordering=['first_name','last_name','speciality']

class UserProfile(models.Model):
    user=models.OneToOneField(User,unique=True,on_delete=models.DO_NOTHING)
    student=models.OneToOneField(Student,unique=True,on_delete=models.DO_NOTHING)

class Staff(models.Model):
    user=models.OneToOneField(User,default=None)
    student=models.OneToOneField(Student,on_delete=models.DO_NOTHING)
    position=models.CharField(max_length=200)
    start_date=models.DateField(default=timezone.now)


    def __str__(self):
        return self.student.__str__()

class Violation(models.Model):
    name=models.CharField(max_length=200,verbose_name='Нарушение')
    punishment=models.IntegerField(verbose_name='Размер штрафа')
    student=models.ForeignKey(Student,default=None,unique=False,verbose_name='Нарушитель')
    start_date=models.DateField(default=timezone.now,verbose_name='Время нарушения')
    expected_time=models.DateField(verbose_name='Отработать до')
    is_forgiven=models.BooleanField(default=False,verbose_name='Отработано')
    the_head=models.ForeignKey(Staff,related_name='head_violation',verbose_name='Сотрудник')

    def __str__(self):
        return '[%s]:%s'%(self.punishment,self.name)

class Promotion(models.Model):
    name=models.CharField(max_length=200,verbose_name='Поощрение')
    promotion=models.IntegerField(verbose_name="Размер поощрения")
    student=models.ForeignKey(Student,default=None,unique=False,verbose_name="Студент")
    start_date=models.DateField(default=timezone.now,verbose_name="Время поощрения")
    the_head=models.ForeignKey(Staff,related_name='head_promotion',verbose_name="Сотрудник")

    def __str__(self):
        return '[%s]:%s'%(self.promotion,self.name)