create database;
use database name;
SHOW TABLES;
SELECT COUNT(*) FROM cleaned_superstore;
SELECT 
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit
FROM cleaned_superstore;
SELECT 
    customer_name,
    SUM(sales) AS total_spent
FROM cleaned_superstore
GROUP BY customer_name
ORDER BY total_spent DESC
LIMIT 5;
SELECT 
    category,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit
FROM cleaned_superstore
GROUP BY category;
SELECT 
    year,
    month,
    SUM(sales) AS monthly_sales
FROM cleaned_superstore
GROUP BY year, month
ORDER BY year, month;
SELECT 
    region,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit
FROM cleaned_superstore
GROUP BY region
ORDER BY total_sales DESC;
SELECT 
    category,
    SUM(profit) AS total_profit
FROM cleaned_superstore
GROUP BY category
ORDER BY total_profit DESC;
SELECT 
    product_name,
    SUM(profit) AS total_profit
FROM cleaned_superstore
GROUP BY product_name
HAVING total_profit < 0
ORDER BY total_profit;
SELECT 
    region,
    SUM(sales) AS total_sales
FROM cleaned_superstore
GROUP BY region
ORDER BY total_sales DESC
LIMIT 3;
SELECT 
    region,
    AVG(delivery_days) AS avg_delivery_days
FROM cleaned_superstore
GROUP BY region
ORDER BY avg_delivery_days;
SELECT 
    customer_name,
    COUNT(order_id) AS total_orders
FROM cleaned_superstore
GROUP BY customer_name
ORDER BY total_orders DESC
LIMIT 5;
SELECT 
    category,
    AVG(profit_margin) AS avg_margin
FROM cleaned_superstore
GROUP BY category
ORDER BY avg_margin DESC;

