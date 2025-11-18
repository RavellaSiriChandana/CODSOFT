contacts = {}

while True:
    print("\n1. Add  2. View  3. Exit")
    choice = input("Choose: ")

    if choice == "1":
        name = input("Name: ")
        number = input("Number: ")
        contacts[name] = number
        print("Saved!")

    elif choice == "2":
        print("\nContacts:")
        for name, number in contacts.items():
            print(name, ":", number)

    elif choice == "3":
        print("Bye!")
        break

    else:
        print("Invalid choice!")
