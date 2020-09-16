#from django.conf.urls import patterns, url
from django.urls import path

from . import views


urlpatterns = [
    #path('business_info/',views.business_info,name='business_info'),
    #path('edit_business/', views.edit_business, name='edit_business'),
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    #path('new_business/', views.new_business, name='new_business'),
    #path('op_result/', views.op_result, name='op_result'),
    #path('do_login/', views.do_login, name='do_login'),
    #path('do_new_business/', views.do_new_business, name='do_new_business'),
    #path('do_edit_business/', views.do_edit_business, name='do_edit_business'),
    #path('open_business/', views.open_business, name='open_business'),
    #path('close_business/', views.close_business, name='close_business'),
    #path('delete_business/', views.delete_business, name='delete_business'),
    #path('analysis_record/', views.analysis_record, name='analysis_record'),
]
