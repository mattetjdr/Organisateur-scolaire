import runpy

while True:
    print("\n==============================")
    print("        MENU PRINCIPAL        ")
    print("==============================")
    print("1 - Lancer le programme de Alex")
    print("2 - Lancer le programme de Gerald")
    print("3 - Lancer le programme de Matthieu")
    print("0 - Quitter")
    print("==============================")
    
    choix = input("Votre choix : ")
    
    if choix == "1":
        runpy.run_path("Alex_To-do-list/main1.py")
    elif choix == "2":
        runpy.run_path("Gerald_Sous-taches/main2.py")
    elif choix == "3":
        runpy.run_path("Matthieu_Créateur de planning/main3.py")
    elif choix == "0":
        print("Au revoir !")
        break
    else:
        print("Choix invalide")
