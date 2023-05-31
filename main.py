products = [{
  "id": 1,
  "name": "T-Shirt",
  "category": "Clothes",
  "price": 120000,
  "stock": 10
}, {
  "id": 2,
  "name": "Jeans",
  "category": "Clothes",
  "price": 300000,
  "stock": 10
}, {
  "id": 3,
  "name": "Sneakers",
  "category": "Shoes",
  "price": 550000,
  "stock": 10
}, {
  "id": 4,
  "name": "Boots",
  "category": "Shoes",
  "price": 700000,
  "stock": 10
}, {
  "id": 5,
  "name": "Sling Bag",
  "category": "Bags",
  "price": 100000,
  "stock": 10
}, {
  "id": 6,
  "name": "Backpack",
  "category": "Bags",
  "price": 150000,
  "stock": 10
}, {
  "id": 7,
  "name": "Glasses",
  "category": "Accessories",
  "price": 50000,
  "stock": 10
}, {
  "id": 8,
  "name": "Watch",
  "category": "Accessories",
  "price": 130000,
  "stock": 10
}]

cart = []


# Menampilkan seluruh produk di variabel products
def display_products():
  print("--- PRODUCTS ---\n")
  for product in products:
    print(
      f"{product['id']}. {product['name']}: Rp{product['price']} | stock: {product['stock']}"
    )


# Menampilkan seluruh item di variabel cart
def display_cart():
  if not cart:
    print("\nYour cart is empty.\n")
  else:
    print("--- ITEMS ---\n")
    for i, item in enumerate(cart):
      product = item["product"]
      print(
        f"{i+1}. Product ID: {product['id']} | {product['name']}: Rp{product['price']} x {item['quantity']} = Rp{product['price'] * item['quantity']}"
      )
  print()


# Menambahkan item ke dalam variabel cart
def add_to_cart(product_id, quantity):
  for product in products:
    if product["id"] == product_id:
      if product["stock"] >= quantity:
        item = {"id": product_id, "product": product, "quantity": quantity}
        cart.append(item)
        product["stock"] -= quantity
        print(f"\nAdded {quantity} {product['name']}(s) to the cart.")
      else:
        print("Insufficient stock.")
      return
  print("Product not found.")


# Mengubah quantity item di dalam cart
def edit_cart(product_id, quantity):
  for item in cart:
    if item["id"] == product_id:
      if quantity == 0:
        remove_from_cart(product_id)
        return
      elif quantity > item["quantity"]:
        for product in products:
          if product["id"] == product_id:
            if product["stock"] >= quantity:
              item["quantity"] = quantity
              product["stock"] -= (item["quantity"] - quantity)
              print(
                f"\nYou changed quantity of {product['name']} to {quantity}")
            else:
              print("Insufficient stock.")
            return
      elif quantity < item["quantity"]:
        for product in products:
          if product["id"] == product_id:
            product["stock"] += (item["quantity"] - quantity)
            item["quantity"] = quantity
            print(f"\nYou changed quantity of {product['name']} to {quantity}")
            return
  print("Item not found in the cart.")


# Menghapus item dari cart
def remove_from_cart(product_id):
  for item in cart:
    if item["id"] == product_id:
      product = item["product"]
      product["stock"] += item["quantity"]
      cart.remove(item)
      print(f"\nRemoved {product['name']} from the cart.")
      return
  print("Item not found in the cart.")


# Proses checkout untuk pembayaran
def checkout():
  if not cart:
    print("Your cart is empty. Nothing to checkout.")
    return

  print("\n--- CHECKOUT ---")
  display_cart()
  total_amount = sum(item["product"]["price"] * item["quantity"]
                     for item in cart)
  print(f"Total Amount: Rp{total_amount}")

  while True:
    try:
      amount_paid = int(input("Enter the amount paid: Rp"))
      break
    except ValueError:
      print("Invalid input. Please enter a valid amount.")

  if amount_paid < total_amount:
    print("\nInsufficient amount paid. Please provide the correct amount.")
    return

  change = amount_paid - total_amount
  print(f"Change: Rp{change}")

  confirm_checkout = input("Confirm checkout? (y/n): ").lower()
  if confirm_checkout == "y":
    for item in cart:
      product = item["product"]
      print(f"Checkout {item['quantity']} {product['name']}(s).")
    cart.clear()
    print("\nCheckout successful. Thank you for shopping!")
    main_menu()
  else:
    print("Checkout canceled.")
    cart_menu()


def main_menu():
  print("\nWelcome to PRWDK Shop. Happy shopping!\n")
  print("--- MAIN MENU ---\n")
  print("1. Shopping")
  print("2. Cart")
  print("3. Exit\n")

  choice = input("Please select one of the options above: ")
  if choice == "1":
    shopping_menu()
  elif choice == "2":
    cart_menu()
  elif choice == "3":
    print("\nThank you for shopping with us. Goodbye!")
  else:
    print("Invalid choice. Please try again.\n")
    main_menu()


def shopping_menu():
  while True:
    print("\n--- SHOPPING ---")
    display_products()

    while True:
      try:
        product_id = int(input("\nSelect product ID: "))
        break
      except ValueError:
        print("Invalid input. Please enter a valid product ID.")

    while True:
      try:
        quantity = int(input("Quantity: "))
        break
      except ValueError:
        print("Invalid input. Please enter a valid quantity.")

    add_to_cart(product_id, quantity)
    choice = input(
      "\nPress 'c' to continue shopping or any other key to go back to the main menu: "
    )
    if choice.lower() != "c":
      main_menu()


def cart_menu():
  while True:
    print("\n--- CART ---")
    display_cart()
    if cart:
      print("1. Remove item from cart")
      print("2. Edit Cart")
      print("3. Checkout\n")
      choice = input(
        "Please select one of the options above (Any other input to go back): "
      )
      if choice == "1":
        while True:
          try:
            product_id = int(input("Enter product ID to remove: "))
            break
          except ValueError:
            print("Invalid input. Please enter a valid product ID.")

        remove_from_cart(product_id)
      elif choice == "2":
        while True:
          try:
            product_id = int(input("Enter product ID to edit: "))
            quantity = int(input("Quantity: "))
            break
          except ValueError:
            print(
              "Invalid input. Please enter a valid product ID and quantity.")

        edit_cart(product_id, quantity)
      elif choice == "3":
        checkout()
        break
      else:
        main_menu()
        break
    else:
      input("Press Enter to go back to the main menu.")
      main_menu()


main_menu()
