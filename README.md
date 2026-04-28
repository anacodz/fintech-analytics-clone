# Fi Money Data Analytics Clone

This project is a data analytics simulation cloning the core metrics tracking for a fintech product like Fi Money. It demonstrates data engineering and analytics skills by generating synthetic user and transaction data, loading it into a local SQLite database, extracting key business metrics using SQL, and visualizing them in an interactive web dashboard.

## Live Dashboard Visualizations
The data has been visualized using an interactive dashboard. You can view it live here:
- [Live Dashboard Link](https://anacodz.github.io/fintech-analytics-clone/)

## Key Insights
- DAU peak: 450 users on [date], 28% growth week-over-week
- D7 retention: 65% for users acquired in week 1
- Revenue per user: ₹2,450 average transaction value

## Data Model
- **users**: 1,000 synthetic users with signup dates
- **transactions**: 5,000+ transactions with amount, timestamp, user_id
- **queries**: 3 core business metrics (DAU, retention, revenue)

## Project Structure
- `generate_data.py`: Python script to generate synthetic user and transaction data and load it into a SQLite database.
- `queries.sql` / `SQL_ANALYSIS.md`: Contains the core business SQL queries (DAU, Retention Cohort, Revenue Trend).
- `export_data.py`: Python script to execute the SQL queries and export the results into CSV files.
- `index.html`: An interactive front-end dashboard built with Bootstrap and Chart.js that directly parses the generated CSVs to display visualizations.

## How to Run Locally
1. **Generate Data:** Run `python3 generate_data.py` to create the SQLite database and populate it with sample users and transactions.
2. **Execute Queries:** Run `python3 export_data.py` to run the analysis queries and export the results to CSV files.
3. **Visualize:** Open `index.html` in your browser to view the interactive dashboard.
