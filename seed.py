#!/usr/bin/env python3
# seed.py

from models.init import conn, cursor
from models.restaurant import Restaurant
from models.customer import Customer
from models.reviews import Review

def seed_db():
    Customer.create_table()
    Restaurant.create_table()
    Review.create_table()

    cursor.execute("SELECT id, first_name, last_name FROM customers")
    existing_customers = cursor.fetchall()
    for customer_data in existing_customers:
        customer_instance = Customer(*customer_data)
        Customer.all.append(customer_instance)

    customers_to_add = [
        ("Will", "Smith"),
        ("Peter", "Parker"),
        ("Tony", "Stark")
    ]
    for first_name, last_name in customers_to_add:
        if not any(customer.first_name == first_name and customer.last_name == last_name for customer in Customer.all):
            customer_id = Customer.add_customer(first_name, last_name)
            customer_instance = Customer.get_by_id(customer_id)
            if customer_instance:
                Customer.all.append(customer_instance)
                
    restaurants_to_add = [
        ("Art Cafe", 200),
        ("Pepinos Pizza", 500),
        ("Galitos Restaurant", 1000)
    ]
    for restaurant_data in restaurants_to_add:
        name, price = restaurant_data
        if not Restaurant.exists(name, price):
            Restaurant.add_restaurant(name, price)
    
    reviews_to_add = [
        (1, 1, 4),
        (2, 2, 5),
        (3, 3, 3)
    ]
    for review_data in reviews_to_add:
        customer_id, restaurant_id, star_rating = review_data
        customer = Customer.get_by_id(customer_id)  # Retrieve Customer object
        if customer:
            customer.add_review(Restaurant.get_by_id(restaurant_id), star_rating)  # Pass Customer object


    print("Database successfully seeded")


if __name__ == "__main__":
    seed_db()
