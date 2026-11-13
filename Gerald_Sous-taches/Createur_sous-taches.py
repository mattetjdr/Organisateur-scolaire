
# 1. An empty list to store all subjects
subjects: list[dict] = []


# 2. Add the possibility to add a subject
def add_subject():

    # Ask for subject name
    name = input("What is your subject name?: ")

    # Difficulty options
    print("""Choose the difficulty:
1) Easy
2) Medium
3) Hard""")

    choice = int(input("Your choice: "))

    # Check the difficulty
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
add_subject()
def show_subjects():
    if len(subjects)==0:
        print("Subject not found")
        return
for s in subjects:
    print(s)
show_subjects()
    
