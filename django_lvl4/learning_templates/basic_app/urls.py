from django.conf.urls import url 
from . import views

#template tagging
app_name = 'basic_app' #global variabel and set the app name always for use for template tagging
#the name assigned basic_app should match with the url : given in html file
urlpatterns=[
    url(r'^relative/$',views.relative,name='relative'),#asfter regular exp $ is antyhong typed after the relative url
    url(r'^other/$',views.other,name='other'),
]
