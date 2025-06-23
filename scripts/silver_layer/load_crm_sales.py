import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ayush007",
    database="data_warehouse"
)
cursor = conn.cursor()
cursor.execute("TRUNCATE TABLE silver_crm_sales")
df = pd.read_sql("SELECT * FROM bronze_crm_sales_details", conn)
df = df.dropna(subset=["sls_ord_num", "sls_prd_key", "sls_cust_id", "sls_sales"])
for col in ['sls_order_dt', 'sls_ship_dt', 'sls_due_dt']:
    df[col] = pd.to_datetime(df[col], errors='coerce')
    df[col] = df[col].dt.strftime('%Y-%m-%d %H:%M:%S')

for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO silver_crm_sales (
            sales_order_num, product_key, customer_id,
            order_date, ship_date, due_date,
            sales_amount, quantity, unit_price
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        row['sls_ord_num'], row['sls_prd_key'], row['sls_cust_id'],
        row['sls_order_dt'], row['sls_ship_dt'], row['sls_due_dt'],
        int(row['sls_sales']) if not pd.isna(row['sls_sales']) else 0,
        int(row['sls_quantity']) if not pd.isna(row['sls_quantity']) else 0,
        int(row['sls_price']) if not pd.isna(row['sls_price']) else 0,
    ))

conn.commit()
print("Sales data inserted into Silver Layer.")
cursor.close()
conn.close()
