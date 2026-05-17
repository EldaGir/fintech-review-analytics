import pandas as pd
import nltk
import re

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer

from transformers import pipeline


# ----------------------------------------
# Load Dataset
# ----------------------------------------

df = pd.read_csv("data/bank_reviews_cleaned.csv")

print("Dataset loaded successfully.")
print(df.head())


# ----------------------------------------
# Download NLTK Resources
# ----------------------------------------

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('vader_lexicon')


# ----------------------------------------
# Text Preprocessing
# ----------------------------------------

stop_words = set(stopwords.words('english'))


def preprocess_text(text):

    # Convert to lowercase
    text = text.lower()

    # Remove special characters and numbers
    text = re.sub(r'[^a-zA-Z\s]', '', text)

    # Tokenization
    tokens = word_tokenize(text)

    # Remove stopwords
    filtered_tokens = [
        word for word in tokens
        if word not in stop_words
    ]

    # Join cleaned tokens
    cleaned_text = " ".join(filtered_tokens)

    return cleaned_text


df["cleaned_review"] = df["review"].apply(preprocess_text)

print("\nText preprocessing completed.")


# ----------------------------------------
# VADER Sentiment Analysis
# ----------------------------------------

sia = SentimentIntensityAnalyzer()


def vader_sentiment(text):

    score = sia.polarity_scores(text)["compound"]

    if score >= 0.05:
        label = "positive"
    elif score <= -0.05:
        label = "negative"
    else:
        label = "neutral"

    return pd.Series([label, score])


df[["vader_sentiment", "vader_score"]] = (
    df["cleaned_review"]
    .apply(vader_sentiment)
)

print("\nVADER sentiment analysis completed.")


# ----------------------------------------
# DistilBERT Sentiment Analysis
# ----------------------------------------

print("\nLoading DistilBERT model...")

classifier = pipeline("sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)


def bert_sentiment(text):

    try:

        result = classifier(text[:512])[0]

        label = result["label"].lower()
        score = result["score"]

        if label == "positive":
            sentiment = "positive"
        else:
            sentiment = "negative"

        return pd.Series([sentiment, score])

    except Exception:

        return pd.Series(["neutral", 0.0])


df[["bert_sentiment", "bert_score"]] = (
    df["cleaned_review"]
    .apply(bert_sentiment)
)

print("\nDistilBERT sentiment analysis completed.")


# ----------------------------------------
# Sentiment Aggregation
# ----------------------------------------

print("\nAverage sentiment score by bank:")

bank_sentiment = (
    df.groupby("bank")["bert_score"]
    .mean()
)

print(bank_sentiment)


print("\nAverage sentiment score by rating:")

rating_sentiment = (
    df.groupby("rating")["bert_score"]
    .mean()
)

print(rating_sentiment)


# ----------------------------------------
# Save Sentiment Results
# ----------------------------------------

sentiment_df = df[[
    "review",
    "cleaned_review",
    "rating",
    "date",
    "bank",
    "source",
    "vader_sentiment",
    "vader_score",
    "bert_sentiment",
    "bert_score"
]]

sentiment_df.to_csv(
    "data/sentiment_analysis_results.csv",
    index=False
)

print("\nSentiment analysis results saved successfully.")