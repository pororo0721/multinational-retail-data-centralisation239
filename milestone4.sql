-- Task 1:
SELECT country, COUNT(store_id) AS total_no_stores
FROM stores
GROUP BY country
ORDER BY total_no_stores DESC;

-- Task 2:
SELECT locality, COUNT(*) as total_no_stores
FROM stores
GROUP BY locality
ORDER BY total_no_stores DESC;

-- Task 3:
SELECT SUM(sales) as total_no_stores, MONTH(sales_date) as month
FROM sales
GROUP BY month
ORDER BY total_sales DESC;