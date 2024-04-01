from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        sanitized_value = ''.join(char for char in value if char.isdigit() or char in {'+', '-', '(', ')'})
        if len(sanitized_value) != 10:
            raise ValueError("Phone number must contain 10 digits.")

        self.value = sanitized_value

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                return
        raise ValueError("Phone number not found in record.")

    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if p.value == old_phone:
                try:
                    new_phone = Phone(new_phone)
                except ValueError as e:
                    raise ValueError(f"Error: {e}")
                p.value = new_phone.value
                return
        raise ValueError("Phone number not found in record.")

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def __str__(self):
        phones_str = ', '.join(str(phone.value) for phone in self.phones)
        return f"Contact name: {self.name.value}, phones: {phones_str}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def delete_record(self, name):
        if name in self.data:
            del self.data[name]
            print("Record removed successfully.")
        else:
            print("Record not found.")

    def find_record(self, name):
        return self.data.get(name)

    def show_all_records(self):
        if self.data:
            print("All records in the address book:")
            for name, record in self.data.items():
                print(f"{name}: {record}")
        else:
            print("Address book is empty.")

def main():
    book = AddressBook()

    print("Welcome to the Address Book!")

    while True:
        print("\nOptions:")
        print("1. Add record")
        print("2. Search record")
        print("3. Remove record")
        print("4. Show all records")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter the name: ")
            record = Record(name)
            phone = input("Enter the phone number: ")
            record.add_phone(phone)
            book.add_record(record)
            print("Record added successfully.")
        elif choice == "2":
            name = input("Enter the name to search: ")
            found_record = book.find_record(name)
            if found_record:
                print(found_record)
            else:
                print("Record not found.")
        elif choice == "3":
            name = input("Enter the name to remove: ")
            book.delete_record(name)
        elif choice == "4":
            book.show_all_records()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
