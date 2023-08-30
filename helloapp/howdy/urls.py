from django.urls import path
from howdy import views

urlpatterns = [
    path('', views.HomePageView.as_view()),
    path('about/', views.AboutPageView.as_view(), name='about')
]
