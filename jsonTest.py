import urllib.request, json
import sqlite3
import sys
from datetime import datetime
import time

#######################
### Constant Values ###
#######################
# BOLD Products
PRODUCTS = ["product-upsell", "product-discount", "store-locator",
            "product-options", "quantity-breaks", "product-bundles",
            "customer-pricing", "product-builder", "social-triggers",
            "recurring-orders", "multi-currency", "quickbooks-online",
            "xero", "the-bold-brain"]
# Base request URL
BASE_URL = "https://apps.shopify.com/{}/reviews.json"
# Format for time
FORMAT_TIME = "%Y-%m-%dT%H:%M:%S.%f%z"

# Creating Database Connections
DB_conn = sqlite3.connect('db.sqlite3')
DB_cursor = DB_conn.cursor()

# Function to check if review is update or new review
def isUpdate(review):
    DB_cursor.execute("SELECT * FROM reviews WHERE shop_domain=? and app_id=?", (review[2], review[5]))
    current_review = DB_cursor.fetchall()
    if len(current_review) > 0:
        return True
    else:
        return False

# Creating tables for reviews and apps if they do not yet exist
DB_cursor.execute('''CREATE TABLE IF NOT EXISTS reviews
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    body TEXT NOT NULL,
                    star_rating INTEGER NOT NULL,
                    previous_star_rating INTEGER,
                    shop_domain TEXT NOT NULL,
                    shop_name TEXT NOT NULL,
                    created_at TEXT NOT NULL,
                    updated_at TEXT,
                    app_id TEXT NOT NULL,
                    FOREIGN KEY (app_id) REFERENCES app(id) ON DELETE CASCADE ON UPDATE NO ACTION)''')
DB_cursor.execute('''CREATE TABLE IF NOT EXISTS app
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL UNIQUE,
                    last_updated TEXT DEFAULT "1900-01-01T00:00:00.000+0000")''')

# Inserting an entry for each BOLD Product
for p in PRODUCTS:
    try:
        DB_cursor.execute("INSERT INTO app(name) VALUES (?)", (p,))
    except:
        print("Unexpected error:")
        for item in sys.exc_info():
            print("\t", item)
DB_conn.commit()

# Inserting each new review into reviews table
while True:
    for p in PRODUCTS:
        print("\n\n##########")
        print(p)
        with urllib.request.urlopen(BASE_URL.format(p)) as url:
            data = json.loads(url.read().decode())
            DB_cursor.execute("SELECT last_updated FROM app WHERE name=?", (p,))
            # Last updated time for Project
            p_datetime = datetime.strptime(DB_cursor.fetchone()[0], FORMAT_TIME)
            # Value which will be used to update 'last updated' time for project
            new_datetime = p_datetime
            new_reviews = []
            update_reviews = []
            for d in data['reviews']:
                # Removing ':' from timestamp
                date_val = d['created_at']
                date_val = date_val[:date_val.rfind(':')] + date_val[date_val.rfind(':')+1:]
                d_datetime = datetime.strptime(date_val, FORMAT_TIME)
                # If review datetime is newer than project last updated datetime
                if d_datetime > p_datetime:
                    entry = (d['body'], d['star_rating'], d['shop_domain'], d['shop_name'], date_val, p)
                    if isUpdate(entry):
                        update_reviews += [entry]
                        DB_cursor.execute("SELECT star_rating FROM reviews WHERE shop_domain=? and app_id=?", (entry[2], entry[5]))
                        previous_star = DB_cursor.fetchone()[0]
                        DB_cursor.execute("UPDATE reviews SET body=?, star_rating=?, previous_star_rating=?, updated_at=? WHERE shop_domain=? and app_id=?", (entry[0], entry[1], previous_star, entry[4], entry[2], entry[5]))
                    else:
                        new_reviews += [entry]
                        DB_cursor.execute("INSERT INTO reviews(body, star_rating, shop_domain, shop_name, created_at, app_id) VALUES (?,?,?,?,?,?)", entry)
                    # In order to get only the newest datetime among new reviews
                    if d_datetime > new_datetime:
                        new_datetime = d_datetime
                else:
                    break
            if len(new_reviews) > 0 or len(update_reviews) > 0:
                DB_cursor.execute("UPDATE app SET last_updated=? WHERE name=?", (new_datetime.strftime(FORMAT_TIME), p))
                DB_conn.commit()
                print("Inserted {} new reviews into {} project".format(len(new_reviews), p))
                print("Updated {} reviews into {} project".format(len(update_reviews), p))

    print("#############################\n\n\n\n\n")
    print("Sleeping for 15 minutes")
    time.sleep(900)
