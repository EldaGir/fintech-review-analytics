import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ----------------------------------------
# Load Dataset
# ----------------------------------------

df = pd.read_csv("data/task2_final_results.csv")

print("Dataset loaded successfully.")


# ----------------------------------------
# Create Output Folder
# ----------------------------------------

import os

os.makedirs("visualizations", exist_ok=True)


# ----------------------------------------
# Plot 1: Sentiment Distribution by Bank
# ----------------------------------------

plt.figure(figsize=(10, 6))

sns.countplot(
    data=df,
    x="bank",
    hue="bert_sentiment"
)

plt.title("Sentiment Distribution by Bank")
plt.xlabel("Bank")
plt.ylabel("Number of Reviews")

plt.tight_layout()

plt.savefig(
    "visualizations/sentiment_distribution_by_bank.png"
)

plt.close()


# ----------------------------------------
# Plot 2: Rating Distribution by Bank
# ----------------------------------------

plt.figure(figsize=(10, 6))

sns.boxplot(
    data=df,
    x="bank",
    y="rating"
)

plt.title("Rating Distribution by Bank")
plt.xlabel("Bank")
plt.ylabel("Rating")

plt.tight_layout()

plt.savefig(
    "visualizations/rating_distribution_by_bank.png"
)

plt.close()


# ----------------------------------------
# Plot 3: Theme Frequency
# ----------------------------------------

theme_counts = (
    df["identified_theme"]
    .value_counts()
)

plt.figure(figsize=(12, 6))

theme_counts.plot(
    kind="bar"
)

plt.title("Theme Frequency Across Reviews")
plt.xlabel("Theme")
plt.ylabel("Frequency")

plt.tight_layout()

plt.savefig(
    "visualizations/theme_frequency.png"
)

plt.close()


# ----------------------------------------
# Plot 4: Top Keywords
# ----------------------------------------

from sklearn.feature_extraction.text import TfidfVectorizer


vectorizer = TfidfVectorizer(
    max_features=15,
    stop_words='english'
)

X = vectorizer.fit_transform(
    df["cleaned_review"].fillna("")
)

keywords = vectorizer.get_feature_names_out()

scores = X.sum(axis=0).A1


keywords_df = pd.DataFrame({
    "keyword": keywords,
    "score": scores
})

keywords_df = keywords_df.sort_values(
    by="score",
    ascending=True
)

plt.figure(figsize=(10, 6))

plt.barh(
    keywords_df["keyword"],
    keywords_df["score"]
)

plt.title("Top Keywords Across Reviews")
plt.xlabel("TF-IDF Score")
plt.ylabel("Keyword")

plt.tight_layout()

plt.savefig(
    "visualizations/top_keywords.png"
)

plt.close()


# ----------------------------------------
# Plot 5: Sentiment Trend Over Time
# ----------------------------------------

df["date"] = pd.to_datetime(df["date"])

trend_df = (
    df.groupby("date")
    .size()
)

plt.figure(figsize=(12, 6))

trend_df.plot()

plt.title("Review Volume Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Number of Reviews")

plt.tight_layout()

plt.savefig(
    "visualizations/review_trend_over_time.png"
)

plt.close()


print("All visualizations generated successfully.")