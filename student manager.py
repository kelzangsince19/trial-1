#initialize empty list and a dictionary 
students_list = []
students_dict = {}
#add students infromation
name = input("Enter student's name: ")
age = input("Enter student's age: ")
grade = input("Enter student's grade: ")
students_list.append("name")
students_dict[name] = {"age": age, "grade": grade}
print("students information sucessfully added!")
#to search by students name
if name in students_list:
    print(f"student found! name: {students_dict [name]}")
    print(f"student found! Age: {students_dict[name]['age']}")
    print(f"student found! Grade: {students_dict[name]['grade']}")
else:
    print("student not found! ") 

#remove students info
remove_title  = input("enter the name of a student to remove or else enter to skip: ")
if remove_title in students_list:
    remove_name = students_dict[name]
    students_list.remove(name)
    del students_dict[name]
    print("students removed successfully!")
    print("students present: ", students_list)
    
else:
    print("students not found!")


    
    

           


