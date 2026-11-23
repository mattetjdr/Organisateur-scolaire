import json
import os
FILE_NAME= "subjects.json"
def load_subjects() -> list[dict]:
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME,"r", encoding="utf-8") as f:
            return json.load(f)
    return[]
def save_subjects():
    with open(FILE_NAME,"w", encoding="utf-8") as f:
        json.dump(subjects,f, indent=4, ensure_ascii=False)
# An empty list to store all subjects
subjects: list[dict] = load_subjects()

def generate_subtasks(difficulty: str) -> list[dict]:
    if difficulty == "Easy":
        return [
            {"task": "Review class notes", "duration": "10 min"},
            {"task": "Define key terms", "duration": "10 min"}
        ]
    elif difficulty == "Medium":
        return [
            {"task": "Summarize main concepts", "duration": "15 min"},
            {"task": "Create flashcards for key terms", "duration": "15 min"},
            {"task": "Answer review questions", "duration": "15 min"}
        ]
    elif difficulty == "Hard":
        return [
            {"task": "Analyze core theories or arguments", "duration": "20 min"},
            {"task": "Write a structured personal summary", "duration": "20 min"},
            {"task": "Test knowledge with active recall", "duration": "20 min"}
        ]
    return []

# Add a subject to the list
def add_subject():
    name = input("What is your subject name? ").strip()
    if not name or name.isnumeric():
        print("Please enter a valid subject name.")
        return
    chapter = input("What is the chapter name? ").strip()
    if not chapter:
        print("Please enter a valid chapter name.")
        return

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

    subject = {
        "name": name,
        "chapter": chapter,
        "difficulty": difficulty,
        "task": subtasks
    }

    subjects.append(subject)
    save_subjects()
    print("Subject, chapter and task plan added successfully!")

# Show all subjects (simple view)
def show_subjects():
    if len(subjects) == 0:
        print("No subjects yet")
        return
    number = 1
    for s in subjects:
        print(f"{number}) {s['name']} - {s['chapter']} [{s['difficulty']}]")
        number = number + 1

# Show subjects with their subtasks (detailed view)
def show_subtasks():
    if len(subjects) == 0:
        print("No subjects yet")
        return
    number = 1
    for s in subjects:
        print(f"\n{number}) {s['name']} - {s['chapter']} [{s['difficulty']}]")
        print("   Study plan:")
        for t in s["task"]:
            print(f"     - {t['task']} ({t['duration']})")
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
    save_subjects()
    print(f"{removed['name']} deleted")

def modify_subject():
    if len(subjects) == 0:
        print("No subjects yet")
        return
    show_subjects()
    try:
        number_to_modify = int(input("Which line do you want to modify? "))
    except ValueError:
        print("Please enter a number")
        return
    if number_to_modify < 1 or number_to_modify > len(subjects):
        print("Invalid choice")
        return

    new_name = input("Enter the new name (leave blank to keep current): ").strip()
    new_chapter = input("Enter the new chapter name (leave blank to keep current): ").strip()

    if new_name:
        subjects[number_to_modify - 1]["name"] = new_name
    if new_chapter:
        subjects[number_to_modify - 1]["chapter"] = new_chapter
    save_subjects()
        
    print("Subject has been modified")

# Main menu
def main():
    while True:
        print("""
1) Add subject
2) Show subjects
3) View subtasks
4) Modify subject
5) Delete a subject
6) Quit""")
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
            show_subtasks()
        elif choice == 4:
            modify_subject()
        elif choice == 5:
            delete_subject()
        elif choice == 6:
            print("Are you sure?")
            answer=input("Yes or no? ").strip().lower()
            if answer == "yes":
                print("OK Bye!")
                break
            else:
                continue
        else:
            print("Invalid choice")

# Start the program
main()