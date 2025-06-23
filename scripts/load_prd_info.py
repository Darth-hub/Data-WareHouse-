import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ayush007", 
    database="data_warehouse"
)

cursor = conn.cursor()
df = pd.read_csv("datasets/source_crm/prd_info.csv")
for index, row in df.iterrows():
    print(f"Inserting row {index + 1}")
    cursor.execute("""
        INSERT INTO bronze_crm_prd_info (
            prd_id, prd_key, prd_nm, prd_cost,
            prd_line, prd_start_dt, prd_end_dt
        ) VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (
        row['prd_id'],
        row['prd_key'],
        row['prd_nm'],
        row['prd_cost'],
        row['prd_line'],
        row['prd_start_dt'],
        row['prd_end_dt']
    ))

conn.commit()
print("Data inserted successfully.")
cursor.close()
conn.close()
