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

    def edit_name(self, new_name):
        self.name.value = new_name

    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                return
        raise ValueError("Phone number not found in record.")

    def __str__(self):
        phones_str = ', '.join(str(phone.value) for phone in self.phones)
        return f"Contact name: {self.name.value}, phones: {phones_str}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def delete(self, name):
        del self.data[name]

    def find(self, name):
        return self.data[name]

    def search_record(self, name):
        for record in self.data.values():
            if record.name.value == name:
                return record
        return None

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
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            print("All records in the address book:")
            for name, record in book.data.items():
                print(f"{name}: {record}")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
