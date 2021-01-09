from django.urls import path
from . import views
# single dot means current directory or root


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('finches/', views.finches_index, name='index'),
]
