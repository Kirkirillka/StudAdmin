__author__ = 'kirill'


from django.conf.urls import url
from .views import AddStudentView,StudentDetailView,AddPromotionView,StudentListView,index,AddViolationView,ChooseViolationView



app_name='studadmin'

urlpatterns=[
    url(r'^$',index.as_view(),name='index'),
    url(r'AddStudent/$',AddStudentView.as_view(),name='add_student'),
    url(r'^Students/?page=(?P<page>[0-9]+)/$',StudentListView.as_view(),name='students_list'),
    url(r'^Student/(?P<pk>[0-9]+)/$',StudentDetailView.as_view(),name='student_detail'),
    url(r'^AddPromotion/$',AddPromotionView.as_view(),name='add_promotion'),
    url(r'^AddVioletion/$',AddViolationView.as_view(),name='add_violation'),
    url(r'^ChooseViolation/$',ChooseViolationView.as_view(),name='choose_violation')
]