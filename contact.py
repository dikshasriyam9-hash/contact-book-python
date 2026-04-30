def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    with open("contacts.txt", "a") as file:
        file.write(name + "," + phone + "\n")

    print("Contact saved successfully!")


def view_contacts():
    try:
        with open("contacts.txt", "r") as file:
            contacts = file.readlines()

            if not contacts:
                print("No contacts found.")
                return

            print("\n--- Contact List ---")
            for contact in contacts:
                name, phone = contact.strip().split(",")
                print(f"Name: {name} | Phone: {phone}")

    except FileNotFoundError:
        print("No contacts file found.")


def search_contact():
    search_name = input("Enter name to search: ")

    try:
        with open("contacts.txt", "r") as file:
            found = False

            for contact in file:
                name, phone = contact.strip().split(",")

                if name.lower() == search_name.lower():
                    print(f"Found: {name} | Phone: {phone}")
                    found = True
                    break

            if not found:
                print("Contact not found.")

    except FileNotFoundError:
        print("No contacts file found.")


def menu():
    print("\n--- Contact Book ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")


while True:
    menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Try again.")