# models/reviews.py

from models.init import cursor, conn

class Review:

    all =[]

    def __init__(self, id, customer_id, restaurant_id, star_rating):
        self.id = id
        self.customer_id = customer_id
        self.restaurant_id = restaurant_id
        self.star_rating = star_rating
        self.__class__.all.append(self)

    def customer(self):
        from models.customer import Customer
        return Customer.get_by_id(self.customer_id)

    def restaurant(self):
        from models.restaurant import Restaurant
        return Restaurant.get_by_id(self.restaurant_id)

    def full_review(self):
        customer = self.customer()
        restaurant = self.restaurant()
        return f"Review for {restaurant.name} by {customer.full_name()}: {self.star_rating} stars."

    @classmethod
    def create_table(cls):
        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS reviews(
                       id INTEGER PRIMARY KEY,
                       customer_id INTEGER,
                       restaurant_id INTEGER,
                       star_rating INTEGER,
                       FOREIGN KEY (restaurant_id) REFERENCES restaurants(id),
                       FOREIGN KEY (customer_id) REFERENCES customers(id)
                       )''')
        conn.commit()

    @staticmethod
    def exists(customer_id, restaurant_id):
        cursor.execute("SELECT COUNT(*) FROM reviews WHERE customer_id = ? AND restaurant_id = ?", (customer_id, restaurant_id))
        count = cursor.fetchone()[0]
        return count > 0