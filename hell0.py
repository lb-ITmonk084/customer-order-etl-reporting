import pandas as pd

try:
    df = pd.read_csv(r"C:\Users\leela\OneDrive\Desktop\customer-order-etl-reporting\pizza_sales.csv")
    print(df.head())
except Exception as e:
    print("Error:", e)