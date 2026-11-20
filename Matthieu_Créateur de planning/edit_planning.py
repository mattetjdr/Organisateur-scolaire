import json
import os

PLANNING_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "planning.json")

def run():
    if not os.path.exists("planning.json"):
        print("No planning exists! Please create one with Option 1 before coming here.")
        input("Press Enter to return to the main menu... ")
        return
    