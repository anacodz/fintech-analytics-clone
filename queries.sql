-- 1. Daily Active Users (DAU)
-- Counts the number of unique users making a transaction on each day
SELECT 
    transaction_date AS date,
    COUNT(DISTINCT user_id) AS dau
FROM 
    transactions
GROUP BY 
    transaction_date
ORDER BY 
    transaction_date;

-- 2. Retention Cohort
-- Tracks how many users from a specific sign-up month return to make transactions in subsequent months
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
        -- Calculate difference in months between cohort month and activity month
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
    month_number >= 0 -- Exclude activities that somehow happen before signup month (should be 0)
GROUP BY 
    cohort_month,
    month_number
ORDER BY 
    cohort_month,
    month_number;

-- 3. Revenue Trend
-- Calculates daily revenue generated from transactions
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
