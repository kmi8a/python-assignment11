import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

DB_PATH = "db/lesson.db"

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()
cursor.execute("PRAGMA foreign_keys = ON;")

employee_results = pd.read_sql("""
                               SELECT last_name, SUM(price * quantity) AS revenue 
                               FROM employees e 
                               JOIN orders o 
                               ON e.employee_id = o.employee_id 
                               JOIN line_items l 
                               ON o.order_id = l.order_id 
                               JOIN products p 
                               ON l.product_id = p.product_id 
                               GROUP BY e.employee_id;""", conn)

# print(employee_results.head())


employee_results.plot(x="last_name", y="revenue", kind="bar", color="orange", title="Revenue per Employee")
plt.show()