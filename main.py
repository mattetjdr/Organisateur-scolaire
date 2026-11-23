import os
import runpy
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
PROGRAMS = {
    "1": ("Alex_To-do-list", "main1.py", "Alex", "__main__"),
    "2": ("Gerald_Sous-taches", "main2.py", "Gerald", "__main__"),
    "3": ("Matthieu_Créateur de planning", "main3.py", "Matthieu", "__main3__"),
}


def launch_project(folder, filename, run_name):
    project_dir = ROOT / folder
    script_path = project_dir / filename
    previous_dir = Path.cwd()
    sys.path.insert(0, str(project_dir))
    try:
        os.chdir(project_dir)
        runpy.run_path(str(script_path), run_name=run_name)
    finally:
        os.chdir(previous_dir)
        sys.path.remove(str(project_dir))


def main():
    while True:
        print("\n=== Organisateur scolaire ===")
        for choice, (_, _, name, _) in PROGRAMS.items():
            print(f"{choice}. Lancer le programme de {name}")
        print("0. Quitter")

        choice = input("Votre choix : ").strip()
        if choice == "0":
            break
        if choice in PROGRAMS:
            folder, filename, _, run_name = PROGRAMS[choice]
            launch_project(folder, filename, run_name)
        else:
            print("Choix invalide.")


if __name__ == "__main__":
    main()
