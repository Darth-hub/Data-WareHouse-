CREATE TABLE IF NOT EXISTS silver_crm_sales (
    sales_order_num VARCHAR(50),
    product_key VARCHAR(50),
    customer_id INT,
    order_date DATE,
    ship_date DATE,
    due_date DATE,
    sales_amount INT,
    quantity INT,
    unit_price INT
);
