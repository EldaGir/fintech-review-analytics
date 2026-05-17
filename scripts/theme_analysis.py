import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer


# ----------------------------------------
# Load Sentiment Dataset
# ----------------------------------------

df = pd.read_csv("data/sentiment_analysis_results.csv")

df["cleaned_review"] = (
    df["cleaned_review"]
    .fillna("")
)

print("Dataset loaded successfully.")


# ----------------------------------------
# TF-IDF Keyword Extraction
# ----------------------------------------

vectorizer = TfidfVectorizer(
    max_features=100,
    stop_words='english',
    ngram_range=(1, 2)
)

X = vectorizer.fit_transform(df["cleaned_review"])

feature_names = vectorizer.get_feature_names_out()


# ----------------------------------------
# Display Top Keywords
# ----------------------------------------

tfidf_scores = X.sum(axis=0).A1

keywords_df = pd.DataFrame({
    "keyword": feature_names,
    "score": tfidf_scores
})

keywords_df = keywords_df.sort_values(
    by="score",
    ascending=False
)

print("\nTop Keywords and Bigrams:")
print(keywords_df.head(30))


# ----------------------------------------
# Theme Identification Function
# ----------------------------------------

def identify_theme(review):

    review = str(review).lower()

    # Account Access Issues
    if any(word in review for word in [
        "login",
        "log in",
        "password",
        "otp",
        "access",
        "signin",
        "verification",
        "verify",
        "account blocked",
        "cant open",
        "cannot open"
    ]):
        return "Account Access Issues"

    # Transaction Performance
    elif any(word in review for word in [
        "transfer",
        "transaction",
        "slow",
        "loading",
        "payment",
        "delay",
        "failed",
        "processing",
        "network",
        "timeout"
    ]):
        return "Transaction Performance"

    # App Stability & Bugs
    elif any(word in review for word in [
        "crash",
        "bug",
        "error",
        "issue",
        "problem",
        "stuck",
        "fix",
        "broken"
    ]):
        return "App Stability & Bugs"

    # UI & Design
    elif any(word in review for word in [
        "ui",
        "design",
        "interface",
        "easy",
        "navigation",
        "layout",
        "user friendly",
        "experience"
    ]):
        return "UI & Design"

    # Customer Support
    elif any(word in review for word in [
        "support",
        "service",
        "help",
        "customer",
        "response",
        "call center"
    ]):
        return "Customer Support"

    # Feature Requests
    elif any(word in review for word in [
        "feature",
        "update",
        "fingerprint",
        "dark mode",
        "option",
        "notification",
        "biometric"
    ]):
        return "Feature Requests"

    else:
        return "Other"

df["identified_theme"] = (
    df["cleaned_review"]
    .apply(identify_theme)
)


# ----------------------------------------
# Theme Frequency
# ----------------------------------------

print("\nTheme Distribution:")

theme_counts = (
    df["identified_theme"]
    .value_counts()
)

print(theme_counts)


# ----------------------------------------
# Theme Distribution by Bank
# ----------------------------------------

print("\nTheme Distribution by Bank:")

bank_theme_distribution = (
    pd.crosstab(
        df["bank"],
        df["identified_theme"]
    )
)

print(bank_theme_distribution)


# ----------------------------------------
# Save Final Task 2 Dataset
# ----------------------------------------

final_df = df[[
    "review",
    "cleaned_review",
    "bank",
    "rating",
    "date",
    "bert_sentiment",
    "bert_score",
    "identified_theme"
]]

final_df.to_csv(
    "data/task2_final_results.csv",
    index=False
)

print("\nTask 2 final dataset saved successfully.")