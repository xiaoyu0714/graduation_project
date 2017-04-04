from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^index$', views.index, name='index'),
    url(r'^login$',views.login,name='login'),
    url(r'^verify$',views.verify,name='verify'),
    url(r'^sharethings$', views.sharethings, name='sharethings'),
   	url(r'^person$', views.person, name='person'),
   	url(r'^register$',views.register,name='register'),
   	url(r'^modify_personalinfo$',views.modify_personalinfo,name='modify_personalinfo'),
   	url(r'^modify$',views.modify,name='modify'),
   	url(r'^logout$',views.logout,name='logout'),
    url(r'^test$',views.test,name='test'),
    url(r'^test_for_refresh$',views.test_for_refresh,name='test_for_refresh'),
    url(r'^tmp$',views.tmp,name='tmp'),
    url(r'^test_for_person$',views.test_for_person,name='test_for_person'),
    url(r'^test_for_modify$',views.test_for_modify,name='test_for_modify')
]
