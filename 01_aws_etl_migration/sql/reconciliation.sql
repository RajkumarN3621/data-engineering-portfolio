-- Source-to-target reconciliation examples

SELECT COUNT(*) AS source_count
FROM source_schema.source_table;

SELECT COUNT(*) AS target_count
FROM curated_schema.target_table;

SELECT MAX(load_date) AS source_max_date
FROM source_schema.source_table;

SELECT MAX(load_date) AS target_max_date
FROM curated_schema.target_table;

SELECT customer_id, order_date, COUNT(*) AS record_count
FROM curated_schema.target_table
GROUP BY customer_id, order_date
HAVING COUNT(*) > 1;
