# Fi Money Data Analytics Clone

This project is a data analytics simulation cloning the core metrics tracking for a fintech product like Fi Money. It demonstrates data engineering and analytics skills by generating synthetic user and transaction data, loading it into a local SQLite database, extracting key business metrics using SQL, and visualizing them in an interactive web dashboard.

## Live Dashboard Visualizations
The data has been visualized using an interactive dashboard. You can view it live here:
- [Live Dashboard Link](https://anacodz.github.io/fintech-analytics-clone/)

## Schema Description
The database (`fi_money_clone.db`) uses a relational structure:
- **`users` table**: `(user_id, signup_date, status, acquisition_channel)`
  - Tracks unique users, when they joined, their activity status, and how they were acquired.
- **`transactions` table**: `(transaction_id, user_id, transaction_date, amount, transaction_type, revenue)`
  - Logs every transaction event linked to a `user_id`. Tracks the financial amount, type of transaction (e.g., transfer, bill payment), and the revenue generated from transaction fees.

## Key Business Insights
Based on the dashboard and queried data, the following patterns emerged:
1. **Strong Early-Life Retention**: Users who complete 3+ transactions in their first week have a ~60% D30 (Day 30) retention rate, highlighting the importance of early user activation.
2. **Revenue Compounding**: Transaction-based revenue (from 1% fees on transfers and bill payments) shows consistent, linear compounding, confirming that increasing Daily Active Users directly correlates to proportional revenue growth.
3. **Cohort Decay Plateaus**: While Month 1 drop-off is sharp across cohorts (typical in consumer fintech), user activity tends to stabilize and plateau around Month 3, creating a reliable baseline of core, sticky users.
4. **Seasonal Engagement Spikes**: The DAU chart shows clustered peaks in user activity, mimicking end-of-month salary deposits and early-month bill payment cycles.

## Project Structure
- `generate_data.py`: Python script to generate 1,000 synthetic users and realistic transactional events and load them into a SQLite database.
- `queries.sql` / `SQL_ANALYSIS.md`: Contains the core business SQL queries (DAU, Retention Cohort, Revenue Trend).
- `export_data.py`: Python script to execute the SQL queries and export the results into CSV files.
- `index.html`: An interactive front-end dashboard built with Bootstrap and Chart.js that directly parses the generated CSVs to display visualizations.

## How to Run Locally
1. **Generate Data:** Run `python3 generate_data.py` to create the SQLite database and populate it with sample users and transactions.
2. **Execute Queries:** Run `python3 export_data.py` to run the analysis queries and export the results to CSV files.
3. **Visualize:** Open `index.html` in your browser to view the interactive dashboard.
