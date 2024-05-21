from queue import Queue
import sys

#initialized queue for storing patient names
patients = Queue()
current_patient = None


while True:
    print ("Desktop Manager - Patient Registeration and Appointment System\n")
    print("""
        1. Register the patient
        2. Remove the Patient
        3. Display the patient 
        4. Exit
        Enter your choice (Just enter the option number):
        """)
    userinput = input(">>> ")
    print()

    if userinput == "1":
        patient_name = input('Enter patient name:')
        patients.put(patient_name)
        current_patient = patient_name
        print(f"Patient {patient_name} successfully Registered\n")

    elif userinput == "2":
        patients.get()
        print (f"Patient {current_patient} removed after meeting the doctor.\n")

    elif userinput == "3":
        print("Current Patient Queue :")
        for i in patients.queue:
            print (i)

    elif userinput == "4":
        print("Exiting program")
        sys.exit()
    
    else:
        print("Invalid Input. Follow the instruction Well.\n\n")
