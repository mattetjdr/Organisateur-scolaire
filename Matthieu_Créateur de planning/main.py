import create_planning
import view_planning
import edit_planning

def main.menu():
    while True:
        print("\n" + "=" * 35)
        print("       PLANNING MAIN MENU")
        print("=" * 35)
        print("1. Create or replace a planning")
        print("2. View existing planning")
        print("3. Modify existing planning")
        print("4. Exit")
        print("=" * 35)

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            create_planning.run()
        elif choice == "2":
            view_planning.run()
        elif choice == "3":
            edit_planning.run()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please enter a number from 1 to 4.")

if __name__ == "__main__":
    main_menu()