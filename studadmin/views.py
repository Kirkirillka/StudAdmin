from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import reverse
from django.views import View
from django.views.generic import DetailView, ListView,FormView
from .forms import AddStudentForm, AddPromotion, AddStaffForm, AddViolation, ChooseViolation, AddHabitsForm,StaffForm
from .models import *

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


# Create your views here.

class index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'studadmin/index.html')



class Logout(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return HttpResponseRedirect(reverse('studadmin:login'))

class Login(View):
    def get(self,request,*args,**kwargs):
        staff_form=StaffForm()
        return render(request,'studadmin/login.html',{'staff_form':staff_form})

    def post(self,request,*args,**kwargs):
        staff_form=StaffForm(request.POST)
        if staff_form.is_valid():
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(username=username,password=password)
            if user:
                if user.is_active:
                    login(request,user)
                    return HttpResponseRedirect(reverse('studadmin:students_list',kwargs={'page':1}))
                else:
                    return HttpResponse('Your account is not active')
            else:
                return render(request,'studadmin/login.html',{'staff_form':StaffForm(),
                                                              'error':'Bad credentials'})

class StudentListView(ListView):
    model = Student
    paginate_by = 10


class StudentDetailView(DetailView):
    model = Student

    def get_context_data(self, **kwargs):
        content = super(StudentDetailView, self).get_context_data(**kwargs)
        return content


class AddPromotionView(View):
    def get(self, request, *args, **kwargs):
        usr = request.user
        form = AddPromotion()
        return render(request, 'studadmin/add_promotion.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = AddPromotion(request.POST)
        if form.is_valid() and request.user.is_authenticated() and request.user.has_perm('studadmin.add_promotion'):
            form.save()
            return HttpResponse('Promotion has been added')
        return render(request, 'studadmin/add_promotion.html', {'form': form})


class AddViolationView(View):
    def get(self, request, *args, **kwargs):
        usr = request.user
        form = AddViolation()
        return render(request, 'studadmin/add_violation.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = AddViolation(request.POST)
        if form.is_valid() and request.user.is_authenticated() and request.user.has_perm('studadmin.add_violation'):
            form.save()
            return HttpResponse('Violation has been added')
        return render(request, 'studadmin/add_violation.html', {'form': form})


class AddStudentView(View):
    def get(self, request, *args, **kwargs):
        student_form = AddStudentForm()
        habits_form = AddHabitsForm()
        return render(request, 'studadmin/add_student.html', {'student_form': student_form,
                                                              'habits_form': habits_form})

    def post(self, request, *args, **kwargs):
        student_form = AddStudentForm(request.POST)
        habits_form = AddHabitsForm(request.POST)
        if request.user.is_authenticated() and request.user.has_perm('studadmin.add_student'):
            if student_form.is_valid() and habits_form.is_valid():
                student = student_form.save()
                student.habits_set = habits_form.cleaned_data
                return render(request, 'studadmin/add_student.html', {'student_form': AddStudentForm(),
                                                                      'habits_form': AddHabitsForm(),
                                                                      'notification': 'User has been succesfully added '})
        return render(request, 'studadmin/add_student.html', {'student_form': AddStudentForm(),
                                                              'habits_form': AddHabitsForm(),
                                                              'error': 'Bad credentials'})


class ChooseViolationView(View):
    def get(self, request, *args, **kwargs):
        usr = request.user
        form = ChooseViolation()
        return render(request, 'studadmin/choose_violation.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = ChooseViolation(request.POST)
        print(form)
        if form.is_valid() and request.user.is_authenticated():
            form.save()
            return HttpResponse('Violation has been added')
        return render(request, 'studadmin/choose_violation.html', {'form': form})



