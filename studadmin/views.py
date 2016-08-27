from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import DetailView, ListView
from .forms import AddStudentForm, AddPromotion, AddStaffForm, AddViolation, ChooseViolation, AddHabitsForm
from .models import *


# Create your views here.

class index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'studadmin/index.html')


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
        if form.is_valid() and request.user.is_authenticated():
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
        if form.is_valid() and request.user.is_authenticated():
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
        if request.user.is_authenticated():
            student_form = AddStudentForm(request.POST)
            habits_form = AddHabitsForm(request.POST)
            if student_form.is_valid() and habits_form.is_valid():
                student = student_form.save()
                student.habits_set = habits_form.cleaned_data
                return render(request, 'studadmin/add_student.html', {'student_form': AddStudentForm(),
                                                                      'habits_form': AddHabitsForm(),
                                                                      'notification': 'User has been succesfully added '})
        return render(request, 'studadmin/add_student.html', {'student_form': student_form,
                                                              'habits_form': habits_form,
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



