# Fi Money Data Analytics Clone

This project is a data analytics simulation cloning the core metrics tracking for a fintech product like Fi Money. It demonstrates data engineering and analytics skills by generating synthetic user and transaction data, loading it into a local SQLite database, and extracting key business metrics using SQL.

## Project Structure
- `generate_data.py`: Python script to generate synthetic user and transaction data and load it into a SQLite database (`fi_money_clone.db`).
- `queries.sql`: Contains the 3 core business SQL queries:
  1. Daily Active Users (DAU)
  2. Retention Cohort Analysis
  3. Revenue Trend
- `export_data.py`: Python script to execute the SQL queries and export the results into CSV files for easy visualization in tools like Tableau.
- `*.csv`: Exported data for Daily Active Users, Retention Cohort, and Revenue Trend.

## Visualizations
The data has been visualized using Tableau Public. You can view the interactive dashboard here:
- [Tableau Public Dashboard Link] (Replace with your actual link)

## Video Walkthrough
Watch a quick 2-minute walkthrough of the project, including the SQL queries and the Tableau dashboard:
- [Video Walkthrough Link] (Replace with your actual link)

## How to Run Locally
1. **Generate Data:** Run `python3 generate_data.py` to create the SQLite database and populate it with sample users and transactions.
2. **Execute Queries:** Run `python3 export_data.py` to run the analysis queries and export the results to CSV files.
3. **Visualize:** Import the generated `.csv` files into Tableau Public to create visualizations for DAU, Cohort Retention, and Revenue Trends.
