from django.conf.urls import url,include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^error',views.error,name='error'),
    url(r'^search/', views.search, name='search'),
    url(r'^viewdetails/(\d+)', views.viewdetails, name='viewdetails'),
    url(r'^comment/(\d+)',views.comment, name='comment'),

]
