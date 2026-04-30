contacts = {'tanveer': 9963256876,'raju': 7876544876,'rakesh': 8787878787}

# creating function for adding new contacts
def add_contact(name: str, mobile: int):
    if name not in contacts:
        contacts[name] = mobile
        return "Contact saved"
    return "Contact name already exists, check with another name"

# creating function for updating contacts
def update_contact(name: str, mobile: int):
    if name in contacts:
        contacts[name] = mobile
        return "Contact updated"
    return "Contact is not there, check name again"

# function for deleting the contact
def delete_contact(name: str):
    if name in contacts:
        contacts.pop(name)
        return "Contact deleted"
    return "Contact doesn't exist, check name again"

# function for getting the mobile number
def get_mobile_number(name: str):
    if name in contacts:
        return contacts[name]
    return "Contact not found"

# all contacts
def all_contacts():
    return contacts


# main
if __name__ == "__main__":
    print("Welcome to the Contacts Management System")

    while True:
        print("\nSelect your operation")
        print("1. Add contacts")
        print("2. Update contacts")
        print("3. Delete contacts")
        print("4. Search mobile number by name")
        print("5. See all contacts")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter contact name: ").strip()
            number = int(input("Enter mobile number: "))
            res = add_contact(name, number)
            print(res)

        elif choice == 2:
            name = input("Enter contact name: ").strip()
            number = int(input("Enter new mobile number: "))
            res = update_contact(name, number)
            print(res)

        elif choice == 3:
            name = input("Enter contact name: ").strip()
            res = delete_contact(name)
            print(res)

        elif choice == 4:
            name = input("Enter contact name: ").strip()
            res = get_mobile_number(name)
            print(res)

        elif choice == 5:
            res = all_contacts()
            for name, mobile in res.items():
                print(f"{name}: {mobile}")

        elif choice == 6:
            print("You exited from the application. Bye!")
            break

        else:
            print("Invalid choice. Select between (1-6)")