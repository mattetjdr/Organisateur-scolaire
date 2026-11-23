import json
import os
import random
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
# Mini-game: Guess the number
def play_game():
    # 1. Choisir un nombre au hasard
    number_to_guess = random.randint(1, 1000)
    guess = -1
    abandon = False
    essais = 0

    while guess != number_to_guess:
        # 2.1 demander un nombre
        instruction = input("Entrez un nombre entre 1 et 1000 [q: quitter]: ")
        if not instruction.isnumeric():
            if instruction == "q":
                abandon = True
                break
            else:
                print("Instruction is invalid")
                continue
        guess = int(instruction)
        essais += 1
        if guess < number_to_guess:
            print("C'est plus")
        elif guess > number_to_guess:
            print("C'est moins")

    if abandon:
        print(f"Dommage,c'est quand tu veux pour avouer à Sasha , si tu cherche le nombre: le nombre était {number_to_guess} ")
    #ref de dev le "avouer a Sasha" c'est un easter egg
    else:
        print(f"Bravo, vous avez trouvé en {essais} essais! le nombre était {number_to_guess}")

# Main menu
def main():
    while True:
        print("\n" + "=" * 30)
        print("         STUDY PLANNER        ")
        print("=" * 30)
        print("1) Add subject")
        print("2) Show subjects")
        print("3) View subtasks")
        print("4) Modify subject")
        print("5) Delete a subject")
        print("6) Take a break (Play a game)")
        print("7) Quit")
        print("-" * 30)
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
            play_game()
        elif choice == 7:
            print("Are you sure?")
            answer = input("Yes or no? ").strip().lower()
            if answer == "yes":
                print("OK Bye!")
                break
            else:
                continue
        else:
            print("Invalid choice")

# Start the program
main()