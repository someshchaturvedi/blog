from django.conf.urls import url
from . import views

app_name = 'cogni'
urlpatterns = [
  url(r'^$' , views.index.as_view() , name='index'),
  url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
  url(r'^about/$' , views.about , name = 'about'),
 ]
