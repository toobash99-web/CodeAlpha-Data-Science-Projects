```python
# CodeAlpha Data Science Internship - Project Portfolio

This repository contains my complete project submissions for the CodeAlpha Data Science Internship. It showcases my skills in **Exploratory Data Analysis**, **Interactive Visualization**, **Natural Language Processing (Sentiment Analysis)**, and **Web Scraping**.

---

## 📁 Projects Included

### 1. Exploratory Data Analysis (EDA) & Visualization - Seoul Bike Sharing
- **Objective**: Analyze 8,760 hourly bike rental records to identify demand patterns and optimize fleet operations.
- **Key Findings**:
  - Summer demand is ~808 rentals/hour higher than Winter (proven via ANOVA & Tukey HSD).
  - Peak hour is **6:00 PM** with an average of **1,503 rentals**.
  - Rain reduces demand by a staggering **77.9%** (statistically significant, p < 0.001).
  - Temperature has a non-linear (curved) effect; demand peaks around 25°C.
- **Key Visuals**: Interactive Plotly dashboards, 3D weather heatmaps, and an Executive Decision Dashboard.
- **Technologies**: Python, Pandas, Seaborn, Matplotlib, Plotly, Scipy (Stats).

---

### 2. Sentiment Analysis - Airline Tweets
- **Objective**: Classify 14,000+ airline tweets as Positive, Negative, or Neutral to gauge public opinion.
- **Approaches**:
  - *VADER (Rule-Based)*: Achieved baseline accuracy.
  - *Logistic Regression + TF-IDF (ML)*: Achieved superior performance, identifying top complaint words.
- **Key Findings**:
  - ~60%+ of tweets express negative sentiment.
  - Top complaints: Flight delays, cancellations, and baggage issues.
  - Positive tweets often mention "good," "great," and "thanks."
- **Technologies**: NLTK, Scikit-learn, WordCloud, VADER Lexicon.

---

### 3. Web Scraping & Analysis - Show HN Launch Analyzer (Bonus Project)
- **Objective**: Scrape 115 "Show HN" posts from Hacker News to analyze what makes a startup launch successful.
- **Process**:
  - Built a custom scraper using `Requests` and `BeautifulSoup`.
  - Extracted titles, URLs, upvotes, and comments.
  - Stored data in Pandas and exported to Excel for manual review.
- **Key Findings**:
  - **GitHub** hosts **41%** of all Show HN launches (dominates the platform).
  - **Short titles** (<50 characters) get approximately **17% more upvotes** than long ones.
  - The most viral post was *"Hacker News Trends"* with **814 upvotes**.
- **Challenges Overcome**: Fixed DNS connection errors using `try-except` blocks and debugged HTML parsing to accurately extract upvotes.
- **Technologies**: Python, Requests, BeautifulSoup, Pandas, Openpyxl.

---

## 🛠️ How to Run These Projects

### Prerequisites
Make sure you have Python installed. Then install the required libraries:
```bash
pip install pandas numpy matplotlib seaborn plotly scipy scikit-learn nltk wordcloud requests beautifulsoup4 openpyxl
```
