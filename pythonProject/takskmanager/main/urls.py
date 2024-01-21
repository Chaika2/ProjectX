from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('actual', views.actual, name='act'),
    path('geo', views.geo, name='geo'),
    path('last', views.last, name='last'),
    path('skills', views.skills, name='skills')
]
