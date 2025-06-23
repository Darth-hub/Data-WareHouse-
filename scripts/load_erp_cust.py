import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ayush007",  
    database="data_warehouse"
)

cursor = conn.cursor()
df = pd.read_csv("datasets/source_erp/CUST_AZ12.csv")

for index, row in df.iterrows():
    print(f"Inserting row {index+1}")
    cursor.execute("""
        INSERT INTO bronze_erp_cust_az12 (
            cid, bdate, gen
        ) VALUES (%s, %s, %s)
    """, (
        row['CID'],
        row['BDATE'],
        row['GEN']
    ))

conn.commit()
print("Data inserted successfully.")
cursor.close()
conn.close()
