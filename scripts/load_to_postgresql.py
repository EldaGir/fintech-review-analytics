import pandas as pd
from sqlalchemy import create_engine


# ----------------------------------------
# PostgreSQL Connection
# ----------------------------------------

USERNAME = "postgres"
PASSWORD = "PostgreSQL"
HOST = "localhost"
PORT = "5432"
DATABASE = "bank_reviews"


engine = create_engine(
    f"postgresql+psycopg2://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
)


# ----------------------------------------
# Load Final Dataset
# ----------------------------------------

df = pd.read_csv("data/task2_final_results.csv")

print("Dataset loaded successfully.")


# ----------------------------------------
# Create Banks Table Data
# ----------------------------------------

banks_df = pd.DataFrame({

    "bank_name": [
        "CBE",
        "BOA",
        "Dashen"
    ],

    "app_name": [
        "Commercial Bank of Ethiopia",
        "Bank of Abyssinia",
        "Dashen Bank"
    ]
})


# ----------------------------------------
# Insert Banks Data
# ----------------------------------------

banks_df.to_sql(
    "banks",
    engine,
    if_exists="append",
    index=False
)

print("Banks table populated.")


# ----------------------------------------
# Retrieve Bank IDs
# ----------------------------------------

bank_lookup = pd.read_sql(
    "SELECT bank_id, bank_name FROM banks",
    engine
)

bank_mapping = dict(
    zip(
        bank_lookup["bank_name"],
        bank_lookup["bank_id"]
    )
)

df["bank_id"] = df["bank"].map(bank_mapping)


# ----------------------------------------
# Prepare Reviews Table
# ----------------------------------------

reviews_df = df[[
    "bank_id",
    "review",
    "rating",
    "date",
    "bert_sentiment",
    "bert_score",
    "identified_theme",
    "source"
]].copy()


reviews_df.columns = [
    "bank_id",
    "review_text",
    "rating",
    "review_date",
    "sentiment_label",
    "sentiment_score",
    "identified_theme",
    "source"
]


# ----------------------------------------
# Insert Reviews
# ----------------------------------------

reviews_df.to_sql(
    "reviews",
    engine,
    if_exists="append",
    index=False
)

print("Reviews inserted successfully.")

print(f"Total inserted reviews: {len(reviews_df)}")