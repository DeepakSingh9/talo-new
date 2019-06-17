from django.conf.urls import url
from . import views

urlpatterns=[url(r'^signin/$',views.user_login,name='signin'),
             url(r'^signup/$',views.user_registration,name='signup'),
             url(r'^logout/$',views.user_logout,name='logout'),

]
