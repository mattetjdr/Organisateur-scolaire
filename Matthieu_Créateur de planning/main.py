print("Hello, you're here to create your planning")
# 1. Sommeil
bed_time=input("At wich time do you want to sleep? Example 22:00")
wakeup_time=input("At wich time do you want to wake up? Example 07:00")
# 2. Activité fixes
importance = 0
while True:
    name_activity=input("What's the name of your class or activity? (Press 'q' to exit)")
    # 2.1 Sortie de l'encodage des activités
    if name_activity == "q":
        break
    # 2.2 Encodage infos importantes
    day=input("Day of the week : ")
    start_time=input("Time of start (HH:MM) : ")
    end_time=input("Ending time (HH:MM) : ")
    while True:
        importance = input("What's the importance from 1 to 5 : ")
        if importance not is.numeric():
            continue
        elif importance < 1 or importance > 5:
            print("Error, please repeat")
            continue
        else:
            break
    # 2.3 Sauvegarder infos
    activite = {
        "name": name_activity,
        "day": day,
        "start time": start_time,
        "end time": end_time
        "importance": importance
    }
    
    activites.append(activite)
    