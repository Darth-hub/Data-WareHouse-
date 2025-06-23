import mysql.connector
import pandas as pd
from datetime import datetime

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ayush007",
    database="data_warehouse"
)

cursor = conn.cursor()

sales_df = pd.read_sql("SELECT * FROM silver_erp_sales_details", conn)
prd_df = pd.read_sql("SELECT * FROM silver_erp_products", conn)

# Merge on product ID
merged_df = pd.merge(sales_df, prd_df, left_on='sls_prd_key', right_on='product_id', how='inner')

merged_df['month'] = pd.to_datetime(merged_df['sls_order_dt']).dt.to_period('M').astype(str)
merged_df['total_sale'] = merged_df['sls_quantity'] * merged_df['sls_price']

summary_df = merged_df.groupby(['month', 'category']).agg(
    total_sales=pd.NamedAgg(column='total_sale', aggfunc='sum')
).reset_index()


insert_query = """
    INSERT INTO gold_monthly_sales_trends (month, category, total_sales)
    VALUES (%s, %s, %s)
"""

for index, row in summary_df.iterrows():
    cursor.execute(insert_query, (
        row['month'],
        row['category'],
        round(row['total_sales'], 2)
    ))

conn.commit()
cursor.close()
conn.close()


