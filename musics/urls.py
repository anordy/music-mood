from django.urls import path
from . import views


urlpatterns = [
    path('', views.musics, name='musics'),
    path('dashboards/', views.dashboards, name='dashboards'),
    path('songs/', views.songs, name= 'songs'),
    path('albums/', views.albums, name= 'albums'),
    path('artists/', views.artists, name= 'artists'),
    path('browse/', views.browse, name= 'browse'),
    path('radio/', views.radio, name= 'radio'),
    path('upload/', views.upload, name= 'upload'),

    # path('organizations/', views.organizations, name= 'organizations')

]
