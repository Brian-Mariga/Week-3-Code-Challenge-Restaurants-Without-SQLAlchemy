# models/init.py

import sqlite3

conn = sqlite3.connect('restaurant.db')
cursor = conn.cursor()