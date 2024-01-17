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

-- Task 8:
SELECT SUM(total_sales) AS total_sales, store_type, country_code
FROM sales
WHERE country_code ='DE'
GROUP BY store_type, country_code
ORDER BY total_sales DESC;

-- Task 9:
SELECT
    EXTRACT(YEAR FROM sale_time) AS year,
    AVG(EXTRACT(EPOCH FROM (LEAD(sale_time) OVER(PARTITION BY EXTRACT(YEAR FROM sale_time) ORDER BY sale_time) - sale_time))) AS actual_time_taken
FROM sales
GROUP BY year
ORDER BY year;    
