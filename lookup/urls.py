from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about')
]

# note to self:
# {{ '/' }} in html links to home or {% url 'home' %}
# {{ 'about' }} in html links to home or {% url 'about' %}
# ! USE url syntax to pull name because path could change


