__author__ = 'kirill'

from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from .views import AddStudentView, \
    StudentDetailView, \
    AddPromotionView, \
    StudentListView, \
    index, \
    AddViolationView, \
    ChooseViolationView, \
    Login, \
    Logout, \
    AddViolationToStudentView, \
    AddPromotionToStudentView, \
    ViolationDetail, \
    PromotionDetail

app_name = 'studadmin'



violation_patterns = [url(r'^add_violetion/$', login_required(AddViolationView.as_view()), name='add_violation'),
                      url(r'add_violetion_to_student/(?P<student_id>[0-9]+)/$', AddViolationToStudentView.as_view(),
                          name='add_violation_to_student'),
                      url(r'^(?P<pk>[0-9]+)/$', login_required(ViolationDetail.as_view()), name='violation_detail'),
                      url(r'^choose_violation/$', ChooseViolationView.as_view(), name='choose_violation'),
                      ]

promotion_patterns = [url(r'^add_promotion/$', login_required(AddPromotionView.as_view()), name='add_promotion'),
                      url(r'^(?P<pk>[0-9]+)/$', login_required(PromotionDetail.as_view()), name='promotion_detail'),
                      url(r'add_promotion_to_student /(?P<student_id>[0-9]+)/$', AddPromotionToStudentView.as_view(),
                          name='add_promotion_to_student'), ]



urlpatterns = [
    url(r'^$', index.as_view(), name='index'),
    url(r'add_student/$', AddStudentView.as_view(), name='add_student'),
    url(r'^students_list//?page=(?P<page>[0-9]+)/$', StudentListView.as_view(), name='students_list'),
    url(r'^student_detail/(?P<pk>[0-9]+)/$', StudentDetailView.as_view(), name='student_detail'),
    url(r'violation/',include(violation_patterns)),
    url(r'promotion/',include(promotion_patterns)),
    url(r'^Login/$', Login.as_view(), name='login'),
    url(r'^Logout/$', Logout.as_view(), name='logout')
]
