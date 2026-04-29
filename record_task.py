import json

main_list=[]

while True:
    
    employee_data={}
    print("=============================")
    print("  REGISTER EMPLOYEE    : '1' ")
    print("  SEARCH EMPLOYEE DATA : '2' ")
    print("  VIEW EMPLOYEE DATA   : '3' ")
    print("  EXIT                 : '4' ")
    print("=============================")

    user_input=(input(" Enter Your Choice: "))
    choice=int(user_input)
    
    
    if choice==1:
        print("Welcome to Employee registration Corner.")
            
        employee_data["name"]=input(" Enter Employee's Full Name: ")
        employee_data["id"]=input(" Enter Employee ID: ")
        while True:
            employee_data["mobile"]=input(" Enter Employee's Mobile No. (10 Digits): ")
            if len(employee_data["mobile"])==10 and employee_data["mobile"].isdigit():
                break
            else:
                print("Invalid Mobile Number ")
        employee_data["email_id"]=input(" Enter Employee's Email ID: ")

        roles_are=["CEO","Manager","Assistant","Developer"]
        while True:
            employee_data["role"]=input(" Enter Employee's Current Post: ")
            if employee_data["role"] in roles_are:
                break
            else:
                 print("Post not Found")

        main_list.append(employee_data)
        print("Employee Registerd Successfully.")

    elif choice==2:
        check_id=input("Enter Employee's ID ")
        for data_b in main_list:
            if check_id==data_b["id"]:
                print("\n He is a Valid Employee.")
                break
        else:
            print(" Employee Data Not Found !")

    elif choice==3:
        check_name=input("Enter Employee's Name : ").lower()
        check_email=input("Enter Employee's Email Id : ").lower()
        for data_c in (main_list):
            saved_data_name=data_c["name"].lower()
            saved_data_email=data_c["email_id"].lower()

            if check_name==saved_data_name and check_email==saved_data_email:
                print("\n----------Employee Data------------ ")
                print(json.dumps(data_c,indent=4)) #copy
                break
        else:
            print("Employee Not Found") 

    elif choice==4:
        print("Exiting...")
        break
    else:
        print("Enter Valid Choice -> ('1','2','3' or '4')")   
   