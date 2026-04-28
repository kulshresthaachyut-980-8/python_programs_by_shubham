import json

main_list=[]

while True:
    
    employ_data={}
    print("=============================")
    print("  REGISTER EMPLOY      : '1' ")
    print("  SEARCH EMPLOY DATA   : '2' ")
    print("  VIEW EMPLOY DATA     : '3' ")
    print("  EXIT                 : '4' ")
    print("=============================")

    user_input=input(" Enter Your Choice: ")
    if len(user_input)==1 and user_input.isdigit():

        if user_input=='1':
            print("Wellcome to Employ registration Corner.")
            
            employ_data["NAME"]=input(" Enter Employ's Full Name: ")
            employ_data["ID"]=input(" Enter Employ ID: ")
            while True:
                employ_data["MOBILE"]=input(" Enter Employ's Mobile No. (10 Digits): ")
                if len(employ_data["MOBILE"])==10 and employ_data["MOBILE"].isdigit():
                    break
                else:
                    print("Invalid Mobile Number ")
            employ_data["Email ID"]=input(" Enter Employ's Email ID: ")


            post_are=["CEO","Manager","Assistant","Developer"]
            while True:
                employ_data["POST"]=input(" Enter Employ's Current Post: ")
                if employ_data["POST"] in post_are:
                    break

                for posts in post_are:
                    if posts.lower() == employ_data["POST"].lower():
                        break

                    else:
                         print("Post not Found")

                main_list.append(employ_data)

        elif user_input=='2':
            check_id=input("Enter Employ's ID ")
            for data_b in main_list:
                if check_id==data_b["ID"]:
                    print("\n He is a Valid Employ.")
                    break
            else:
                print(" Employ Data Not Found !")

        elif user_input=='3':
            check_name=input("Enter Employ's Name : ")
            check_email=input("Enter Employ's Email Id : ")
            for data_c in (main_list):
                if check_name==data_c["NAME"] and check_email==data_c["Email ID"]:
                    print("\n----------Employ Data------------ ")
                    print(json.dumps(data_c,indent=4)) #copy
                    break
            else:
                print("Employ Not Found") 

        elif user_input=='4':
            print("Exiting...")
            break
        else:
         print("Enter Valid Choice -> ('1','2','3' or '4')")   
    else:
        print("Only one Digit is valid !")