# Fintech Review Analytics

Customer Experience Analytics for Ethiopian Fintech Apps

#Project Overview

This project analyzes customer review from Ethiopian banking mobile 
application on the Google play store. the objective is to collect, 
preprocess, analyze, and extract insights from user feedback to help 
banks improve customer experience and product quality. 

The project focuses on three Ethiopian banks:

- Commercial bank of Ethiopia (CBE)
- Bank of Abyssinia (BOA)
- Dashen Bank

The analysis pipeline includes:

-Google Play Store review scraping
-Data preprocessing and cleaning
-sentiment analysis
-thematic analysis
-PostgreSQL database storage
-Data visualization and business insights

#Project Structure
fintech-review-analytics/
│
├── .github/
│   └── workflows/
│       └── unittests.yml
│
├── data/
│   └── raw/
│
├── notebooks/
│
├── scripts/
│   ├── scrape_reviews.py
│   └── preprocess_reviews.py
│
├── src/
├── tests/
│
├── .gitignore
├── README.md
├── requirements.tx

#Technologies used
-python 3.14
-pandas
-google-play-scraper
-Git & GitHub
-GitHub Actions

#Data collection methodology
customer reviews were scraped from the Google Play Store using the 'google-play-scraper'

#Target applications
| Bank | Google Play Package |
|------|----------------------|
| CBE | `com.combanketh.mobilebanking` |
| BOA | `com.boa.boaMobileBanking` |
| Dashen | `com.dashen.dashensuperapp` |

#Collected fields

The following fields were collected:
-review text
-rating (1-5)
-review date
-Bank name
-source

#Dataset Size
-minimum target: 1200 reviews
-collected: 1,500 reviews

Approximately 500 reviews were collected per bank


#Data preprocessing
The preprocessing pipeline included:
-removing duplicate reviews using review IDs
-Handling missing values
-Normalizing date to 'YYYY-MM-DD'
-selecting only required columns

# Final dataset columns
-review
-rating
-date
-bank
-source

#Data quality summary
| Metric | Result |
|---|---|
| Total Reviews Collected | 1500 |
| Duplicate Reviews Removed | 0 |
| Missing Reviews | 0 |
| Missing Ratings | 0 |

The dataset met the project KPI requirements with less than 5% missing data.

#Limitations
-Some Google Play reviews may not be available due to API limitations.
-Review availability depends on the public data exposed by the Google Play Store
-Review counts may change over time as new reviews are posted.

#Setup instructions

### Clone Repository

```bash
git clone <repository-url>
cd fintech-review-analytics
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Git Bash

```bash
source venv/Scripts/activate
```

#### PowerShell

```powershell
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Scripts

### Scrape Reviews

```bash
python scripts/scrape_reviews.py
```

### Preprocess Reviews

```bash
python scripts/preprocess_reviews.py
```

---

## Git Workflow

This project follows a task-based Git workflow:

- `main` → stable production branch
- `task-1` → data collection and preprocessing

Conventional Commits were used for commit messages.

## CI/CD

GitHub Actions is configured to automatically install dependencies on every push to the `main` branch.

Workflow file:

```text
.github/workflows/unittests.yml


# PostgreSQL Database Integration

A PostgreSQL database named `bank_reviews` was created to store the cleaned and processed review data.

## Database Schema

The project uses two relational tables:

### banks
Stores metadata about the banking applications.

Columns:
- bank_id
- bank_name
- app_name

### reviews
Stores processed customer reviews and analytical results.

Columns:
- review_id
- bank_id
- review_text
- rating
- review_date
- sentiment_label
- sentiment_score
- identified_theme
- source

## Technologies Used

- PostgreSQL
- pgAdmin
- SQLAlchemy
- psycopg2

## Verification Queries

The following verification checks were performed:

- Count reviews per bank
- Compute average rating per bank
- Check for null values in key columns

More than 1,500 processed reviews were successfully inserted into the database.