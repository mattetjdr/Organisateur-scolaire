# An empty list to store all subjects
subjects: list[dict] = []


# Add a subject to the list
def add_subject():
    # Ask for subject name
    name = input("What is your subject name?: ")

    # Difficulty options
    print("""Choose the difficulty:
1) Easy
2) Medium
3) Hard""")
    try:
        choice = int(input("Your choice: "))
    except ValueError:
        print("Please enter a number.")
        return

    if choice == 1:
        difficulty = "Easy"
    elif choice == 2:
        difficulty = "Medium"
    elif choice == 3:
        difficulty = "Hard"
    else:
        print("Invalid choice")
        return

    # Create a dictionary for the subject
    subject = {
        "name": name,
        "difficulty": difficulty
    }

    # Add the subject to the list
    subjects.append(subject)
    print("Subject added successfully!")


# Show all subjects, numbered from 1
def show_subjects():
    if len(subjects) == 0:
        print("No subjects yet")
        return
    number = 1
    for s in subjects:
        print(f"{number}) {s['name']} [{s['difficulty']}]")
        number = number + 1


# Delete a subject chosen by its number
def delete_subject():
    if len(subjects) == 0:
        print("No subjects yet")
        return

    show_subjects()
    try:
        number = int(input("Subject number to delete: "))
    except ValueError:
        print("Please enter a number")
        return

    if number < 1 or number > len(subjects):
        print("Invalid choice")
        return

    removed = subjects.pop(number - 1)
    print(f"{removed['name']} deleted")


# Main menu
def main():
    while True:
        print("""
1) Add subject
2) Show subjects
3) Delete a subject
4) Quit""")
        try:
            choice = int(input("Your choice: "))
        except ValueError:
            print("Please enter a number")
            continue

        if choice == 1:
            add_subject()
        elif choice == 2:
            show_subjects()
        elif choice == 3:
            delete_subject()
        elif choice == 4:
            print("Ok! bye!")
            break
        else:
            print("Invalid choice")


# Start the program
main()