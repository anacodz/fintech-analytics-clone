import sqlite3
import csv

def export_queries_to_csv():
    conn = sqlite3.connect('fi_money_clone.db')
    cursor = conn.cursor()
    
    # 1. DAU
    dau_query = """
    SELECT 
        transaction_date AS date,
        COUNT(DISTINCT user_id) AS dau
    FROM 
        transactions
    GROUP BY 
        transaction_date
    ORDER BY 
        transaction_date;
    """
    cursor.execute(dau_query)
    with open('dau_data.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([i[0] for i in cursor.description])
        writer.writerows(cursor.fetchall())
    
    # 2. Retention Cohort
    retention_query = """
    WITH signup_cohort AS (
        SELECT 
            user_id,
            STRFTIME('%Y-%m', signup_date) AS cohort_month
        FROM 
            users
    ),
    transaction_month AS (
        SELECT 
            user_id,
            STRFTIME('%Y-%m', transaction_date) AS activity_month
        FROM 
            transactions
    ),
    cohort_activity AS (
        SELECT 
            s.user_id,
            s.cohort_month,
            t.activity_month,
            CAST(SUBSTR(t.activity_month, 1, 4) AS INTEGER) * 12 + CAST(SUBSTR(t.activity_month, 6, 2) AS INTEGER) - 
            (CAST(SUBSTR(s.cohort_month, 1, 4) AS INTEGER) * 12 + CAST(SUBSTR(s.cohort_month, 6, 2) AS INTEGER)) AS month_number
        FROM 
            signup_cohort s
        LEFT JOIN 
            transaction_month t ON s.user_id = t.user_id
    )
    SELECT 
        cohort_month,
        month_number,
        COUNT(DISTINCT user_id) AS active_users
    FROM 
        cohort_activity
    WHERE 
        month_number >= 0
    GROUP BY 
        cohort_month,
        month_number
    ORDER BY 
        cohort_month,
        month_number;
    """
    cursor.execute(retention_query)
    with open('retention_cohort_data.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([i[0] for i in cursor.description])
        writer.writerows(cursor.fetchall())
    
    # 3. Revenue Trend
    revenue_query = """
    SELECT 
        transaction_date AS date,
        SUM(revenue) AS daily_revenue,
        SUM(SUM(revenue)) OVER (ORDER BY transaction_date) as cumulative_revenue
    FROM 
        transactions
    GROUP BY 
        transaction_date
    ORDER BY 
        transaction_date;
    """
    cursor.execute(revenue_query)
    with open('revenue_trend_data.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([i[0] for i in cursor.description])
        writer.writerows(cursor.fetchall())
    
    conn.close()
    print("Queries executed and exported to CSV files successfully.")

if __name__ == '__main__':
    export_queries_to_csv()
