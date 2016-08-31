__author__ = 'kirill'


from django.conf.urls import url
from .views import AddStudentView,\
    StudentDetailView,\
    AddPromotionView,\
    StudentListView,\
    index,\
    AddViolationView,\
    ChooseViolationView,\
    Login,\
    Logout,\
    AddViolationToStudentView,\
    AddPromotionToStudentView,\
    ViolationDetail,\
    PromotionDetail




app_name='studadmin'

urlpatterns=[
    url(r'^$',index.as_view(),name='index'),
    url(r'AddStudent/$',AddStudentView.as_view(),name='add_student'),
    url(r'^Students/?page=(?P<page>[0-9]+)/$',StudentListView.as_view(),name='students_list'),
    url(r'^Student/(?P<pk>[0-9]+)/$',StudentDetailView.as_view(),name='student_detail'),
    url(r'^Violation/(?P<pk>[0-9]+)/$',ViolationDetail.as_view(),name='violation_detail'),
    url(r'^AddPromotion/$',AddPromotionView.as_view(),name='add_promotion'),
    url(r'^Promotion/(?P<pk>[0-9]+)/$',PromotionDetail.as_view(),name='promotion_detail'),
    url(r'^AddVioletion/$',AddViolationView.as_view(),name='add_violation'),
    url(r'AddVioletionToStudent/(?P<student_id>[0-9]+)/$',AddViolationToStudentView.as_view(),name='add_violation_to_student'),
    url(r'AddPromotionToStudent/(?P<student_id>[0-9]+)/$',AddPromotionToStudentView.as_view(),name='add_promotion_to_student'),
    url(r'^ChooseViolation/$',ChooseViolationView.as_view(),name='choose_violation'),
    url(r'^Login/$',Login.as_view(),name='login'),
    url(r'^Logout/$',Logout.as_view(),name='logout')
]