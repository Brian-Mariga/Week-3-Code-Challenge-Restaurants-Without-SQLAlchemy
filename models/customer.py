# models/customer.py

import sqlite3
from models.init import cursor, conn
from models.restaurant import Restaurant
from models.reviews import Review

class Customer:
    all = []

    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.__class__.all.append(self)

    def __str__(self):
        return f"ID: {self.id}, Name: {self.first_name} {self.last_name}"
        
    def reviews(self):
        cursor.execute("SELECT * FROM reviews WHERE customer_id = ?", (self.id,))
        results = cursor.fetchall()
        reviews = []
        for result in results:
            review_id, _, restaurant_id, star_rating = result
            restaurant = Restaurant.get_by_id(restaurant_id)
            reviews.append(Review(review_id, self.id, restaurant_id, star_rating))
        return reviews
    
    def restaurants(self):
        cursor.execute("SELECT DISTINCT restaurant_id FROM reviews WHERE customer_id = ?", (self.id,))
        results = cursor.fetchall()
        restaurants = []
        for result in results:
            restaurant_id = result[0]
            restaurant = Restaurant.get_by_id(restaurant_id)
            restaurants.append(restaurant)
        return restaurants
    
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def favorite_restaurant(self):
        cursor.execute('''
                       SELECT restaurant_id FROM reviews
                       WHERE customer_id = ?
                       ORDER BY star_rating DESC
                       LIMIT 1
                       ''', (self.id,))
        result = cursor.fetchone()
        if result:
            restaurant_id = result[0]
            return Restaurant.get_by_id(restaurant_id)
        else:
            return None

    def add_review(self, restaurant, rating):
        cursor.execute("""INSERT INTO reviews 
                       (restaurant_id, customer_id, star_rating)
                       VALUES (?, ?, ?)""",(restaurant.id, self.id, rating))
        conn.commit()

    def delete_reviews(self, restaurant):
        cursor.execute('''DELETE FROM reviews WHERE restaurant_id = ? AND customer_id = ?''',
                       (restaurant.id, self.id))
        conn.commit()

    @classmethod
    def create_table(cls):
        cursor.execute('''CREATE TABLE IF NOT EXISTS customers(
                       id INTEGER PRIMARY KEY,
                       first_name TEXT,
                       last_name TEXT)''')
        conn.commit()

    @staticmethod
    def get_by_id(customer_id):
        for customer in Customer.all:
            if customer.id == customer_id:
                return customer
        return None

    @staticmethod
    def add_customer(first_name, last_name):
        if not first_name or not last_name:
            print("Error: First Name and Last Name are required!")
            return None

        cursor.execute("SELECT id FROM customers WHERE first_name = ? AND last_name = ?", (first_name, last_name))
        existing_customer = cursor.fetchone()
        if existing_customer:
            print(f"Customer {first_name} {last_name} already exists with ID: {existing_customer[0]}")

        try:
            cursor.execute("INSERT INTO customers (first_name, last_name) VALUES (?, ?)", (first_name, last_name))
            conn.commit()
            new_customer_id = cursor.lastrowid
            print("Customer Added Successfully")
            customer_instance = Customer.get_by_id(new_customer_id)
            if customer_instance:
                Customer.all.append(customer_instance)
        except sqlite3.IntegrityError:
            print(f"Error: Customer {first_name} {last_name} already exists!")
