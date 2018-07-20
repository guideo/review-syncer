from django.contrib import admin

# Register your models here.
from .models import App, Review

admin.site.register(App)
admin.site.register(Review)