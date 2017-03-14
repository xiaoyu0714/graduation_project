from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^index$', views.index, name='index'),
    url(r'^login$',views.login,name='login'),
    url(r'^verify$',views.verify,name='verify'),
    url(r'^sharethings$', views.sharethings, name='sharethings'),
   	url(r'^things_can_be_borrowed$', views.things_can_be_borrowed, name='things_can_be_borrowed'),
   	url(r'^register$',views.register,name='register'),
   	url(r'^modify_personalinfo$',views.modify_personalinfo,name='modify_personalinfo'),
   	url(r'^modify$',views.modify,name='modify')

]
   