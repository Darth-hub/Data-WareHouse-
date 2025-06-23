import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ayush007",
    database="data_warehouse"
)
cursor = conn.cursor()

df = pd.read_csv("datasets/source_erp/PX_CAT_G1V2.csv")

for index, row in df.iterrows():
    print(f"Inserting row {index + 1}")
    cursor.execute("""
        INSERT INTO bronze_erp_pz_cat_g1v2 (
            id, cat, subcat, maintenance
        ) VALUES (%s, %s, %s, %s)
    """, (
        row['ID'],
        row['CAT'],
        row['SUBCAT'],
        row['MAINTENANCE']
    ))

conn.commit()
print("Data inserted successfully.")
cursor.close()
conn.close()
