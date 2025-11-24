import random

class Product:
    def __init__(self, name, price, description, stock):
        self.name = name
        self.price = price
        self.description = description
        self.stock = stock

    def __str__(self):
        return f"{self.name} - ₹{self.price:.2f}\n{self.description}\nIn Stock: {self.stock} units"

class Electronic(Product):
    def __init__(self, name, price, description, stock, brand):
        super().__init__(name, price, description, stock)
        self.brand = brand

    def __str__(self):
        return super().__str__() + f"\nBrand: {self.brand}"

class Food(Product):
    def __init__(self, name, price, description, stock, expiration_date):
        super().__init__(name, price, description, stock)
        self.expiration_date = expiration_date

    def __str__(self):
        return super().__str__() + f"\nExpiration Date: {self.expiration_date}"

class Furniture(Product):
    def __init__(self, name, price, description, stock, material):
        super().__init__(name, price, description, stock)
        self.material = material

    def __str__(self):
        return super().__str__() + f"\nMaterial: {self.material}"

class Clothes(Product):
    def __init__(self, name, price, description, stock, size):
        super().__init__(name, price, description, stock)
        self.size = size

    def __str__(self):
        return super().__str__() + f"\nSize: {self.size}"

class Grocery(Product):
    def __init__(self, name, price, description, stock, expiration_date):
        super().__init__(name, price, description, stock)
        self.expiration_date = expiration_date

    def __str__(self):
        return super().__str__() + f"\nExpiration Date: {self.expiration_date}"

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.cart = []

    def add_to_cart(self, product, quantity):
        if product.stock >= quantity:
            self.cart.append((product, quantity))
            product.stock -= quantity
            print(f"{quantity} {product.name}(s) added to your cart.")
        else:
            print(f"Sorry, we only have {product.stock} {product.name}(s) in stock.")

    def remove_from_cart(self, product, quantity):
        for item in self.cart:
            if item[0] == product:
                if item[1] >= quantity:
                    item[1] -= quantity
                    product.stock += quantity
                    if item[1] == 0:
                        self.cart.remove(item)
                    print(f"{quantity} {product.name}(s) removed from your cart.")
                else:
                    print(f"You have only {item[1]} {product.name}(s) in your cart.")
                break

    def view_cart(self):
        if not self.cart:
            print("Your cart is empty.")
        else:
            total_price = sum(item[0].price * item[1] for item in self.cart)
            print("Your Cart:")
            for item in self.cart:
                product, quantity = item
                print(f"{product.name} - ₹{product.price:.2f} x {quantity}")
            print(f"Total Price: ₹{total_price:.2f}")

def browse_products(products):
    print("\nBrowse Products:")
    print("1. All Products")
    print("2. Food Items")
    print("3. Electronic Items")
    print("4. Clothes Items")
    print("5. Furniture Items")
    print("6. Grocery Items")  # Added option for grocery items

    category_choice = input("Select a category (1-6): ")

    if category_choice == '1':
        category_products = products
    elif category_choice == '2':
        category_products = [product for product in products if isinstance(product, Food)]
    elif category_choice == '3':
        category_products = [product for product in products if isinstance(product, Electronic)]
    elif category_choice == '4':
        category_products = [product for product in products if isinstance(product, Clothes)]
    elif category_choice == '5':
        category_products = [product for product in products if isinstance(product, Furniture)]
    elif category_choice == '6':
        category_products = [product for product in products if isinstance(product, Grocery)]
    else:
        print("Invalid category selection.")
        return

    for i, product in enumerate(category_products, start=1):
        print(f"{i}. {product}")

