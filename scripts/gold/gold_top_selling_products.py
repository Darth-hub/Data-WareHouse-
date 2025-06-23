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


prd_df = pd.read_sql("SELECT * FROM silver_erp_products", conn)
sales_df = pd.read_sql("SELECT * FROM silver_erp_sales_details", conn)

sales_df.rename(columns={"sls_prd_key": "product_id"}, inplace=True)
merged_df = pd.merge(prd_df, sales_df, on="product_id", how="inner")

summary_df = merged_df.groupby(['product_id', 'category']).agg(
    total_sales_amount=pd.NamedAgg(column='sls_price', aggfunc='sum'),
    total_quantity_sold=pd.NamedAgg(column='sls_quantity', aggfunc='sum')
).reset_index()

# Create gold table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS gold_top_selling_products (
        product_id VARCHAR(50),
        product_name VARCHAR(255),
        total_sales_amount INT,
        total_quantity_sold INT
    )
""")
conn.commit()

# Insert into gold layer
for _, row in summary_df.iterrows():
    try:
        cursor.execute("""
            INSERT INTO gold_top_selling_products (
                product_id, product_name, total_sales_amount, total_quantity_sold
            ) VALUES (%s, %s, %s, %s)
        """, (
            row['product_id'],
            row['category'],  # if you're using `category` as product_name
            int(row['total_sales_amount']),
            int(row['total_quantity_sold'])
        ))
    except Exception as e:

conn.commit()
cursor.close()
conn.close()
