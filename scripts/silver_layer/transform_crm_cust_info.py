import pandas as pd
import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ayush007",
    database="data_warehouse"
)
cursor = conn.cursor()
df = pd.read_sql("SELECT * FROM bronze_crm_cust_info", conn)

df = df.dropna(subset=["cst_id", "cst_key"])
df['cst_gndr'] = df['cst_gndr'].str.strip().str[0].str.upper()
df = df.drop_duplicates(subset=["cst_id"])

for index, row in df.iterrows():
    cursor.execute("""
    INSERT IGNORE INTO silver_crm_customers (
        cst_id, cst_key, first_name, last_name, marital_status, gender, created_date
    ) VALUES (%s, %s, %s, %s, %s, %s, %s)
""", (
    row['cst_id'],
    row['cst_key'],
    row['cst_firstname'],
    row['cst_lastname'],
    row['cst_material_status'],
    row['cst_gndr'],
    row['cst_create_date']
))


conn.commit()
print("Data inserted into Silver Layer successfully.")
cursor.close()
conn.close()
