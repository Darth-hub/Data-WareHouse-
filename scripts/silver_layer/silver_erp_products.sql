CREATE TABLE IF NOT EXISTS silver_erp_products (
    product_id VARCHAR(50) PRIMARY KEY,
    product_name VARCHAR(100),
    product_category VARCHAR(50),
    product_price INT,
    launch_date DATE
);
