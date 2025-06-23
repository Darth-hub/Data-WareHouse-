CREATE DATABASE IF NOT EXISTS data_warehouse;
USE data_warehouse;

-- BRONZE Layer Tables

-- 1. CRM Customer Info
CREATE TABLE IF NOT EXISTS bronze_crm_cust_info (
    cst_id INT,
    cst_key VARCHAR(50),
    cst_firstname VARCHAR(50),
    cst_lastname VARCHAR(50),
    cst_material_status VARCHAR(50),
    cst_gndr VARCHAR(50),
    cst_create_date DATE
);

-- 2. CRM Product Info
CREATE TABLE IF NOT EXISTS bronze_crm_prd_info (
    prd_id INT,
    prd_key VARCHAR(50),
    prd_nm VARCHAR(50),
    prd_cost INT,
    prd_line VARCHAR(50),
    prd_start_dt DATETIME,
    prd_end_dt DATETIME
);

-- 3. CRM Sales Details
CREATE TABLE IF NOT EXISTS bronze_crm_sales_details (
    sls_ord_num VARCHAR(50),
    sls_prd_key VARCHAR(50),
    sls_cust_id INT,
    sls_order_dt DATE,
    sls_ship_dt DATE,
    sls_due_dt DATE,
    sls_sales INT,
    sls_quantity INT,
    sls_price INT
);

-- 4. ERP Location (A101)
CREATE TABLE IF NOT EXISTS bronze_erp_loc_a101 (
    cid VARCHAR(50),
    cntry VARCHAR(50)
);

-- 5. ERP Customer (AZ12)
CREATE TABLE IF NOT EXISTS bronze_erp_cust_az12 (
    cid VARCHAR(50),
    bdate DATE,
    gen VARCHAR(50)
);

-- 6. ERP Product Category (G1V2)
CREATE TABLE IF NOT EXISTS bronze_erp_pz_cat_g1v2 (
    id VARCHAR(50),
    cat VARCHAR(50),
    subcat VARCHAR(50),
    maintenance VARCHAR(50)
);
