import UserMdule

# write a menu driven program to add user information and display all user information


print("Welcome to User Information system")
print("1. Add user information")
print("2. Display user information")
print("3. Exit")



while True:
    choice = int(input("Enter your choice:"))
    if choice == 1:
        user_id = int(input("Enter the user id:"))
        user_name = input("Enter user-name:")
        user_email = input("Enter user-email:")
        UserMdule.add_user_info(user_id,user_name,user_email)
        print("User information added successfully")
    elif choice == 2:
        all_user_info = UserMdule.get_all_user_info()
        print("All User Information:")
        for user_id,info in all_user_info.items():
            print(f"User ID: {user_id},Name: {info['user_name']}, Email:{info['user_email']}")
    elif choice == 3:
        print("Exiting the program")
        break
    else:
        print("Invalid choice. Please try again")
