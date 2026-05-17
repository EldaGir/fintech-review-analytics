import pandas as pd
from google_play_scraper import reviews, Sort

# Bank app package names
BANK_APPS = {
    "CBE": "com.combanketh.mobilebanking",
    "BOA": "com.boa.boaMobileBanking",
    "Dashen": "com.dashen.dashensuperapp"
}

all_reviews = []

for bank_name, app_id in BANK_APPS.items():
    print(f"Scraping reviews for {bank_name}...")

    result, continuation_token = reviews(
        app_id,
        lang='en',
        country='et',
        sort=Sort.NEWEST,
        count=500
    )

    for review in result:
        all_reviews.append({
            "review_id": review.get("reviewId"),
            "review": review.get("content"),
            "rating": review.get("score"),
            "date": review.get("at"),
            "bank": bank_name,
            "source": "Google Play"
        })

    print(f"Collected {len(result)} reviews for {bank_name}")

# Convert to DataFrame
df = pd.DataFrame(all_reviews)

print("\nDataset Preview:")
print(df.head())

print(f"\nTotal Reviews Collected: {len(df)}")

# Save raw dataset
df.to_csv("data/raw/bank_reviews_raw.csv", index=False)

print("\nRaw dataset saved successfully.")