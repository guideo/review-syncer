from django.urls import path

from . import views

app_name = 'data_viewer'
urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('charts/', views.charts, name='charts'),
    path('monthlyreviews/', views.monthlyreviews, name='monthlyreviews'),
    #path('publicacoes/', views.publicacoes, name='publicacoes'),
    #path('publicacoes/<int:artigo_id>/<str:artigo_title>/', views.artigo, name='artigo'),
]