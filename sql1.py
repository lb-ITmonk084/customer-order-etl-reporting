import pyodbc

try:
    # Connect using Windows Authentication
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=ITMONK\SQLSERVERLB;'  # e.g., 'localhost\\SQLEXPRESS'
        'DATABASE=ORDER;'
        'Trusted_Connection=yes;'
    )

    cursor = conn.cursor()

    # Create table if it doesn't exist
    cursor.execute("""
    IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='customers' AND xtype='U')
    CREATE TABLE customers (
        id INT IDENTITY(1,1) PRIMARY KEY,
        name NVARCHAR(100),
        email NVARCHAR(100)
    )
    """)

    # Insert single record
    cursor.execute("""
    INSERT INTO customers (name, email)
    VALUES (?, ?)
    """, ("Leela", "leela@example.com"))

    # Insert multiple records
    data = [
        ("Ravi", "ravi@example.com"),
        ("Anita", "anita@example.com"),
        ("Kiran", "kiran@example.com")
    ]

    cursor.executemany("""
    INSERT INTO customers (name, email)
    VALUES (?, ?)
    """, data)

    # Commit changes
    conn.commit()
    print("Data inserted successfully!")

except Exception as e:
    print(f"Error: {e}")

finally:
    if 'conn' in locals():
        conn.close()