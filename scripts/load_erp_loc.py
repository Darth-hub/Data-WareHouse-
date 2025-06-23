import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ayush007",
    database="data_warehouse"
)
cursor = conn.cursor()

df = pd.read_csv("datasets/source_erp/LOC_A101.csv")

for index, row in df.iterrows():
    print(f"Inserting row {index + 1}")
    cursor.execute("""
        INSERT INTO bronze_erp_loc_a101 (
            cid, cntry
        ) VALUES (%s, %s)
    """, (
        row['CID'],
        row['CNTRY']
    ))

conn.commit()
print("Data inserted successfully.")
cursor.close()
conn.close()
