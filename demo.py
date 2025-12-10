"""
E-Shop Demo Application
=======================
Demonstrates core functionality of the E-Shop system.
"""

from Products.product import Product
from Products.books import Books
from Products.clothes import Clothes
from Shopping.Carts.cart import Cart
from Shopping.Payments.credit_card import CreditCardPayment
from Shopping.Payments.paypal import PayPalPayment
from Users.customer import Customer
from Users.admin import Admin
from Inventory_Management.inventory import InventoryService
import uuid


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
    
    # =========================================
    # 2. CREATE USERS
    # =========================================
    print_section("2. CREATING USERS")
    
    customer = Customer(
        user_id=generate_id("CUST-"),
        username="john_doe",
        email="john@example.com",
        password="password123"
    )
    print(f"Customer created: {customer.username} (ID: {customer.user_id})")
    
    admin = Admin(
        user_id=generate_id("ADMIN-"),
        username="admin_user",
        email="admin@eshop.com",
        password="adminpass"
    )
    print(f"Admin created: {admin.username} (ID: {admin.user_id})")
    
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
    
    cc_result = cc_payment.process_payment(total, cc_info)
    print(f"  Card: **** **** **** {cc_info['card_number'][-4:]}")
    print(f"  Payment successful: {cc_result}")
    
    # PayPal Payment Demo
    print("\nProcessing PayPal Payment...")
    paypal = PayPalPayment(amount=total, email="john@example.com")
    
    paypal_info = {
        'email': 'john@example.com',
        'password': '********'
    }
    
    paypal_result = paypal.process_payment(total, paypal_info)
    print(f"  Account: {paypal_info['email']}")
    print(f"  Payment successful: {paypal_result}")
    
    # =========================================
    # 6. INVENTORY OPERATIONS
    # =========================================
    print_section("6. INVENTORY MANAGEMENT")
    
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
    # 7. DEMO COMPLETE
    # =========================================
    print_section("DEMO COMPLETE")
    print("Successfully demonstrated:")
    print("  [x] Product creation (Books, Clothes)")
    print("  [x] User creation (Customer, Admin)")
    print("  [x] User authentication")
    print("  [x] Shopping cart operations")
    print("  [x] Payment processing")
    print("  [x] Inventory management")
    print()


if __name__ == "__main__":
    main()