from app.services import *
import os

def clear():
    os.system('clear')

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except:
            print("❌ Enter valid number")

def menu():
    while True:
        print("\n==== USER MANAGEMENT SYSTEM ====")
        print("1. Create User")
        print("2. Show Users")
        print("3. Update User")
        print("4. Delete User")
        print("5. Search User")
        print("6. Exit")

        choice = input("Enter choice: ")

        try:
            if choice == "1":
                name = input("Name: ")
                age = get_int("Age: ")
                user = create_user(name, age)
                print("✅ Created:", user)

            elif choice == "2":
                users = get_all_users()
                if not users:
                    print("❌ No users found")
                else:
                    for u in users:
                        print(u)

            elif choice == "3":
                uid = get_int("User ID: ")
                name = input("New Name: ")
                age = get_int("New Age: ")
                result = update_user(uid, name, age)
                print("✅ Updated:", result if result else "❌ Not found")

            elif choice == "4":
                uid = get_int("User ID: ")
                print("✅ Deleted" if delete_user(uid) else "❌ Not found")

            elif choice == "5":
                name = input("Search Name: ")
                result = search_user(name)
                if result:
                    for u in result:
                        print(u)
                else:
                    print("❌ No user found")

            elif choice == "6":
                print("Goodbye 👋")
                break

            else:
                print("❌ Invalid choice")

        except Exception as e:
            print("⚠️ Error:", e)

        input("\nPress Enter...")
        clear()