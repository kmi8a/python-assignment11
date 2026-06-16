# Task 2: A Line Plot with Pandas

import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

DB_PATH = "../db/lesson.db"

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()
cursor.execute("PRAGMA foreign_keys = ON;")

df = pd.read_sql("""
                               SELECT orders.order_id, SUM(price * quantity) AS total_price FROM orders 
                               JOIN line_items
                               ON line_items.order_id = orders.order_id 
                               JOIN products 
                               ON line_items.product_id = products.product_id 
                               GROUP BY orders.order_id""", conn)


def cumulative(row):
   totals_above = df['total_price'][0:row.name+1]
   return totals_above.sum()

df['cumulative'] = df.apply(cumulative, axis=1)

# print(df.head())


revenue_orders_plot = df.plot(x="order_id", y="cumulative", kind="line", title="Cumulative Revenue vs Orders")

revenue_orders_plot.xaxis.set_major_locator(MultipleLocator(50))
revenue_orders_plot.xaxis.set_minor_locator(MultipleLocator(10))
revenue_orders_plot.grid(which='major', linestyle='-', linewidth='0.4', color='gray')
revenue_orders_plot.grid(which='minor', linestyle=':', linewidth='0.3', color='gray')
plt.show()