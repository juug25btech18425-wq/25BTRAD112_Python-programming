# Mini Project (Unit 3): Sales Data Analyzer
products = {}

while True:
    print("\n1. Add Product")
    print("2. Update Product")
    print("3. Display Sales")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter product name: ")
        quantity = int(input("Enter quantity sold: "))
        price = float(input("Enter price: "))
        products[name] = [quantity, price]

    elif choice == 2:
        name = input("Enter product name: ")

        if name in products:
            quantity = int(input("Enter new quantity: "))
            price = float(input("Enter new price: "))
            products[name] = [quantity, price]
        else:
            print("Product not found")

    elif choice == 3:
        total_sales = 0
        highest = ""

        for name, data in products.items():
            quantity = data[0]
            price = data[1]

            revenue = quantity * price
            total_sales += revenue

            print(name, "Quantity:", quantity)
            print("Revenue:", revenue)

            if highest == "" or quantity > products[highest][0]:
                highest = name

        print("Total Sales:", total_sales)

        if highest != "":
            print("Highest Selling Product:", highest)

    elif choice == 4:
        break

    else:
        print("Invalid choice")
