# models/restaurant.py

import sqlite3
from models.init import cursor, conn
from models.reviews import Review

class Restaurant:

    all = []

    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price
        self.__class__.all.append(self)

    def reviews(self):
        cursor.execute("SELECT * FROM reviews WHERE restaurant_id = ?", (self.id,))
        results = cursor.fetchall()
        reviews = []
        for result in results:
            review_id, customer_id, _, star_rating = result
            reviews.append(Review(review_id, customer_id, self.id, star_rating))
        return reviews

    def customers(self):
        from models.customer import Customer
        cursor.execute("SELECT DISTINCT customer_id FROM reviews WHERE restaurant_id = ?", (self.id,))
        results = cursor.fetchall()
        customers = []
        for result in results:
            customer_id = result[0]
            customer = Customer.get_by_id(customer_id)
            customers.append(customer)
        return customers

    @classmethod
    def fanciest(cls):
        cursor.execute("SELECT * FROM restaurants ORDER BY price DESC LIMIT 1")
        result = cursor.fetchone()
        if result:
            id, name, price = result
            return cls(id, name, price)
        else:
            return None

    def all_reviews(self):
        from models.customer import Customer

        cursor.execute("SELECT * FROM reviews WHERE restaurant_id = ?", (self.id,))
        results = cursor.fetchall()
        reviews = []
        for result in results:
            review_id, customer_id, _, star_rating = result
            customer = Customer.get_by_id(customer_id)
            reviews.append(f"Review for {self.name} by {customer.full_name()}: {star_rating} stars.")
        return reviews

    @classmethod
    def create_table(cls):
        cursor.execute('''CREATE TABLE IF NOT EXISTS restaurants(
                       id INTEGER PRIMARY KEY,
                       name TEXT,
                       price INTEGER)''')
        conn.commit()

    @classmethod
    def get_by_id(cls, restaurant_id):
        cursor.execute("SELECT * FROM restaurants WHERE id = ?", (restaurant_id,))
        result = cursor.fetchone()
        if result:
            id, name, price = result
            return cls(id, name, price)
        else:
            return None

    @staticmethod
    def add_restaurant(name, price):
        try:
            cursor.execute("INSERT INTO restaurants (name, price) VALUES (?, ?)", (name, price))
            conn.commit()
            print("Restaurant Added Successfully")
        except sqlite3.IntegrityError:
            print("Error: Restaurant already exists!")

    @staticmethod
    def exists(name, price):
        cursor.execute("SELECT COUNT(*) FROM restaurants WHERE name = ? AND price = ?", (name, price))
        count = cursor.fetchone()[0]
        return count > 0