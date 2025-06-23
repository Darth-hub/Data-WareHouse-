import pandas as pd
import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ayush007",
    database="data_warehouse"
)

cursor = conn.cursor()
df = pd.read_csv("datasets/source_crm/sales_details.csv")
for index, row in df.iterrows():
    print(f"Inserting row {index + 1}")
    cursor.execute("""
        INSERT INTO bronze_crm_sales_details (
            sls_ord_num, sls_prd_key, sls_cust_id,
            sls_order_dt, sls_ship_dt, sls_due_dt,
            sls_sales, sls_quantity, sls_price
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        row['sls_ord_num'],
        row['sls_prd_key'],
        row['sls_cust_id'],
        row['sls_order_dt'],
        row['sls_ship_dt'],
        row['sls_due_dt'],
        row['sls_sales'],
        row['sls_quantity'],
        row['sls_price']
    ))

conn.commit()
print("Data inserted successfully.")
cursor.close()
conn.close()
