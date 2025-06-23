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

# Read CRM and ERP Sales Data
crm_df = pd.read_sql("SELECT * FROM silver_crm_customers", conn)
erp_sales_df = pd.read_sql("SELECT * FROM silver_erp_sales_details", conn)
crm_df.rename(columns={"cst_id": "customer_id", "first_name": "cst_name"}, inplace=True)
erp_sales_df.rename(columns={"sls_cust_id": "customer_id"}, inplace=True)
merged_df = pd.merge(crm_df, erp_sales_df, on="customer_id", how="inner")
summary_df = merged_df.groupby(['customer_id', 'cst_name']).agg(
    total_sales=pd.NamedAgg(column='sls_price', aggfunc='sum'),
    total_quantity=pd.NamedAgg(column='sls_quantity', aggfunc='sum')
).reset_index()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS gold_customer_sales_summary (
        customer_id INT,
        customer_name VARCHAR(255),
        total_sales INT,
        total_quantity INT
    )
""")
conn.commit()
for _, row in summary_df.iterrows():
    try:
        cursor.execute("""
            INSERT INTO gold_customer_sales_summary (
                customer_id, customer_name, total_sales, total_quantity
            ) VALUES (%s, %s, %s, %s)
        """, (
            int(row['customer_id']),
            row['cst_name'],
            int(row['total_sales']),
            int(row['total_quantity'])
        ))
    except Exception as e:
        print(f"Failed to insert row: {row}, due to error: {e}")

conn.commit()


cursor.close()
conn.close()
