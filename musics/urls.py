from django.urls import path
from . import views


urlpatterns = [
    path('', views.musics, name='musics'),
    path('dashboards/', views.dashboards, name='dashboards'),

    # path('songs/', views.songs, name= 'songs'),
    # path('albums/', views.albums, name= 'albums'),
    # path('organizations/', views.organizations, name= 'organizations')

]
