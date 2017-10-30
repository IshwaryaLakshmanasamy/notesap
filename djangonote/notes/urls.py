from django.conf.urls import patterns, url, include
from django.contrib import admin
from notes import views
urlpatterns = patterns('',
                       url(r'^$', views.index_view, name='index'),
                       url(r'^add_note/', views.add_note, name='add_note'),
                       url(r'^add_tag/', views.add_tag, name='add_tag'),
                       )
