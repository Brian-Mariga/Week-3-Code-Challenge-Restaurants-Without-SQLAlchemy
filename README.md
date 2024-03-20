# Week-3-Code-Challenge-Restaurants-Without-SQLAlchemy
## Introduction
This project implements a restaurant review system where customers can leave reviews for restaurants they have visited. The system consists of three main classes: Customer, Restaurant, and Review, each with various methods to interact with the database and perform operations related to customers, restaurants, and reviews.

## Database Schema
The database schema includes three tables: customers, restaurants, and reviews. Here's a brief overview of each table's structure:

1. customers Table
- id (INTEGER): Unique identifier for the customer.
- first_name (TEXT): First name of the customer.
- last_name (TEXT): Last name of the customer.
2. restaurants Table
- id (INTEGER): Unique identifier for the restaurant.
- name (TEXT): Name of the restaurant.
- price (INTEGER): Price level of the restaurant.
3. reviews Table
- id (INTEGER): Unique identifier for the review.
- customer_id (INTEGER): ID of the customer who left the review.
- restaurant_id (INTEGER): ID of the restaurant being reviewed.
- star_rating (INTEGER): Rating given by the customer (out of 5 stars).

## Object Relationship Methods
### Review
- customer(): Returns the Customer instance for this review.
- restaurant(): Returns the Restaurant instance for this review.
### Restaurant
- reviews(): Returns a collection of all the reviews for the restaurant.
- customers(): Returns a collection of all the customers who reviewed the restaurant.
### Customer
- reviews(): Returns a collection of all the reviews left by the customer.
- restaurants(): Returns a collection of all the restaurants reviewed by the customer.
## Aggregate and Relationship Methods
### Customer
- full_name(): Returns the full name of the customer, with the first name and last name concatenated.
- favorite_restaurant(): Returns the restaurant instance with the highest star rating from this customer.
- add_review(restaurant, rating): Adds a new review for the restaurant with the given rating.
- delete_reviews(restaurant): Removes all reviews left by the customer for the specified restaurant.
### Review
- full_review(): Returns a string formatted as "Review for {restaurant name} by {customer's full name}: {review star rating} stars."
### Restaurant
- fanciest(): Returns one restaurant instance for the restaurant with the highest price.
- all_reviews(): Returns a list of strings with all the reviews for the restaurant.
## Testing
Ensure to test all implemented methods to verify their correctness and functionality. Use the main.py script to create instances of all classes and execute the tests.
