from .models import App

def products_processor(request):
    products = App.objects.all()
    return {'products': products}
