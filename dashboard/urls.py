from django.conf.urls import url
from . import views

urlpatterns=[url(r'^home/(?P<username>[\w.@+-]+)/$',views.home,name='home'),
             #url(r'^account/(?P<pk>\d+)/$',views.account,name='account'),
             url(r'^image_upload/(?P<pk>\d+)/$',views.profile_image_upload,name='image_upload'),
             url(r'^uploadskills/$',views.uploadskills,name='uploadskills'),
             url(r'^aboutme/(?P<pk>\d+)/$',views.aboutme,name='aboutme'),
             url(r'^editaboutme/(?P<pk>\d+)/$',views.edit_aboutme,name='edit_aboutme'),
             url(r'^learning/$',views.learning,name='learning'),
             url(r'^addskills/$',views.addskills,name='addskills'),
             url(r'^edit_skill/(?P<pk>\d+)/$',views.edit_skill,name='edit_skills'),
             url(r'^delete_skill/(?P<pk>\d+)/$',views.delete_skill,name='delete_skills'),
             url(r'^addcontact/$',views.addcontact,name='addcontact'),
             url(r'^edit_contact/(?P<pk>\d+)/$',views.edit_contact,name='edit_contact'),
             url(r'^delete_contact/(?P<pk>\d+)/$',views.delete_contact,name='delete_contact'),
             url(r'^follow/(?P<pk>\d+)/$',views.follow,name='follow'),
]
