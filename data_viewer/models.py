from django.db import models

class App(models.Model):
    name = models.TextField(unique=True)
    last_updated = models.TextField(blank=True, null=True)

class Reviews(models.Model):
    body = models.TextField()
    star_rating = models.IntegerField()
    previous_star_rating = models.IntegerField(blank=True, null=True)
    shop_domain = models.TextField()
    shop_name = models.TextField()
    created_at = models.TextField()
    updated_at = models.TextField(blank=True, null=True)
    app = models.ForeignKey(App, models.DO_NOTHING)