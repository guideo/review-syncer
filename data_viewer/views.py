from django.shortcuts import render
import sqlite3
from .models import App, Review
from datetime import datetime, timezone
from dateutil.relativedelta import relativedelta
import calendar

FORMAT_TIME = "%Y-%m-%dT%H:%M:%S.%f%z"
PRODUCTS = ["product-upsell", "product-discount", "store-locator",
            "product-options", "quantity-breaks", "product-bundles",
            "customer-pricing", "product-builder", "social-triggers",
            "recurring-orders", "multi-currency", "quickbooks-online",
            "xero", "the-bold-brain"]

def last_twelve_months(review_list):
    d = {}
    for r in review_list:
        r_date = r.created_at
        if r.updated_at is not None:
            r_date = r.updated_at
        if r_date > datetime.now(timezone.utc) - relativedelta(years=1):
            if calendar.month_name[r_date.month] in d:
                d[calendar.month_name[r_date.month]] += 1
            else:
                d[calendar.month_name[r_date.month]] = 1
    return d

def index(request):
    reviews = Review.objects.all()
    review_per_product = {}
    for p in PRODUCTS:
        review_per_product[p] = Review.objects.filter(app_id__name=p)
    dict_reviews = last_twelve_months(reviews)
    months = []
    month_reviews = []
    for key, value in dict_reviews.items():
        months += [key]
        month_reviews += [value]
    months = list(reversed(months))
    month_reviews = list(reversed(month_reviews))
    last_data_update_time = str(datetime.now().hour)
    next_data_update_time = ""
    if datetime.now().minute < 30:
        next_data_update_time = last_data_update_time + ":30"
        last_data_update_time += ":00"
    else:
        next_data_update_time = str((datetime.now() + relativedelta(minutes=30)).hour) + ":00"
        last_data_update_time += ":30"
    latest_reviews = [r for r in Review.objects.order_by('-created_at')[:20]]
    latest_updates = [u for u in Review.objects.order_by('-updated_at')[:20]]
    aux = []
    for review in latest_reviews:
        if latest_updates[0].updated_at > review.created_at:
            aux += latest_updates[:1]
            latest_updates = latest_updates[1:]
        else:
            aux += [review]
    return render(request, 'data_viewer/index.html', {'months': months, 'reviews': month_reviews, 'review_per_product': review_per_product,
                    'last_update': last_data_update_time, 'next_update': next_data_update_time, 'latest_reviews': aux})

def charts(request):
    return render(request, 'data_viewer/charts.html')