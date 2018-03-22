from django.conf.urls import include,url
from . import views

urlpatterns=[
    url('^$',views.index),
    url('^index$', views.index),
    url('^login$', views.userlogin,name='login'),
    url('^logout$', views.userlogout,name='logout'),
    url('^list/',views.RecoreList.as_view()),
    url('^listing$',views.listing)
]