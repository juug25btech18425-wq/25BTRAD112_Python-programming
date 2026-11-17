# Lab Exercise 8: Contact Book Using Lists and Dictionaries
contacts = []

while True:
    print("\n--- CONTACT BOOK ---")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display Contacts")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contact = {"name": name, "phone": phone}
        contacts.append(contact)
        print("Contact added successfully!")

    elif choice == 2:
        name = input("Enter name to search: ")
        found = False
        for contact in contacts:
            if contact["name"] == name:
                print("Phone:", contact["phone"])
                found = True
        if found == False:
            print("Contact not found!")

    elif choice == 3:
        name = input("Enter name to update: ")
        found = False
        for contact in contacts:
            if contact["name"] == name:
                phone = input("Enter new phone number: ")
                contact["phone"] = phone
                print("Contact updated!")
                found = True
        if found == False:
            print("Contact not found!")

    elif choice == 4:
        name = input("Enter name to delete: ")
        found = False
        for contact in contacts:
            if contact["name"] == name:
                contacts.remove(contact)
                print("Contact deleted!")
                found = True
                break
        if found == False:
            print("Contact not found!")

    elif choice == 5:
        for contact in contacts:
            print("Name:", contact["name"])
            print("Phone:", contact["phone"])

    elif choice == 6:
        print("Exiting Contact Book...")
        break

    else:
        print("Invalid choice!")
