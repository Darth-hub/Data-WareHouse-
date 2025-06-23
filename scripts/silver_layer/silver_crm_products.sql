CREATE TABLE IF NOT EXISTS silver_crm_products (
    prd_id INT PRIMARY KEY,
    prd_key VARCHAR(50),
    product_name VARCHAR(100),
    product_cost INT,
    product_line VARCHAR(100),
    start_date DATETIME,
    end_date DATETIME
);
