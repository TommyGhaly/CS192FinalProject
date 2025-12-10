"""
demo.py
A simple demonstration of the shopping system.
Shows how products are created, added to the product manager,
added to a cart, turned into an order, and paid for.
"""

from Users.admin import Admin
from Users.user import User
from Products.productManagement import ProductManagement
from Products.books import Books
from Products.clothes import Clothes
from Shopping.Carts.cart import Cart
from Shopping.Orders.orderService import OrderService
from Shopping.Payments.credit_card import CreditCardPayment


def main():
    print("\n=== SIMPLE DEMO START ===\n")

    # --- Create users ---
    admin = Admin("A1", "admin", "admin@example.com", "password123")
    customer = User("U1", "john", "john@example.com", "pass123")

    print("Admin created:", admin.username)
    print("Customer created:", customer.username)

    # --- Create a product manager and add products ---
    pm = ProductManagement()

    book = Books("B1", "Intro to Python", 29.99, "Sarah Smith", 300)
    shirt = Clothes("C1", "Black T-Shirt", 15.99, "L", "Cotton")

    pm.add_product(book)
    pm.add_product(shirt)

    print("\nProducts added:")
    print(book)
    print(shirt)

    # --- Customer builds a cart ---
    cart = Cart(customer.user_id)
    cart.add_item("B1", 1)
    cart.add_item("C1", 2)

    print("\nCart items:", cart.get_items())

    # --- Create an order from the cart ---
    order = OrderService.create_order(
        customer_id=customer.user_id,
        items=cart.get_items(),
        products=[book, shirt]
    )

    print("\nOrder created:")
    print(order)

    # --- Process a credit card payment ---
    payment = CreditCardPayment(
        amount=order.total_price,
        card_number="4242 4242 4242 4242",
        expiry="12/30",
        cvv="123"
    )

    print("\nProcessing payment...")
    success = payment.process_payment(
        order.total_price,
        payment_info={"card_number": payment.card_number}
    )

    print("Payment success:", success)

    print("\n=== SIMPLE DEMO END ===\n")


if __name__ == "__main__":
    main()
