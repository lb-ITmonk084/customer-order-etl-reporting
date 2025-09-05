import numpy as np
import pandas as pd
import pyodbc

# load csv file 

csv_path = r"C:\Users\leela\OneDrive\Desktop\customer-order-etl-reporting\pizza_sales.csv"
df = pd.read_csv(csv_path)


# Replace NaNs with None (SQL-compatible)
df = df.replace({np.nan: None})

# connect to sql server 

conn = pyodbc.connect(
    'driver={odbc driver 17 for sql server};' \
    'server=ITMONK\SQLSERVERLB;' \
    'database=ORDER;' \
    'trusted_connection=yes;'

)
cursor = conn.cursor()

# create table if not exits 
cursor.execute("""
IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='pizza_sales' AND xtype='U')
CREATE TABLE pizza_sales (
                pizza_id INT,
                order_id INT,
                pizza_name NVARCHAR(100),
                quantity INT,
                order_date varchar(50),
                order_time varchar(50),
                unit_price DECIMAL(10, 2),
                total_price DECIMAL(10, 2),
                pizza_size NVARCHAR(50),
                pizza_category NVARCHAR(100),
                pizza_ingredients NVARCHAR(255)                
                )
""")
query = "INSERT INTO pizza_sales (pizza_id, order_id, pizza_name, quantity, order_date, order_time, unit_price, total_price, pizza_size, pizza_category, pizza_ingredients) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"

data = [tuple(x) for x in df.to_numpy()]

cursor.executemany(query, data)
conn.commit()
conn.close()
print("Data inserted successfully!")    
# insert data row by row

# for index, row in df.iterrows():
#     try:
#         cursor.executemany("""
#         INSERT INTO pizza_sales (pizza_id, order_id, pizza_name, order_date, order_time, unit_price, total_price, pizza_size, pizza_category, pizza_ingredients)
#         VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
#         """, row.pizza_id, row.order_id, row.pizza_name, row.order_date, row.order_time, row.unit_price, row.total_price, row.pizza_size, row.pizza_category, row.pizza_ingredients)
#         conn.commit()
#     except Exception as e:
#         print(f"Error at row {index}: {e}")

# conn.close()
# print("Data insertion complete!")

