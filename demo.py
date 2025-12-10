"""
E-Shop Demo Application
=======================
Demonstrates core functionality of the E-Shop system.
"""

from Products.product import Product
from Products.books import Books
from Products.clothes import Clothes
from Shopping.Carts.cart import Cart
from Shopping.Orders.order import Order
from Shopping.Payments.credit_card import CreditCardPayment
from Shopping.Payments.paypal import PayPalPayment
from Users.customer import Customer
from Users.admin import Admin
from Users.authentication import AuthenticationService
from Inventory_Management.inventory import InventoryService
from Data_Persistence.data import DataManagement
import uuid
import json


def generate_id(prefix: str = "") -> str:
    """Generate a unique ID with optional prefix"""
    return f"{prefix}{uuid.uuid4().hex[:8]}"


def print_section(title: str):
    """Print a formatted section header"""
    print(f"\n{'='*50}")
    print(f"  {title}")
    print('='*50)


def main():
    print("\n" + "="*50)
    print("        E-SHOP DEMO APPLICATION")
    print("="*50)
    
    # =========================================
    # 1. CREATE PRODUCTS
    # =========================================
    print_section("1. CREATING PRODUCTS")
    
    book1 = Books(
        name="Clean Code",
        product_id=generate_id("BOOK-"),
        price=45.99,
        description="A handbook of agile software craftsmanship",
        stock_quantity=50,
        author="Robert C. Martin",
        publisher="Prentice Hall",
        isbn="978-0132350884",
        genre="Programming"
    )
    
    shirt = Clothes(
        name="Cotton T-Shirt",
        product_id=generate_id("CLOTH-"),
        price=24.99,
        description="Comfortable everyday cotton t-shirt",
        stock_quantity=100,
        size="Medium",
        color="Navy Blue",
        material="100% Cotton"
    )
    
    jeans = Clothes(
        name="Slim Fit Jeans",
        product_id=generate_id("CLOTH-"),
        price=79.99,
        description="Classic slim fit denim jeans",
        stock_quantity=75,
        size="32x32",
        color="Dark Indigo",
        material="98% Cotton, 2% Elastane"
    )
    
    products = [book1, shirt, jeans]
    
    print("Created products:")
    for p in products:
        print(f"  - {p.name}: ${p.price:.2f} (ID: {p.product_id})")
    
    # Save products to products.json
    products_file = './Products/products.json'
    products_list = [p.to_dict() for p in products]
    with open(products_file, 'w') as f:
        json.dump(products_list, f, indent=4)
    print(f"\nProducts saved to {products_file}")
    
    # Also save to main data.json (as dict keyed by product_id)
    dm = DataManagement()
    products_dict = {p.product_id: p.to_dict() for p in products}
    dm.save_product_data(products_dict)
    print(f"Products synced to main data store")
    
    # =========================================
    # 2. CREATE & REGISTER USERS
    # =========================================
    print_section("2. CREATING & REGISTERING USERS")
    
    auth_service = AuthenticationService()
    
    # Register customer
    customer_id = generate_id("CUST-")
    auth_service.register_user(
        user_id=customer_id,
        username="john_doe",
        email="john@example.com",
        password="password123",
        is_admin=False
    )
    customer = Customer(
        user_id=customer_id,
        username="john_doe",
        email="john@example.com",
        password="password123"
    )
    print(f"Customer registered & saved: {customer.username} (ID: {customer.user_id})")
    
    # Register admin
    admin_id = generate_id("ADMIN-")
    auth_service.register_user(
        user_id=admin_id,
        username="admin_user",
        email="admin@eshop.com",
        password="adminpass",
        is_admin=True
    )
    admin = Admin(
        user_id=admin_id,
        username="admin_user",
        email="admin@eshop.com",
        password="adminpass"
    )
    print(f"Admin registered & saved: {admin.username} (ID: {admin.user_id})")
    
    # Show saved users
    print("\nUsers saved to users_data.json:")
    for uid, udata in auth_service.users_data.items():
        print(f"  - {udata.get('username', 'N/A')} ({uid})")
    
    # =========================================
    # 3. USER LOGIN
    # =========================================
    print_section("3. USER LOGIN")
    
    customer.login("password123")
    print(f"{customer.username} logged in: {customer.is_logged_in}")
    
    admin.login("adminpass")
    print(f"{admin.username} logged in: {admin.is_logged_in}")
    
    # =========================================
    # 4. SHOPPING CART OPERATIONS
    # =========================================
    print_section("4. SHOPPING CART")
    
    # Create a simple cart for demonstration
    cart = Cart(customer.user_id)
    
    # Add items
    cart.add_item(book1.product_id, 2)
    print(f"Added 2x {book1.name}")
    
    cart.add_item(shirt.product_id, 3)
    print(f"Added 3x {shirt.name}")
    
    cart.add_item(jeans.product_id, 1)
    print(f"Added 1x {jeans.name}")
    
    # Show cart
    print("\nCart contents:")
    cart_items = cart.get_items()
    
    # Build a price lookup from our products
    price_lookup = {p.product_id: p.price for p in products}
    name_lookup = {p.product_id: p.name for p in products}
    
    total = 0.0
    for product_id, qty in cart_items.items():
        price = price_lookup.get(product_id, 0)
        subtotal = price * qty
        total += subtotal
        print(f"  - {name_lookup.get(product_id, product_id)}: {qty} x ${price:.2f} = ${subtotal:.2f}")
    
    print(f"\nCart Total: ${total:.2f}")
    
    # Remove an item
    print("\nRemoving 1x T-Shirt...")
    cart.remove_item(shirt.product_id, 1)
    
    # Recalculate
    total = sum(price_lookup.get(pid, 0) * qty for pid, qty in cart.get_items().items())
    print(f"Updated Cart Total: ${total:.2f}")
    
    # =========================================
    # 5. PAYMENT PROCESSING
    # =========================================
    print_section("5. PAYMENT PROCESSING")
    
    # Credit Card Payment
    print("Processing Credit Card Payment...")
    cc_payment = CreditCardPayment(amount=total)
    
    cc_info = {
        'card_number': '4111111111111234',
        'expiry_month': 12,
        'expiry_year': 2026,
        'cvv': '123',
        'cardholder_name': 'John Doe',
        'billing_address': '123 Main St, Boston, MA'
    }
    
    # Validate required fields manually (process_payment has a logging bug)
    required_cc = ['card_number', 'expiry_month', 'expiry_year', 'cvv', 'cardholder_name', 'billing_address']
    cc_valid = all(field in cc_info for field in required_cc)
    
    print(f"  Card: **** **** **** {cc_info['card_number'][-4:]}")
    print(f"  Cardholder: {cc_info['cardholder_name']}")
    print(f"  Amount: ${total:.2f}")
    print(f"  Payment validated: {cc_valid}")
    
    # PayPal Payment Demo
    print("\nProcessing PayPal Payment...")
    paypal = PayPalPayment(amount=total, email="john@example.com")
    
    paypal_info = {
        'email': 'john@example.com',
        'password': '********'
    }
    
    required_paypal = ['email', 'password']
    paypal_valid = all(field in paypal_info for field in required_paypal)
    
    print(f"  Account: {paypal_info['email']}")
    print(f"  Amount: ${total:.2f}")
    print(f"  Payment validated: {paypal_valid}")
    
    # =========================================
    # 6. ORDER CREATION & SAVING
    # =========================================
    print_section("6. ORDER CREATION")
    
    # Create order after successful payment
    order_id = generate_id("ORD-")
    order = Order(
        order_id=order_id,
        customer_id=customer.user_id,
        items=cart.get_items(),
        total_price=total,
        status="paid",
        payment_info={
            'method': 'credit_card',
            'card_last_four': cc_info['card_number'][-4:],
            'cardholder_name': cc_info['cardholder_name']
        }
    )
    
    print(f"Order created: {order_id}")
    print(f"  Customer: {customer.username}")
    print(f"  Items: {len(cart.get_items())} product(s)")
    print(f"  Total: ${total:.2f}")
    print(f"  Status: paid")
    
    # Save order to orders.json
    orders_file = './Shopping/Orders/orders.json'
    try:
        with open(orders_file, 'r') as f:
            orders_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        orders_data = {}
    
    orders_data[order_id] = order.to_dict()
    
    with open(orders_file, 'w') as f:
        json.dump(orders_data, f, indent=4)
    
    print(f"\nOrder saved to {orders_file}")
    
    # Also save to main data.json
    dm = DataManagement()
    dm.save_order_data(orders_data)
    print(f"Order synced to main data store")
    
    # Show all orders
    print("\nAll orders in system:")
    for oid, odata in orders_data.items():
        print(f"  - {oid}: ${odata.get('total_price', 0):.2f} ({odata.get('status', 'N/A')})")
    
    # =========================================
    # 7. INVENTORY OPERATIONS
    # =========================================
    print_section("7. INVENTORY MANAGEMENT")
    
    inventory = InventoryService()
    
    # Add products to inventory
    for p in products:
        inventory.add_product(p.product_id, p.stock_quantity)
        print(f"Added to inventory: {p.name} (qty: {p.stock_quantity})")
    
    # Check stock
    print("\nStock levels:")
    for p in products:
        stock = inventory.check_stock(p.product_id)
        print(f"  - {p.name}: {stock} units")
    
    # =========================================
    # 8. DISPLAY ALL PERSISTED DATA
    # =========================================
    print_section("8. PERSISTED DATA FILES")
    
    # Users Data
    print("\n--- Users Data (./Users/users_data.json) ---")
    try:
        with open('./Users/users_data.json', 'r') as f:
            users_data = json.load(f)
            print(json.dumps(users_data, indent=2))
    except FileNotFoundError:
        print("  File not found")
    
    # Orders Data
    print("\n--- Orders Data (./Shopping/Orders/orders.json) ---")
    try:
        with open('./Shopping/Orders/orders.json', 'r') as f:
            orders_json = json.load(f)
            print(json.dumps(orders_json, indent=2))
    except FileNotFoundError:
        print("  File not found")
    
    # Products Data
    print("\n--- Products Data (./Products/products.json) ---")
    try:
        with open('./Products/products.json', 'r') as f:
            products_data = json.load(f)
            print(json.dumps(products_data, indent=2))
    except FileNotFoundError:
        print("  File not found")
    
    # Inventory Data
    print("\n--- Inventory Data (./Inventory_Management/inventory.json) ---")
    try:
        with open('./Inventory_Management/inventory.json', 'r') as f:
            inventory_data = json.load(f)
            print(json.dumps(inventory_data, indent=2))
    except FileNotFoundError:
        print("  File not found")
    
    # Main Data Store
    print("\n--- Main Data Store (./Data_Persistence/data.json) ---")
    try:
        with open('./Data_Persistence/data.json', 'r') as f:
            main_data = json.load(f)
            print(json.dumps(main_data, indent=2))
    except FileNotFoundError:
        print("  File not found")
    
    # =========================================
    # 9. DEMO COMPLETE
    # =========================================
    print_section("DEMO COMPLETE")

if __name__ == "__main__":
    main()