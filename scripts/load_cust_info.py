import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ayush007", 
    database="data_warehouse"
)

cursor = conn.cursor()

df = pd.read_csv("datasets/source_crm/cust_info.csv")
for index, row in df.iterrows():
    print(f"Inserting row {index + 1}")
    cursor.execute("""
        INSERT INTO bronze_crm_cust_info (
            cst_id, cst_key, cst_firstname, cst_lastname,
            cst_material_status, cst_gndr, cst_create_date
        ) VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (
        row['cst_id'],
        row['cst_key'],
        row['cst_firstname'],
        row['cst_lastname'],
        row['cst_marital_status'],
        row['cst_gndr'],
        row['cst_create_date']
    ))

conn.commit()
print("Data inserted successfully.")
cursor.close()
conn.close()



