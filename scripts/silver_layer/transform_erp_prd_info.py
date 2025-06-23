import pandas as pd
import mysql.connector

# DB Connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ayush007",
    database="data_warehouse"
)
cursor = conn.cursor()

# Read data from Bronze layer
df = pd.read_sql("SELECT * FROM bronze_erp_pz_cat_g1v2", conn)

# Drop rows missing critical fields
df = df.dropna(subset=["id", "cat"])

# Optional: clean text fields
df['id'] = df['id'].str.strip()
df['cat'] = df['cat'].str.strip()
df['subcat'] = df['subcat'].str.strip()
df['maintenance'] = df['maintenance'].str.strip()

# Insert into Silver layer
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO silver_erp_products (
            product_id, category, sub_category, maintenance_flag
        ) VALUES (%s, %s, %s, %s)
    """, (
        row['id'], row['cat'], row['subcat'], row['maintenance']
    ))

conn.commit()
print("ERP Products data inserted into Silver Layer.")
cursor.close()
conn.close()
