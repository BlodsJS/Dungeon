from entitys import setup
import sys
print("teste")
monsters = []
bosses = []
player_01 = {
    "name": "Cris"
}
#setup.spawn_monsters(monsters)

def player_screen(entity):
    """Menu and others functions of player """
    MENU_TEXT = (
        f"--- {entity['name']} Perfil ---\n\n"
        "1. Ver atributos\n"
        "2. Adicionar atributos\n"
        "3. Mochila\n"
        "4. Sair \n"
    )
    while True:
        print(MENU_TEXT)
        choice = input(">>> ").strip()
        action = ACTIONS["menu"].get(choice)
        
        if action:
            action()
        else:
            print("Opcao invalida")
    

def settings_screen():
    """game settings screen """
    pass

def main_menu():
    """main screen of game"""
    
    print("algo")

    MENU_TEXT = (
        "--- Menu Principal ---\n\n"
        "2. sair \n"
    )
    
    while True:
        print(MENU_TEXT)    
        choice = input(">>> ").strip()
        
        action = ACTIONS["main"].get(choice)
        
        if action:
            action()
        else:
            print("Opcao invalida")

ACTIONS = {
    "main": {
        "1": lambda: player_screen(player_01),
        "2": sys.exit
    },
    "menu": {
        "1": None
    }
}

main_menu()
