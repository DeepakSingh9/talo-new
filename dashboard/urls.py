from django.conf.urls import url
from . import views

urlpatterns=[url(r'^home/(?P<username>[\w.@+-]+)/$',views.home,name='home'),
             url(r'^profile/(?P<username>[\w.@+-]+)/$',views.profile,name='profile'),
             url(r'^logout',views.user_logout,name='logout'),
             #url(r'^account/(?P<pk>\d+)/$',views.account,name='account'),
             url(r'^image_upload/(?P<username>[\w.@+-]+)/$',views.profile_image_upload,name='image_upload'),
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
             url(r'^addeducation/(?P<pk>\d+)/$',views.addeducation,name='addeducation'),
             url(r'^editeducation/(?P<pk>\d+)/$',views.edit_education,name='edit_education'),
             url(r'^delete_video/(?P<pk>\d+)/$',views.delete_video,name='delete_video'),
             url(r'^edit_video/(?P<pk>\d+)/$',views.edit_video,name='edit_video'),
             url(r'^search/$',views.search,name='search'),
             url(r'^follow/(?P<username>[\w.@+-]+)/$',views.follow,name='follow'),
             url(r'^unfollow/(?P<username>[\w.@+-]+)/$',views.unfollow,name='unfollow'),
             url(r'^block/(?P<username>[\w.@+-]+)/$',views.block,name='block'),
             url(r'^unblock/(?P<username>[\w.@+-]+)/$',views.unblock,name='unblock'),
]
