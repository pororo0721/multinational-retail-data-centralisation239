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

-- Task 4:
SELECT COUNT(*) as numbers_of_sales, SUM(product_quantity) as product_quantity_count, location
FROM sales
GROUP BY location;

-- Task 5:

SELECT
    store_type,
    SUM(sales) as total_sales,
    (SUM(sales) / (SELECT SUM(sales) FROM sales)) * 100 as percentage_total
FROM sales
GROUP BY store_type;  

-- Task 6:

SELECT
    SUM(sales) as total_sales,
    YEAR(sales_date) as year,
    MONTH(sales_date) as month,
FROM sales
GROUP BY year, month
ORDER BY total_sales DESC;    

-- Task 7:
SELECT COUNT(staff_id) AS total_staff_numbers, country_code
FROM staff_id
GROUP BY country_code;