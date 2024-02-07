import json

class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email):
        self.contacts[name] = {"Phone": phone, "Email": email}
        print(f"Contact '{name}' added successfully.")

    def view_contact(self, name):
        if name in self.contacts:
            print(f"Contact Name: {name}")
            print(f"Phone: {self.contacts[name]['Phone']}")
            print(f"Email: {self.contacts[name]['Email']}")
        else:
            print(f"Contact '{name}' not found.")

    def list_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("Contact List:")
            for name in self.contacts:
                print(f" - {name}")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' deleted successfully.")
        else:
            print(f"Contact '{name}' not found.")

    def save_to_file(self, filename="contacts.json"):
        with open(filename, "w") as file:
            json.dump(self.contacts, file)
        print(f"Contacts saved to {filename}.")

    def load_from_file(self, filename="contacts.json"):
        try:
            with open(filename, "r") as file:
                self.contacts = json.load(file)
            print(f"Contacts loaded from {filename}.")
        except FileNotFoundError:
            print(f"File {filename} not found.")

if __name__ == "__main__":
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contact")
        print("3. List Contacts")
        print("4. Delete Contact")
        print("5. Save Contacts to File")
        print("6. Load Contacts from File")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            contact_book.add_contact(name, phone, email)

        elif choice == '2':
            name = input("Enter contact name: ")
            contact_book.view_contact(name)

        elif choice == '3':
            contact_book.list_contacts()

        elif choice == '4':
            name = input("Enter contact name to delete: ")
            contact_book.delete_contact(name)

        elif choice == '5':
            filename = input("Enter filename to save (default: contacts.json): ")
            contact_book.save_to_file(filename)

        elif choice == '6':
            filename = input("Enter filename to load from (default: contacts.json): ")
            contact_book.load_from_file(filename)

        elif choice == '7':
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")
