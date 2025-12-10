# E-Shop: Python E-Commerce System

A modular e-commerce application demonstrating OOP principles in Python.

---

## Project Structure

```
Final_Project/
├── Data_Persistence/
│   └── data.py                 # Centralized JSON storage
├── Inventory_Management/
│   └── inventory.py            # Stock tracking
├── Products/
│   ├── product.py              # Base Product class
│   ├── productManagement.py    # Product CRUD operations
│   ├── books.py, clothes.py    # Product subclasses
├── Shopping/
│   ├── Carts/cart.py           # Shopping cart
│   ├── Orders/orderService.py  # Order processing
│   └── Payments/               # Payment methods
│       ├── payment.py          # Abstract base class
│       ├── credit_card.py, paypal.py, etc.
├── Users/
│   ├── user.py                 # Base User class
│   ├── customer.py, admin.py   # User subclasses
│   └── authentication.py       # Login/registration
├── demo.py
└── README.md
```

---

## Class Hierarchy

**Products:** `Product` → `Books`, `Clothes`, `Electronics`, `Food`

**Users:** `User` → `Customer`, `Admin`

**Payments:** `Payment` (abstract) → `CreditCardPayment`, `PayPalPayment`, `ApplePayPayment`, `BankTransferPayment`

---

## Design Patterns Used

| Pattern | Where | Purpose |
|---------|-------|---------|
| Strategy | Payments | Swap payment methods at runtime |
| Template Method | Products | Override `get_details()` in subclasses |
| Repository | Services | Abstract data access from business logic |
| Factory Method | `from_dict()` | Reconstruct objects from JSON |

---

## Setup & Running

**Requirements:** Python 3.8+

**Setup:**
```bash
cd Final_Project

# Create required JSON files with empty objects {}
echo "{}" > Inventory_Management/inventory.json
echo "[]" > Products/products.json
```

**Run:**
```bash
python demo.py
```

---

## User Guide

### Customer Workflow

```python
from Users.customer import Customer
from Shopping.Carts.cart import Cart
from Shopping.Payments.credit_card import CreditCardPayment

# 1. Create account & login
customer = Customer("CUST-001", "john", "john@email.com", "pass123")
customer.login("pass123")

# 2. Add items to cart
customer.add_to_cart("BOOK-001", quantity=2)
customer.add_to_cart("CLOTH-001", quantity=1)

# 3. View cart
items = customer.cart.get_items()

# 4. Checkout
payment = CreditCardPayment(amount=99.99)
payment_info = {
    'card_number': '4111111111111234',
    'expiry_month': 12,
    'expiry_year': 2026,
    'cvv': '123',
    'cardholder_name': 'John Doe',
    'billing_address': '123 Main St'
}
payment.process_payment(99.99, payment_info)
```

### Admin Workflow

```python
from Users.admin import Admin
from Products.books import Books

# 1. Login as admin
admin = Admin("ADMIN-001", "admin", "admin@shop.com", "adminpass")
admin.login("adminpass")

# 2. Add new product
book = Books("New Book", "BOOK-002", 29.99, "Description", 50,
             "Author", "Publisher", "ISBN", "Genre")
admin.add_inventory(book)

# 3. View inventory
inventory = admin.view_inventory()
```

---

## Assumptions & Limitations

- **No real payments** — Payment methods simulate transactions only
- **No encryption** — Passwords stored in plain text
- **JSON storage** — No database; data stored in local JSON files
- **Single user** — No concurrent access handling
- **No validation** — Minimal input checking

---

## License

Educational project demonstrating Python OOP principles.