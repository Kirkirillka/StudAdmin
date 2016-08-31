__author__ = 'kirill'

from django import forms
from django.contrib.auth.models import User
from .models import Student,Staff,Promotion,Violation,Habits,UserProfile


class StaffForm(forms.ModelForm):
    username=forms.CharField(max_length=100)
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=Staff
        fields=['username','password']


class AddStudentForm(forms.ModelForm):

    class Meta:
        model=Student
        fields='__all__'


class AddStaffForm(forms.ModelForm):
    class Meta:
        model=Staff
        fields='__all__'

class AddPromotion(forms.ModelForm):
    class Meta:
        model=Promotion
        fields='__all__'


class AddViolation(forms.ModelForm):
    class Meta:
        model=Violation
        fields='__all__'







class AddHabitsForm(forms.Form):
    habits=forms.ModelMultipleChoiceField(Habits.objects.all())
    class Meta:
        fields=['habits']


class ChooseViolation(forms.Form):
    violations=forms.ModelMultipleChoiceField(Violation.objects.all())

    class Meta:
        fields=['violations']