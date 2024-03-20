# main.py

from models.customer import Customer
from models.reviews import Review
from models.restaurant import Restaurant
from seed import seed_db

def test_customer_methods():
    print("*******************************Testing Customer Methods*******************************")
  
    if Customer.all:
        customer_one = Customer.all[0]
        print(f"Customer's 1 Full Name: {customer_one.full_name()}")
    else:
        print("No customers found in the list.")

    favorite = customer_one.favorite_restaurant()
    if favorite:
        print(f"Favorite Restaurant: {favorite.name}")
    else:
        print("Favorite Restaurant: None")

    customer_one = Customer.all[0]
    review = customer_one.add_review(Restaurant.get_by_id(1), 5)


def test_restaurant_methods():
    restaurant_one = Restaurant.all[0].all_reviews()
    print("*******************************Testing Restaurant Class*******************************")
    print(restaurant_one)
    fanciest_restaurant = Restaurant.fanciest()
    print(f"Fanciest Restaurant: {fanciest_restaurant.name}")
    
    # Testing all_reviews method for a specific restaurant
    restaurant_two = Restaurant.all[0]
    reviews = restaurant_two.all_reviews()
    print(f"All Reviews for {restaurant_two.name}:")
    for review in reviews:
        print(review)
    print()

def test_review_methods():
    print("*******************************Testing Review Methods*******************************")
    review = Review(2, 1, 1, 5)
    print(review.full_review())

def main():
    # Seed the database
    seed_db()

    test_customer_methods()

    test_restaurant_methods()

    test_review_methods()

if __name__ == "__main__":
    main()
