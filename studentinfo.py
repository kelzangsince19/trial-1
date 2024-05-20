students_list = []
students_dict = {}

# Adding a student
name = input("Enter student's name: ")
age = int(input("Enter student's age: "))
grade = int(input("Enter student's grade: "))

students_list.append(name)
students_dict[name] = {"age": age, "grade": grade}
print("Student list:", students_list)
print("Student dictionary:", students_dict)
print("Student's information added successfully")

# Searching for a student
search_name = input("Enter the name to search: ")
if search_name in students_list:
    print("Student found!", students_dict[search_name])
else:
    print("Student not found!")

# Removing a student
remove_name = input("Enter the name of the student to remove: ")
if remove_name in students_list:
    del students_dict[remove_name]
    students_list.remove(remove_name)
    print("Student removed successfully!")
    print("Updated student list:", students_list)
    print("Updated student dictionary:", students_dict)
else:
    print("Student not found!")