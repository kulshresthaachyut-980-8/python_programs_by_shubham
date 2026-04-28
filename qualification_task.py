import json


all_students = []

while True:
    print("\n--- Main Menu ---")
    print("Press 1 for Registration")
    print("Press 2 for Exit")
    print("Press 3 to View All Students")
    
    inp_ut = input("Press Key function you want to use : ")
    
    if inp_ut == '1':
        print("\n---------------- REGISTER NEW STUDENT ------------------")
        
        student_record = {}
        
        student_record["id"] = input("Enter Student Id : ")
        student_record["name"] = input("Enter Student Name : ")
        student_record["city"] = input("Enter City Name : ")
        
        print("\n Enter Qualifications one by one.")
        print("example : 10th, 12th, Diploma, Bachelors, Masters")
        
        qualification_count = int(input("Enter The Qualification Count You Want to Enter : "))
        
        qualifications_list = []
        
        for count in range(qualification_count):
            print(f"\n--- Entering Qualification {count + 1} ---")
            
            edu_record = {} 
            edu_record["qualification_name"] = input("Enter Qualification Name: ")
            edu_record["Passing_Year"] = input("Enter Passing Year: ")
            
            qualifications_list.append(edu_record)
            
        student_record["Qualifications"] = qualifications_list
        
        all_students.append(student_record)
        
        print(f"\n Student {student_record['name']} successfully registered!")

    elif inp_ut == '2':
        print("Exiting program...!")
        break
        
    elif inp_ut == '3':
        print("\n---------------- ALL REGISTERED STUDENTS ------------------")
        
        for student in all_students:
            print(json.dumps(student,indent=4))
                
    else:
        print("Invalid input. Please try again.")
    
    



