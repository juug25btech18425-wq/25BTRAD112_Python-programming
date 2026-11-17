# Mini Project: Simple Bill Generator
print("===== BILL GENERATOR =====")

item1 = input("Enter first item: ")
quantity1 = int(input("Enter quantity: "))
price1 = float(input("Enter price: "))

item2 = input("Enter second item: ")
quantity2 = int(input("Enter quantity: "))
price2 = float(input("Enter price: "))

item3 = input("Enter third item: ")
quantity3 = int(input("Enter quantity: "))
price3 = float(input("Enter price: "))

amount1 = quantity1 * price1
amount2 = quantity2 * price2
amount3 = quantity3 * price3

total = amount1 + amount2 + amount3

print("\n===== BILL =====")
print(item1, "Quantity:", quantity1, "Amount:", amount1)
print(item2, "Quantity:", quantity2, "Amount:", amount2)
print(item3, "Quantity:", quantity3, "Amount:", amount3)

print("Total Amount:", total)
print("Thank you! Visit again.")
