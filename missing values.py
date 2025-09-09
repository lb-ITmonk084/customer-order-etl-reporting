import pandas as pd

# Load the CSV file
df = pd.read_csv(r"C:\Users\leela\OneDrive\Desktop\customer-order-etl-reporting\pizza_sales.csv")
print(df.head())
# # Find duplicate rows based on 'order_id' and 'pizza_id'
df_duplicates = df[df.duplicated(subset=['order_id', 'pizza_id'], keep=False)]

# Print the duplicates
print("Duplicate Rows based on order_id and pizza_id:")
print(df_duplicates)

# Remove duplicate rows based on 'order_id' and 'pizza_id'
df_cleaned = df.drop_duplicates(subset=['order_id', 'pizza_id'], keep='first')  

df_cleaned.to_csv(r"C:\Users\leela\OneDrive\Desktop\customer-order-etl-reporting\pizza_sales_cleaned.csv", index=False)

print("Duplicates removed and cleaned file saved.")
print(df_cleaned)