def main():
    products = [
        Electronic("Laptop", 80000.00, "High-performance laptop.", 10, "MSI"),
        Electronic("Smartphone", 40000.00, "Latest smartphone model.", 20, "Samsung"),
        Electronic("Headphones", 5000.00, "Wireless headphones.", 15, "Brand Sony"),
        Electronic("Speaker", 3000.00, "Wireless portable speaker.", 30, "Zebronics"),
        Electronic("Charger", 1000.00, "Charger.", 20, "Samsung"),
        Food("Chocolate", 100.00, "Delicious chocolate.", 50, "2023-12-31"),
        Food("Chips", 50.00, "Crunchy chips.", 30, "2023-10-31"),
        Furniture("Chair", 2000.00, "Comfortable chair.", 5, "Wood"),
        Furniture("Table", 5000.00, "Sturdy table.", 8, "Metal"),
        Clothes("T-Shirt", 300.00, "Cotton T-shirt.", 25, "Medium"),
        Clothes("Jeans", 800.00, "Denim jeans.", 15, "32x34"),
        Food("Apple", 30.00, "Fresh and crunchy apple.", 25, "2023-11-30"),
        Food("Pizza", 150.00, "Delicious pizza.", 10, "2023-12-15"),
        Electronic("Smartwatch", 10000.00, "Fitness and health tracker.", 15, "Brand D"),
        Electronic("Camera", 20000.00, "High-resolution camera.", 12, "Brand E"),
        Clothes("Sweater", 500.00, "Warm and cozy sweater.", 20, "Large"),
        Clothes("Dress Shirt", 700.00, "Formal dress shirt.", 15, "Medium"),
        Furniture("Bookshelf", 6000.00, "Wooden bookshelf.", 10, "Wood"),
        Furniture("Sofa", 12000.00, "Comfortable sofa.", 8, "Leather"),
        Grocery("Milk", 40.00, "Fresh and nutritious milk.", 20, "2023-11-30"),
        Grocery("Bread", 25.00, "Whole grain bread.", 15, "2023-12-15"),
        Electronic("Mouse", 800.00, "Wireless gaming mouse.", 25, "Logitech"),
        Electronic("Keyboard", 1500.00, "Mechanical gaming keyboard.", 20, "Corsair"),
        Electronic("Monitor", 12000.00, "27-inch high-resolution monitor.", 15, "Dell"),
        Electronic("Fitness Tracker", 3000.00, "Tracks your daily activities.", 30, "Fitbit"),
        Electronic("Portable Hard Drive", 4000.00, "1TB portable hard drive.", 10, "Seagate"),
        Food("Banana", 10.00, "Ripe and healthy banana.", 40, "2023-11-30"),
        Food("Granola Bars", 20.00, "Healthy snack bars.", 25, "2023-12-31"),
        Food("Pasta", 30.00, "Italian pasta.", 20, "2023-10-31"),
        Food("Orange Juice", 40.00, "Freshly squeezed orange juice.", 15, "2023-12-15"),
        Food("Yogurt", 15.00, "Greek yogurt.", 35, "2023-11-15"),
        Furniture("Desk", 8000.00, "Modern study desk.", 10, "Glass"),
        Furniture("Bed", 25000.00, "King-size comfortable bed.", 5, "Wood"),
        Furniture("Wardrobe", 15000.00, "Spacious wardrobe.", 8, "Metal"),
        Furniture("Coffee Table", 3000.00, "Elegant coffee table.", 15, "Marble"),
        Furniture("Lamp", 500.00, "Desk lamp with adjustable brightness.",20, "Plastic"),



    ]

    users = []

    while True:
        print("\n*********************************************")
        print("**              1. Register                **")
        print("**              2. Login                   **")
        print("**              3. Exit                    **")
        print("*********************************************")
        choice = input("Select an option: ")

        if choice == '1':
            print("*********************************************")
            username = input("**              Enter a username: ")
            password = input("**              Enter a password: ")
            print("*********************************************")
            users.append(User(username, password))
            print("Registration successful. Please login to continue.")

        elif choice == '2':
            print("*********************************************")
            username = input("**              Username: ")
            password = input("**              Password: ")
            print("*********************************************")
            for user in users:
                if user.username == username and user.password == password:
                    current_user = user
                    while True:
                        print("\n*********************************************")
                        print("**              1. Browse Products         **")
                        print("**              2. View Cart               **")
                        print("**              3. Logout                  **")
                        print("*********************************************")
                        option = input("Select an option: ")

                        if option == '1':
                            browse_products(products)

                            product_index = int(input("Select a product (1-30): ")) - 1

                            if 0 <= product_index < len(products):
                                selected_product = products[product_index]
                                quantity = int(input("Enter the quantity: "))
                                current_user.add_to_cart(selected_product, quantity)
                            else:
                                print("Invalid product selection.")

                        elif option == '2':
                            current_user.view_cart()
                            action = input("1. Checkout\n2. Remove from cart\n3. Back\nSelect an option: ")
                            if action == '1':
                                print("Checkout successful. Thank you for shopping with us!")
                                exit()
                            elif action == '2':
                                print("\nYour Cart:")
                                for i, item in enumerate(current_user.cart, start=1):
                                    product, quantity = item
                                    print(f"{i}. {product.name} - x{quantity}")
                                cart_index = int(input("Select an item to remove (1-30): ")) - 1
                                if 0 <= cart_index < len(current_user.cart):
                                    cart_item = current_user.cart[cart_index]
                                    selected_product, quantity = cart_item
                                    current_user.remove_from_cart(selected_product, quantity)
                                else:
                                    print("Invalid cart item selection.")
                            elif action == '3':
                                pass
                            else:
                                print("Invalid option.")

                        elif option == '3':
                            print("Logging out.")
                            break
                        else:
                            print("Invalid option.")

        elif choice == '3':
            print("Exiting the program.")
            exit()
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
