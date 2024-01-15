-- Task 1:
SELECT country, COUNT(store_id) AS total_no_stores
FROM stores
GROUP BY country
ORDER BY total_no_stores DESC;