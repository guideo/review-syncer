from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'data_viewer/index.html')

def charts(request):
    return render(request, 'data_viewer/charts.html')