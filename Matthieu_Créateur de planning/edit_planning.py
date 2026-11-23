import json
import os

PLANNING_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "planning.json")

def run():
#1 Trouver et ouvrir planning.json
    #1.1 Pas de planning qui existe
    if not os.path.exists("planning.json"):
        print("No planning exists! Please create one with Option 1 before coming here.")
        input("Press Enter to return to the main menu... ")
        return
    #1.2 Ouvrir le fichier
    try:
        with open(PLANNING_FILE, "r", encoding="utf-8") as json_file:
            planning_data = json.load(json_file)
    #1.3 Erreur dans l'ouverture d'un fichier
    except json.JSONDecodeError:
        print("Error reading the planning file.")
        input("Press Enter to return to the main menu... ")
        return
#2 Modifier le planning
    while True:
        #2.1 Editing menu
        print("\n" + "=" * 35)
        print("        EDITING MENU")
        print("=" * 35)
        print("1. Change your sleep schedule")
        print("2. Add an activity")
        print("3. Remove an activity")
        print("4. Return to the main menu")
        print("=" * 35)

        choice = input("Choose an option (1-4): ")
        #2.2 Modifying sleep schedule
        if choice == "1":
            sleep_data = planning_data.setdefault("sleep", {})
            current_bed_time = sleep_data.get("bed_time", "")
            current_wakeup_time = sleep_data.get("wakeup_time", "")
            new_bed_time = input(f"What's you're new bed time. (You're current bed time is {bed_time})")
            if new_bed_time == "":
                bed_time = current_bed_time
            else:
                bed_time = new_bed_time
            new_wakeup_time = input(f"What's you're new wake up time? (You're current wake up time is {wakeup_time})")
            if new_wakeup_time == "":
                wakeup_time = current_wakeup_time
            else:
                wakeup_time = new_wakeup_time
            
            sleep_data["bed_time"] = bed_time
            sleep_data["wakeup_time"] = wakeup_time
            
            with open(PLANNING_FILE, "w", encoding="utf-8") as json_file:
                json.dump(planning_data, json_file, indent=4, ensure_ascii=False)
        elif choice == "2":
            day=input("Day of the week : ")
            start_time=input("Time of start (HH:MM) : ")
            end_time=input("Ending time (HH:MM) : ")
            while True:
                importance = input("What's the importance from 1 to 5 : ")
                if not importance.isnumeric():
                    print("Error, please enter a number between 1 and 5")
                    continue
                elif int(importance) < 1 or int(importance) > 5:
                    print("Error, please enter a number between 1 and 5")
                    continue
                else:
                    break
            activities = planning_data.setdefault("activities", [])
            activite = {
                "name": name_activity,
                "day": day,
                "start time": start_time,
                "end time": end_time,
                "importance": int(importance)
            }
    
            activities.append(activite)
            
            with open(PLANNING_FILE, "w", encoding="utf-8") as json_file:
                json.dump(planning_data, json_file, indent=4, ensure_ascii=False)
            
            print("Activity saved")
        elif choice == "3":
            activities = planning_data.get("activities", [])

            if not activities:
                print("\nNo activities to remove.")
                continue

            print("\nSelect an activity to remove (or 0 to cancel):")
            for idx, act in enumerate(activities, 1):
                print(f"  {idx}. {act.get('name')} ({act.get('day')}, {act.get('start time')} - {act.get('end time')})")

            raw_choice = input("Enter activity number: ").strip()
            if not raw_choice.isdigit():
                print("Please enter a valid number.")
                continue

            activity_num = int(raw_choice)
            if activity_num == 0:
                print("Removal cancelled.")
                continue

            if not (1 <= activity_num <= len(activities)):
                print(f"Please choose a number between 1 and {len(activities)}.")
                continue

            removed = activities.pop(activity_num - 1)

            with open(PLANNING_FILE, "w", encoding="utf-8") as json_file:
                json.dump(planning_data, json_file, indent=4, ensure_ascii=False)

            print(f"Removed '{removed.get('name')}' and saved planning.")
        elif choice == "4":
            return
        else:
            print("Invalid choice, please enter a number between 1 and 4!")