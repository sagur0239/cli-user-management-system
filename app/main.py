from app.services import *
from app.utils import clear_screen, pause

def menu():
    while True:
        clear_screen()

        print("==== USER MANAGEMENT SYSTEM ====")
        print("1. Create User")
        print("2. Show Users")
        print("3. Update User")
        print("4. Delete User")
        print("5. Search User")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            user = create_user(name, age)
            print("✅ Created:", user)

        elif choice == "2":
            users = get_users()
            for u in users:
                print(u)

        elif choice == "3":
            uid = int(input("Enter ID: "))
            new_name = input("New name: ")
            if update_user(uid, new_name):
                print("✅ Updated")
            else:
                print("❌ Not found")

        elif choice == "4":
            uid = int(input("Enter ID: "))
            if delete_user(uid):
                print("✅ Deleted")
            else:
                print("❌ Not found")

        elif choice == "5":
            keyword = input("Search: ")
            results = search_user(keyword)
            for r in results:
                print(r)

        elif choice == "6":
            print("Goodbye 👋")
            break

        else:
            print("❌ Invalid choice")

        pause()