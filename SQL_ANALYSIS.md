# SQL Analysis Queries

## 1. Daily Active Users (DAU)
```sql
SELECT 
    transaction_date AS date,
    COUNT(DISTINCT user_id) AS dau
FROM 
    transactions
GROUP BY 
    transaction_date
ORDER BY 
    transaction_date;
```
- Tracks unique users per day
- Used to measure engagement trends

## 2. Retention Cohort
```sql
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
```
- Cohort retention by signup date
- Identifies user lifecycle patterns

## 3. Revenue Trend
```sql
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
```
- Revenue aggregated by week
- Shows monetization trajectory
