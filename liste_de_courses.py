import sys
_list = []
actions = [
    "Ajouter un élément à la liste",
    "Retirer un élément de la liste",
    "Afficher la liste",
    "Vider la liste",
    "Quitter",
]
number_of_actions = len(actions)

print(f"Choisissez parmi les {number_of_actions} options suivantes :")

while True:
    for i, action in enumerate(actions, 1):
        print(f"{i}.{action}")

    user_input = input("👉 Votre choix : ")

    if not (user_input.isdigit() and int(user_input) in range(1, number_of_actions + 1)):
        print("*" * 50)
        print(
            f"Veillez choisir parmi les {number_of_actions} options suivantes :")
        continue

    user_input = int(user_input)
    if user_input == 1:
        element = input(
            "Entrez le nom d'un élément a jouter a la liste de courses : ")
        _list.append(element)
        print(f"L'élément {element} a bien été ajouter a la liste.")
    elif user_input == 2:
        element = input(
            "Entrez le nom d'un élément a retirer a la liste de courses : ")
        if element in _list:
            _list.remove(element)
            print(
                f"L'élément {element} a bien été retire a la liste de courses.")
        else:
            print(
                f"L'élément {element} n'est pas dans la liste de courses.")
    elif user_input == 3:
        if not _list:
            print("Votre liste ne contient aucune élément.")
        else:
            print("Voici le contenu de la liste.")
            for i, element in enumerate(_list, 1):
                print(f"{i}. {element}")
    elif user_input == 4:
        _list.clear()
        print("Votre liste a bien été vider.")
    elif user_input == 5:
        print("Au revoir...")
        sys.exit()

    print("*" * 50)
    print(f"Choisissez parmi les {number_of_actions} options suivantes :")
