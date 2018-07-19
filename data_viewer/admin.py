from django.contrib import admin

# Register your models here.
from .models import App, Reviews

admin.site.register(App)
admin.site.register(Reviews)