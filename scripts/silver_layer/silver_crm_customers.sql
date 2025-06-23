CREATE TABLE IF NOT EXISTS silver_crm_customers (
    cst_id INT PRIMARY KEY,
    cst_key VARCHAR(50),
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    marital_status VARCHAR(50),
    gender CHAR(1),
    created_date DATE
);
