from django.conf.urls import patterns, url

from AssistMe import views

urlpatterns = patterns('',
    url(r'^animate/$', views.animateView, name='animateView'),
    url(r'^studies/$', views.StudiesView.as_view(), name='studies'), 
    url(r'^studies/(?P<pk>\d+)/$', views.DisciplinesView.as_view(), name='disciplines'),
    url(r'^studies/disciplines/(?P<pk>\d+)/$', views.MajorsView.as_view(), name='majors'),
    url(r'^studies/disciplines/majors/(?P<pk>\d+)/$', views.ArticulationsView.as_view(), name='articulations'),

)