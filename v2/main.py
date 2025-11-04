from v2.typing_ import player_types
from .entitys import Monsters_types, Setup
import sys

print("teste")
monsters: Monsters_types = []
bosses = []
#player_01 = {"name": "Cris"}
player_01 = {
    "name": "cris",
    "max_hp": 100,
    "level": 1,
    "atk": 10,
    "damage": 0,
    "xp": 0,
    "attribute": {
        "for": 0,
        "vit": 0,
        "agi": 0
    },
    "adds": {
        "points": 0
    }
}
monsters = Setup.spawn_monsters(monsters)
def player_screen(entity: player_types): # type: ignore
    """Menu and others functions of player"""
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
        action = ACTIONS["player"].get(choice)

        if action:
            action()
        else:
            print("Opcao invalida")


def settings_screen():
    """game settings screen"""
    MENU_TEXT = "1. Load and Save \n2. Dificult \n5. Sair \n"
    while True:
        print(MENU_TEXT)
        choice = input(">>> ").strip()
        action = ACTIONS["settings"].get(choice)

        if action:
            action()
        else:
            print("Opcao invalida")


def main_menu():
    """main screen of game"""

    MENU_TEXT = (
        "--- Menu Principal ---\n\n"
        "1. Player \n"
        "2. Monsters \n"
        "3. Ajuda \n"
        "4. Settings \n"
        "5. sair \n"
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
    "main": {"1": lambda: player_screen(player_01), "5": sys.exit},
    "player": {"1": None},
    "settings": {"5": sys.exit},
}

main_menu()
