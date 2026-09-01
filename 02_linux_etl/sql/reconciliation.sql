-- Source-to-target reconciliation examples

-- Row-count validation
SELECT COUNT(*) AS source_count
FROM source_schema.orders;

SELECT COUNT(*) AS target_count
FROM curated_schema.orders;

-- Latest processed date
SELECT MAX(order_date) AS source_max_date
FROM source_schema.orders;

SELECT MAX(order_date) AS target_max_date
FROM curated_schema.orders;

-- Duplicate business keys
SELECT
    order_id,
    COUNT(*) AS record_count
FROM curated_schema.orders
GROUP BY order_id
HAVING COUNT(*) > 1;
