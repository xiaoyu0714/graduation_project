from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login$',views.login,name='login'),
    url(r'^register$',views.register,name='register'),
    url(r'^verify$',views.verify,name='verify'),
    url(r'^index$', views.index, name='index'),
    url(r'^person_info$',views.person_info,name='person_info'),
    url(r'^object_upload$',views.object_upload,name='object_upload'),
    url(r'^logout$',views.logout,name='logout'),
    url(r'^person_info_modify$',views.person_info_modify,name='person_info_modify'),
    url(r'^order_submit$',views.order_submit,name='order_submit'),
    url(r'^search$',views.search,name='search'),
    url(r'^borrowthings$',views.borrowthings,name='borrowthings')
]
