import json


all_students = []

while True:
    print("\n------ Main Menu ------")
    print("Press 1 for Registration")
    print("Press 2 for Search & View Data")
    print("Press 3 for All Students Data")
    print("Press 4 for Search only")
    print("Press 5 for Exit")
    
    choice = input("Press Key function you want to use : ")
    user_input=int(choice)
    
    if user_input == 1:
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

    elif user_input == 2:
        student_id=input("Enter student Id -: ")
        student_name=input("Enter Student Name -: ")
        for data in all_students:
            if student_id == data["id"] and student_name==data["name"]:
                print("-------------Student Data ------------ ")
                print(json.dumps(data,indent=4))
        else:
            print("Student Data Not Found !")
        
    elif user_input == 3:
        print("\n---------------- ALL REGISTERED STUDENTS ------------------")
        
        for student in all_students:
            print(json.dumps(student,indent=4))
   
    elif user_input==4:
        check_id=input("Enter Id For Student Search : ")
        for id in all_students:
            if check_id==id["id"]:
                print("Valid Student")
            else:
                print("Not Found") 
             
    elif user_input==5:
        print("Exiting program...!")
        break
    
    else:
        print("Invalid input. Please try again.")
    
    



