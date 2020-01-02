from django.conf.urls import url
from mainApp import views

#template tagging
app_name = 'mainApp'
urlpatterns=[
    url(r'^inputPage/$',views.inputpage,name='inputPage'),
    url(r'^Results/$',views.result,name='results'),
]
