#from django.conf.urls import patterns, url
from django.urls import path

from analysis import views


urlpatterns = [
    url(r'^business_info/',views.business_info,name='business_info'),
    url(r'^edit_business/', views.edit_business, name='edit_business'),
    url(r'^index/', views.index, name='index'),
    url(r'^login/', views.login, name='login'),
    url(r'^new_business/', views.new_business, name='new_business'),
    url(r'^op_result/', views.op_result, name='op_result'),
    url(r'^do_login/', views.do_login, name='do_login'),
    url(r'^do_new_business/', views.do_new_business, name='do_new_business'),
    url(r'^do_edit_business/', views.do_edit_business, name='do_edit_business'),
    url(r'^open_business/', views.open_business, name='open_business'),
    url(r'^close_business/', views.close_business, name='close_business'),
    url(r'^delete_business/', views.delete_business, name='delete_business'),
    url(r'^analysis_record/', views.analysis_record, name='analysis_record'),

]