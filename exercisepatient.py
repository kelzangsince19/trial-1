from queue import Queue

# Initialize patient queue
patient_queue = Queue()

# Menu loop
while True:
    print("1. Register Patient")
    print("2. Remove Patient after Meeting Doctor")
    print("3. Display Patient Queue")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        # Register Patient
        name = input("Enter patient name: ")
        patient_queue.put(name)
        print("Patient", name, "registered.")
    elif choice == '2':
        # Remove Patient after Meeting Doctor
        if patient_queue.empty():
            print("No patients in the queue.")
        else:
            name = patient_queue.get()
            print("Patient", name, "removed after meeting the doctor.")
    elif choice == '3':
        # Display Patient Queue
        if patient_queue.empty():
            print("No patients in the queue.")
        else:
            print("Current patient queue:")
            for index, patient in enumerate(patient_queue.queue, start=1):
                print(f"{index}. {patient}")
    elif choice == '4':
        # Exit program
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")

