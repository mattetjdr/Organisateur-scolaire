# An empty list to store all subjects
subjects: list[dict] = []
def generate_subtasks(difficulty: str) -> list[dict]:
    if difficulty == "Easy":
        return[
            {"task": "Relire le cours" , "duration": "15min"}]
# Add a subject to the list
def add_subject():
    # Ask for subject name
    name = input("What is your subject name? ").strip()
    if not name or name.isnumeric():
        print("Please enter a valid subject name.")
        return
    chapter=input("What is the chapter name? ")
    if not chapter:
        print("Please enter a valid chapter name")
        return
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
    subtasks = generate_subtasks(difficulty)
    # Create a dictionary for the subject
    subject = {
        "name": name,
        "chapter": chapter,
        "difficulty": difficulty,
        "task": subtasks
    }

    # Add the subject to the list
    subjects.append(subject)
    print("Subject,chapter and study plan added successfully!")


# Show all subjects, numbered from 1
def show_subjects():
    if len(subjects) == 0:
        print("No subjects yet")
        return
    number = 1
    for s in subjects:
        print(f"{number}) {s['name']} {s['chapter']} [{s['difficulty']}]")
        number = number + 1
    for t in s["task"]:
            print(f"   - {t['task']} ({t['duration']})")
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
def modify_subject():
    if len(subjects)==0:
        print("No subjects yet")
        return
    show_subjects()
    try:
        number_to_modify=int(input("Wich line do you want to modify? "))
    except ValueError:
        print("Please enter a number")
        return
    if number_to_modify < 1 or number_to_modify > len(subjects):
        print("Invalid choice")
        return
    new_name= input("Enter the new name: ")
    new_chapter = input("Enter the new chapter name: ").strip()
    if new_name:
        subjects[number_to_modify - 1]["name"] = new_name
    if new_chapter:
        subjects[number_to_modify - 1]["chapter"] = new_chapter
    print("Subject has been modified")
    # Main menu
def main():
    while True:
        print("""
1) Add subject
2) Show subjects
3) Delete a subject
4) Modify subject
5) Quit""")
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
        elif choice==4:
            modify_subject()
        elif choice == 5:
            print("Ok! bye!")
            break
        else:
            print("Invalid choice")


# Start the program
main()