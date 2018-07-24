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

# Return a dict containing number of reviews for the past 12 months (including current)
def last_twelve_months(review_list):
    d = {}
    for r in review_list:
        r_date = r.created_at
        if r.updated_at is not None:
            r_date = r.updated_at
        if r_date > datetime.now(timezone.utc) - relativedelta(years=1):
            if calendar.month_name[r_date.month] in d:
                d[calendar.month_name[r_date.month]] += [r]
            else:
                d[calendar.month_name[r_date.month]] = []
                d[calendar.month_name[r_date.month]] += [r]
    return d

def index(request):
    reviews = Review.objects.all()
    review_per_product = {}
    for p in PRODUCTS:
        review_per_product[p] = Review.objects.filter(app_id__name=p)
    dict_reviews = last_twelve_months(reviews)
    months = []
    month_reviews = []
    for key in dict_reviews.keys():
        months += [key]
        month_reviews += [len(dict_reviews[key])]
    # Month names for the chart legend
    months = list(reversed(months))
    # Montly reviews (number)
    month_reviews = list(reversed(month_reviews))
    
    # Count number of reviews per star from this month
    this_month = calendar.month_name[datetime.now().month]
    reviews_per_rating = [0, 0, 0, 0, 0]
    for review in dict_reviews[this_month]:
        reviews_per_rating[review.star_rating-1] += 1
    
    # Last time database was probably updated
    last_data_update_time = str(datetime.now().hour)
    # Next update time
    next_data_update_time = ""
    if datetime.now().minute < 30:
        next_data_update_time = last_data_update_time + ":30"
        last_data_update_time += ":00"
    else:
        next_data_update_time = str((datetime.now() + relativedelta(minutes=30)).hour) + ":00"
        last_data_update_time += ":30"
    
    # Retrieving info to display on index Review session
    reviews_to_display = 5
    latest_reviews = [r for r in Review.objects.order_by('-created_at')[:reviews_to_display]]
    latest_updates = [u for u in Review.objects.order_by('-updated_at')[:reviews_to_display]]
    aux = []
    while len(aux) < reviews_to_display:
        # If review was already added (can happen if review was both created and updated recently), remove from list and go to next iteration
        if latest_reviews[0] in aux:
            print('remove review')
            latest_reviews = latest_reviews[1:]
            continue
        if latest_updates[0] in aux:
            print('remove update')
            latest_updates = latest_updates[1:]
            continue
        # If review in updated_list was updated earlier then created review from created_list
        if latest_updates[0].updated_at > latest_reviews[0].created_at:
            aux += latest_updates[:1]
            latest_updates = latest_updates[1:]
            print('if')
        else:
            aux += [latest_reviews[0]]
            latest_reviews = latest_reviews[1:]
            print('else')
    
    return render(request, 'data_viewer/index.html', {'months': months, 'reviews': month_reviews, 'reviews_per_rating': reviews_per_rating, 'review_per_product': review_per_product,
                    'last_update': last_data_update_time, 'next_update': next_data_update_time, 'latest_reviews': aux})

def charts(request):
    return render(request, 'data_viewer/charts.html')