import json

print("Hello, you're here to create your planning")
# 1. Sommeil
bed_time=input("At wich time do you want to sleep? (Example 22:00) ")
wakeup_time=input("At wich time do you want to wake up? (Example 07:00) ")
# 2. Activité fixes
importance = 0
activites = []
while True:
    name_activity=input("What's the name of your class or activity? (Press 'q' to exit) ")
    # 2.1 Sortie de l'encodage des activités
    if name_activity.lower() == "q":
        break
    # 2.2 Encodage infos importantes
    day=input("Day of the week : ")
    start_time=input("Time of start (HH:MM) : ")
    end_time=input("Ending time (HH:MM) : ")
    while True:
        importance = input("What's the importance from 1 to 5 : ")
        if not importance.isnumeric():
            continue
        elif int(importance) < 1 or int(importance) > 5:
            print("Error, please enter a number between 1 and 5")
            continue
        else:
            break
    # 2.3 Sauvegarder infos
    activite = {
        "name": name_activity,
        "day": day,
        "start time": start_time,
        "end time": end_time,
        "importance": int(importance)
    }
    
    activites.append(activite)
    
# 3. Créer et sauvegarder le fichier JSON
planning_data = {
    "sleep": {
        "bed_time": bed_time,
        "wakeup_time": wakeup_time
    },
    "activities": activites
}

with open("planning.json", "w", encoding="utf-8") as json_file:
    json.dump(planning_data, json_file, indent=4, ensure_ascii=False)

def run():
    print("Planning generator started...")
    input("Planning complete! Press Enter to return to the main menu... ")