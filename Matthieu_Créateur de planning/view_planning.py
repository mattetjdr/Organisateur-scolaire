import json
import os

def run():
    print("\n--- VIEW PLANNING ---")
    # Regarder si planning exists
    if not os.path.exists("planning.json"):
        print("No planning file found. Please create a planning first using Option 1.")
        input("Press Enter to return to the main menu... ")
        return
    # Ouvrir le fichier planning.json
    try:
        with open("planning.json", "r", encoding="utf-8") as json_file:
            planning_data = json.load(json_file)
        except json.JSONDecodeError:
            print("Error reading the planning file.")
            input("Press Enter to return to the main menu... ")
            return
        # Montrer Sleep Schedule
        sleep = planning_data.get("sleep", {})
        print("\n🛌 Sleep Schedule:")
        print(f"  • Bed time:    {sleep.get('bed_time', 'N/A')}")
        print(f"  • Wakeup time: {sleep.get('wakeup_time', 'N/A')}")
        # Montrer Activités
        activities = planning_data.get("activities", [])
        print(f"\n Scheduled Activities ({len(activities)} total):")
        
        if not activities:
            print("No activities recorded yet.")
        else:
            for index, act in enumerate(activities, 1):
                print(f"  {index}. **{act.get('name')}** ({act.get('day')})")
                print(f"	 Time: {act.get('start time')} - {act.get('end time')} | Importance: {act.get('importance')}/5")
                
        input("\nPress Enter to return to the main menu... ")