# SQL Data Warehouse + REST API

An end-to-end Data Warehouse system built from scratch using **Python**, **MySQL**, and **Node.js**. Implements the **Medallion Architecture** (Bronze → Silver → Gold) for clean, layered data transformation and reporting. Exposes analytics-ready insights via REST APIs for real-time consumption.

## 🚀 Features

* ✅ **Bronze Layer**: Raw CRM & ERP data ingestion using Pandas & MySQL.
* ✅ **Silver Layer**: Cleaned and transformed tables (e.g., `silver_crm_customers`, `silver_erp_sales_details`).
* ✅ **Gold Layer**: Aggregated reports like:

  * Customer sales summary
  * Top-selling products
  * Monthly sales trends
* ✅ **REST API**: Node.js + Express backend to serve real-time analytics data.

## 🛠️ Tech Stack

* **Languages**: Python, SQL, JavaScript (Node.js)
* **Databases**: MySQL
* **Libraries**: Pandas, MySQL Connector, SQLAlchemy
* **API Framework**: Express.js
* **Architecture**: Medallion (Bronze → Silver → Gold)

## 📊 Sample Outputs

* `gold_customer_sales_summary.csv`
* `gold_top_selling_products.csv`
* `gold_monthly_sales_trends.csv`

> All reports are available as CSVs and accessible through the API server.

## 📂 Folder Structure

```
sql-data-warehouse-project/
├── bronze_ingest.py
├── silver_transform.py
├── gold_customer_sales_summary.py
├── gold_top_selling_products.py
├── gold_monthly_sales_trends.py
├── dw-api-server/
│   ├── index.js
│   └── .env
```

## 🧪 How to Run

1. **Clone the repo**

   ```bash
   git clone https://github.com/Darth-hub/sql-data-warehouse-project
   ```

2. **Set up MySQL**
   Create a database named `data_warehouse` and set credentials in `.env`.

3. **Run ETL Scripts**

   ```bash
   python bronze_ingest.py
   python silver_transform.py
   python gold_customer_sales_summary.py
   ```

4. **Start API Server**

   ```bash
   cd dw-api-server
   node index.js
   ```

5. **Access Reports**
   Open `http://localhost:3000/customer-sales` or other endpoints.

## 🔗 Related Links

* [Medallion Architecture – Databricks](https://www.databricks.com/glossary/medallion-architecture)

