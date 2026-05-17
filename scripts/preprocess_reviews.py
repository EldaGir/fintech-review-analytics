import pandas as pd

#Load raw dataset
df = pd.read_csv("data/raw/bank_reviews_raw.csv")

print("Initial dataset shape:")
print(df.shape)

#Remove duplicate reviews

duplicates_before = df.duplicated(subset=["review_id"]).sum()
df = df.drop_duplicates(subset=["review_id"])
duplicates_after = df.duplicated(subset=["review_id"]).sum()

print(f"\nDuplicate reviews removed: {duplicates_before}")
print(f"Remaining duplicates: {duplicates_after}")

#Handle missing values

missing_review_count = df["review"].isna().sum()
missing_rating_count = df["rating"].isna().sum()

print(f"\nMissing reviews: {missing_review_count}")
print(f"Missing ratings: {missing_rating_count}")

#Drop rows with missing review or rating

df = df.dropna(subset=["review", "rating"])

print("\nDataset shape after dropping missing values:")
print(df.shape)

#Normalize dates

df["date"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d")

#keep only required columns
df = df[["review", "rating", "date", "bank", "source"]]

#save cleaned dataset
df.to_csv("data/bank_reviews_cleaned.csv", index=False)

print("\nCleaned dataset saved successfully.")

print("\nFinal dataset preview:")
print(df.head())