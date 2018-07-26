from django.urls import path

from . import views

app_name = 'data_viewer'
urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('monthlyreviews/', views.monthlyreviews, name='monthlyreviews'),
    path('reviews/', views.reviews, name='reviews'),
    path('reviews_json/', views.reviews_json, name='reviews_json'),
    path('insight/', views.insight, name='insight'),
]