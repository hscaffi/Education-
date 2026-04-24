from datetime import datetime

# Students Dictionary
students_dict = {
    1: "John Smith",
    2: "Jane Johnson",
    3: "Jay Bhogal",
    4: "Mike Wong",
    5: "Ali Khan",
    6: "Sara Ahmed",
    7: "David Brown",
    8: "Emily Clark",
    9: "Daniel White",
    10: "Sophia Taylor"
}

# Books Dictionary
books_dict = {
    1: "Python Book 1",
    2: "Python Book 2",
    3: "Python Book 3",
    4: "Python Book 4",
    5: "Python Book 5",
    6: "Math Book 1",
    7: "Math Book 2",
    8: "Math Book 3",
    9: "Math Book 4",
    10: "Math Book 5"
}

# Equipment List
equipment_list = [
    # Laptops (10)
    "Laptop 1", "Laptop 2", "Laptop 3", "Laptop 4", "Laptop 5",
    "Laptop 6", "Laptop 7", "Laptop 8", "Laptop 9", "Laptop 10",

    # Books (10) from books_dict
    "Python Book 1", "Python Book 2", "Python Book 3", "Python Book 4", "Python Book 5",
    "Math Book 1", "Math Book 2", "Math Book 3", "Math Book 4", "Math Book 5",

    # Tablets (10)
    "Tablet 1", "Tablet 2", "Tablet 3", "Tablet 4", "Tablet 5",
    "Tablet 6", "Tablet 7", "Tablet 8", "Tablet 9", "Tablet 10",

    # Projectors (10)
    "Projector A", "Projector B", "Projector C", "Projector D", "Projector E",
    "Projector F", "Projector G", "Projector H", "Projector I", "Projector J",

    # Accessories (10)
    "Mouse 1", "Mouse 2", "Keyboard 1", "Keyboard 2", "Headset 1",
    "Headset 2", "Charger 1", "Charger 2", "HDMI Cable 1", "HDMI Cable 2"
]

# Booking records
bookings = []


def is_valid_date(date_text):
    try:
        datetime.strptime(date_text, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def display_menu():
    print("""
------------------------------------------------------
|====================================================|
|====== Student Equipment Booking System ============|
|====================================================|
------------------------------------------------------

Enter 1 : View Students
Enter 2 : View Books
Enter 3 : View Equipment List
Enter 4 : Add New Equipment
Enter 5 : Search Equipment
Enter 6 : Remove Equipment
Enter 7 : Record Booking
Enter 8 : View Booking Records
Enter 9 : Search Bookings
Enter 10: Exit
""")


def view_students():
    print("\nStudent List:")
    print("-" * 40)
    for student_id, student_name in students_dict.items():
        print(f"{student_id}. {student_name}")


def view_books():
    print("\nBooks List:")
    print("-" * 40)
    for book_id, book_name in books_dict.items():
        print(f"{book_id}. {book_name}")


def view_equipment():
    print("\nEquipment List:")
    print("-" * 40)
    for index, item in enumerate(equipment_list, start=1):
        print(f"{index}. {item}")


def add_equipment():
    new_item = input("Enter New Equipment: ").strip()

    if new_item == "":
        print("\nError: Equipment name cannot be empty.")
        return

    for item in equipment_list:
        if item.lower() == new_item.lower():
            print(f"\nError: '{new_item}' already exists.")
            return

    equipment_list.append(new_item)
    print(f"\nSuccess: '{new_item}' was added to the equipment list.")


def search_equipment():
    search_item = input("Enter Equipment Name To Search: ").strip()

    if search_item == "":
        print("\nError: Search term cannot be empty.")
        return

    found_items = []

    for item in equipment_list:
        if search_item.lower() in item.lower():
            found_items.append(item)

    if found_items:
        print("\nSearch Results:")
        print("-" * 40)
        for item in found_items:
            print(f"=> {item}")
    else:
        print(f"\nNo equipment found for '{search_item}'.")


def remove_equipment():
    remove_item = input("Enter Equipment Name To Remove: ").strip()

    if remove_item == "":
        print("\nError: Equipment name cannot be empty.")
        return

    for item in equipment_list:
        if item.lower() == remove_item.lower():
            equipment_list.remove(item)
            print(f"\nSuccess: '{item}' was removed.")
            return

    print(f"\nError: '{remove_item}' was not found.")


def record_booking():
    view_students()

    try:
        student_id = int(input("Select Student ID: ").strip())
    except ValueError:
        print("\nError: Student ID must be a number.")
        return

    if student_id not in students_dict:
        print("\nError: Invalid student ID.")
        return

    equipment_name = input("Enter Equipment Name: ").strip()
    booking_date = input("Enter Booking Date (YYYY-MM-DD): ").strip()

    if equipment_name == "" or booking_date == "":
        print("\nError: No field can be empty.")
        return

    actual_equipment_name = None
    for item in equipment_list:
        if item.lower() == equipment_name.lower():
            actual_equipment_name = item
            break

    if actual_equipment_name is None:
        print("\nError: Equipment does not exist.")
        return

    if not is_valid_date(booking_date):
        print("\nError: Invalid date format. Use YYYY-MM-DD.")
        return

    for booking in bookings:
        if booking["equipment"].lower() == actual_equipment_name.lower() and booking["date"] == booking_date:
            print("\nError: This equipment is already booked for that date.")
            return

    booking_record = {
        "student_id": student_id,
        "student_name": students_dict[student_id],
        "equipment": actual_equipment_name,
        "date": booking_date
    }

    bookings.append(booking_record)
    print("\nSuccess: Booking recorded successfully.")


def view_bookings():
    if len(bookings) == 0:
        print("\nNo bookings found.")
        return

    print("\nBooking Records:")
    print("-" * 50)
    for index, booking in enumerate(bookings, start=1):
        print(f"{index}. Student ID : {booking['student_id']}")
        print(f"   Student    : {booking['student_name']}")
        print(f"   Equipment  : {booking['equipment']}")
        print(f"   Date       : {booking['date']}")
        print("-" * 50)


def search_bookings():
    search_term = input("Enter Student Name or Equipment Name to Search: ").strip()

    if search_term == "":
        print("\nError: Search term cannot be empty.")
        return

    found_bookings = []

    for booking in bookings:
        if (search_term.lower() in booking["student_name"].lower() or
                search_term.lower() in booking["equipment"].lower()):
            found_bookings.append(booking)

    if len(found_bookings) == 0:
        print(f"\nNo bookings found for '{search_term}'.")
        return

    print("\nMatching Booking Records:")
    print("-" * 50)
    for index, booking in enumerate(found_bookings, start=1):
        print(f"{index}. Student ID : {booking['student_id']}")
        print(f"   Student    : {booking['student_name']}")
        print(f"   Equipment  : {booking['equipment']}")
        print(f"   Date       : {booking['date']}")
        print("-" * 50)


def main():
    while True:
        display_menu()
        user_input = input("Please select an option: ").strip()

        if user_input == "1":
            view_students()
        elif user_input == "2":
            view_books()
        elif user_input == "3":
            view_equipment()
        elif user_input == "4":
            add_equipment()
        elif user_input == "5":
            search_equipment()
        elif user_input == "6":
            remove_equipment()
        elif user_input == "7":
            record_booking()
        elif user_input == "8":
            view_bookings()
        elif user_input == "9":
            search_bookings()
        elif user_input == "10":
            print("\nExiting Student Equipment Booking System. Goodbye.")
            break
        else:
            print("\nError: Please enter a valid option from 1 to 10.")


if __name__ == "__main__":
    main()