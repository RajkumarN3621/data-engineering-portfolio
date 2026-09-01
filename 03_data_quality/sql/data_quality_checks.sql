-- Generic source-to-target data-quality checks

-- Row counts
SELECT COUNT(*) AS row_count
FROM source_schema.orders;

SELECT COUNT(*) AS row_count
FROM target_schema.orders;

-- Completeness
SELECT
    COUNT(*) AS total_rows,
    COUNT(customer_id) AS non_null_customer_id,
    COUNT(amount) AS non_null_amount
FROM target_schema.orders;

-- Distinct values
SELECT
    COUNT(DISTINCT customer_id) AS distinct_customers
FROM target_schema.orders;

-- Duplicate business keys
SELECT
    order_id,
    COUNT(*) AS record_count
FROM target_schema.orders
GROUP BY order_id
HAVING COUNT(*) > 1;

-- Numeric distribution
SELECT
    COUNT(amount) AS amount_count,
    MIN(amount) AS amount_min,
    MAX(amount) AS amount_max,
    AVG(amount) AS amount_mean,
    SUM(amount) AS amount_sum
FROM target_schema.orders;

-- Processing date range
SELECT
    MIN(order_date) AS min_order_date,
    MAX(order_date) AS max_order_date
FROM target_schema.orders;
