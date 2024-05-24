def add_student(students_list, students_dict):
    name = input("Enter student's name: ")
    age = input("Enter student's age: ")
    grade = input("Enter student's grade: ")
    students_list.append(name)
    students_dict[name] = {'age': age, 'grade': grade}
    print(f"Student {name} added successfully")
    print(f"Current student details: {students_dict}")

def search_student(students_dict):
    name = input("Enter the name of the student to search: ")
    if name in students_dict:
        print(f"Student found: Name: {name}, Age: {students_dict[name]['age']}, Grade: {students_dict[name]['grade']}")
    else:
        print("Student not found")

def remove_student(students_list, students_dict):
    name = input("Enter the name of the student to remove: ")
    if name in students_list:
        students_list.remove(name)
        students_dict.pop(name, None)
        print(f"Student {name} removed successfully")
        print(f"Current student details: {students_dict}")
    else:
        print("Student not found")

def main():
    students_list = []
    students_dict = {}

    while True:
        print("\nStudent Information Management System Menu:")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Remove Student")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_student(students_list, students_dict)
        elif choice == '2':
            search_student(students_dict)
        elif choice == '3':
            remove_student(students_list, students_dict)
        elif choice == '4':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
