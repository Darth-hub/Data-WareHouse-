import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ayush007",
    database="data_warehouse"
)
cursor = conn.cursor()

df = pd.read_sql("SELECT * FROM bronze_crm_prd_info", conn)
df = df.dropna(subset=["prd_id", "prd_key"])

# Convert to datetime safely
df['prd_start_dt'] = pd.to_datetime(df['prd_start_dt'], errors='coerce')
df['prd_end_dt'] = pd.to_datetime(df['prd_end_dt'], errors='coerce')

df['prd_start_dt'] = df['prd_start_dt'].dt.strftime('%Y-%m-%d %H:%M:%S')
df['prd_end_dt'] = df['prd_end_dt'].dt.strftime('%Y-%m-%d %H:%M:%S')

for index, row in df.iterrows():
    cursor.execute("""
        INSERT INTO silver_crm_products (
            prd_id, prd_key, product_name, product_cost,
            product_line, start_date, end_date
        ) VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (
        int(row['prd_id']),
        row['prd_key'],
        row['prd_nm'],
        int(row['prd_cost']) if pd.notnull(row['prd_cost']) else None,
        row['prd_line'],
        row['prd_start_dt'] if pd.notnull(row['prd_start_dt']) else None,
        row['prd_end_dt'] if pd.notnull(row['prd_end_dt']) else None
    ))

conn.commit()
print("✅ Products data inserted into Silver Layer.")
cursor.close()
conn.close()
