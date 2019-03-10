from django.conf.urls import url
from . import views

urlpatterns=[url(r'^signup/$',views.user_login,name='login'),
             url(r'^registration/$',views.user_registration,name='registration'),
             url(r'^logout/$',views.user_logout,name='logout'),

]
