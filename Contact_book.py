
# Contact Management System

contacts = []

while True:

    print("\n========== CONTACT MANAGEMENT SYSTEM ==========")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("\nEnter your choice (1-6): ")

    # Add Contact
    if choice == "1":

        print("\n----- Add Contact -----")

        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        email = input("Enter Email: ")
        

        contact = {
            "name": name,
            "phone": phone,
            "email": email,
            
        }

        contacts.append(contact)

        print("\nContact added successfully!")

    # View Contacts
    elif choice == "2":

        print("\n----- Contact List -----")

        if len(contacts) == 0:
            print("No contacts available!")

        else:
            for i, contact in enumerate(contacts, start=1):

                print("\nContact Number:", i)
                print("Name:", contact["name"])
                print("Phone:", contact["phone"])
                print("Email:", contact["email"])
            
    # Search Contact
    elif choice == "3":

        print("\n----- Search Contact -----")

        search = input("Enter name or phone number: ").lower()

        found = False

        for contact in contacts:

            if (search in contact["name"].lower() or
                    search in contact["phone"]):

                print("\nContact Found!")
                print("Name:", contact["name"])
                print("Phone:", contact["phone"])
                print("Email:", contact["email"])
                

                found = True

        if not found:
            print("Contact not found!")

    # Update Contact
    elif choice == "4":

        print("\n----- Update Contact -----")

        phone = input("Enter phone number to update: ")

        found = False

        for contact in contacts:

            if contact["phone"] == phone:

                contact["name"] = input("Enter New Name: ")
                contact["phone"] = input("Enter New Phone: ")
                contact["email"] = input("Enter New Email: ")
               
                print("\nContact updated successfully!")

                found = True
                break

        if not found:
            print("Contact not found!")

    # Delete Contact
    elif choice == "5":

        print("\n----- Delete Contact -----")

        phone = input("Enter phone number to delete: ")

        found = False

        for contact in contacts:

            if contact["phone"] == phone:

                contacts.remove(contact)

                print("\nContact deleted successfully!")

                found = True
                break

        if not found:
            print("Contact not found!")

    # Exit
    elif choice == "6":

        print("\nThank you for using Contact Management System!")
        break

    else:
        print("\nInvalid choice! Please enter a number between 1 and 6.")
