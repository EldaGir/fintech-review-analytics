-- =========================================
-- Create Banks Table
-- =========================================

CREATE TABLE IF NOT EXISTS banks (

    bank_id SERIAL PRIMARY KEY,

    bank_name VARCHAR(100) NOT NULL UNIQUE,

    app_name VARCHAR(200) NOT NULL
);


-- =========================================
-- Create Reviews Table
-- =========================================

CREATE TABLE IF NOT EXISTS reviews (

    review_id SERIAL PRIMARY KEY,

    bank_id INTEGER REFERENCES banks(bank_id),

    review_text TEXT NOT NULL,

    rating INTEGER,

    review_date DATE,

    sentiment_label VARCHAR(20),

    sentiment_score FLOAT,

    identified_theme VARCHAR(100),

    source VARCHAR(50)
);