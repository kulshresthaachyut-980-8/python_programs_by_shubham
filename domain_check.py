user_id_input = input("Enter Email Id - : ")

if "@" in user_id_input:

    email_parts = user_id_input.split("@")
    
    if len(email_parts) == 2: # it means Email has only 2 parts - user, domain. if any other part found [if==0]

        user_part = email_parts[0]  
        domain_part = email_parts[1] 
        
        print("\n--- Email Parts ---")
        print(f"Everything before @: {user_part}")
        print(f"Everything after @: {domain_part}")
        
    else:
        print("Invalid Email ")

else:
    print("Operator @ not Found!")