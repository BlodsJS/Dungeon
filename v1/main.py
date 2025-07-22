
import time
import random
import sys

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
    },
    "equip": {
        "weapon": None,
        "armor": None
    }

}

# __________________ Monsters methods ________________________

monsters = []
def spawm_monsters(monsters):
    """Set monster to game"""
    monsters.clear()
    
    for i in range(100):
        names = [
            "Slime",
            "Wolf",
            "Orc",
            "Goblin",
            "Troll",
            "Banshee",
            "Dragão",
            "Quimera",
            "Fênix",
            "grifo",
            "Basilisco",
            "Kraken",
            "Hidra",
            "Mantícora",
            "Leviatã",
            "Górgona",
            "Minotauro",
            "Lich",
            "Harpia",
            "Serpente Marinha",
            "Elemental",
            "Djinn",
            "Salamandra",
            "Cérbero",
            "Nosferatus",
            "Cavaleiro negro",
            "Naenia"
            
        ]
        name = random.choice(names)
        mob = {
            "name": name,
            "max_hp": int(100*(i+1)*0.5+50),
            "level": i+1,
            "atk": int(i/0.5+3),
            "damage": 0,
            "xp": 0,
            "attribute": {
                "for": 0,
                "vit": 0,
                "agi": 0
            }
        }
        monsters.append(mob)

def get_monster(monsters: list):
    """get the new monster in list"""
    for i in monsters:
        if i["damage"] < i["max_hp"]:
            return i
    return None

# ____________________ stats methods ________________________

def format_stats(entity: dict):  # lógica
    """better format stats """
    
    if entity == None:
        return None
    hp_max = entity["max_hp"] + entity["attribute"]["vit"]*5
    return {
        "name": entity["name"],
        "hp_current": hp_max - entity["damage"],
        "hp_max": hp_max,
        "atk": entity["atk"] + entity["attribute"]["for"]*3,
        "level": entity["level"]
    }

def show_entity(stats: dict):    # exibição
    """Use to show player or enemy or anything"""
    if stats == None:
        print("Todos os monstros foram derrotados")
        return
    print(
        f'Nome: {stats["name"]}\n'
        f'Level: {stats["level"]}\n'
        f'HP:  {stats["hp_current"]:,}/{stats["hp_max"]:,}\n'
        f'ATK: {stats["atk"]}\n'
    )

#___ Only player____

def heal(entity: dict):
    """heal a entity"""
    
    entity["damage"] = 0

def level_up(entity: dict, value: int):
    """add xp and level a entity"""

    entity["xp"] += value
    if entity["xp"] >= entity["level"]*100:
        entity["level"] +=1
        entity["xp"] -= entity["level"]*100
        entity["max_hp"] += 5
        entity["adds"]["points"] += 6
        
        print("\n\nNOTIFICAÇÃO DO MUNDO...\n")
        time.sleep(1)
        
        print(f"{entity['name']} atingiu um novo patamar,"
        f"chegando no level {entity['level']}\n\n")

def screen_attributes(entity: dict):
    """show attributes of player"""
    
    print(
        f"FOR: {entity['attribute']['for']}\n"
        f"AGI: {entity['attribute']['agi']}\n"
        f"VIT: {entity['attribute']['vit']}\n\n"
        f"pontos para adicionar: {entity['adds']['points']}\n"
    )

def add_point(entity: dict):

    field = input("O que deseja adicionar?\n>>> ").strip()
    
    if field.lower() not in ["for", "agi", "vit"]:
        print("Atributo não permitido")
        return
    value = int(input("Valor:\n>>> ").strip())
    if value > entity["adds"]["points"]:
        print(f"Você só tem {entity['adds']['points']}")
        return

    entity["attribute"][field] += value
    entity["adds"]["points"] -= value
    print(f"{value} pontos foram adicionador ao status de {field}")
  
#_______________ Battle methods _________________

def battle(entity: dict, enemy: dict):
    """simple battle method"""
    
    enemy["damage"] += entity["atk"]

def battle_loop(entity: dict, enemy: dict):
    """battle method"""
    hp_entity = entity["max_hp"] + entity["attribute"]["vit"]*5
    round = 1
    atk_entity = entity["atk"] + entity["attribute"]["for"] *3
    atk_enemy = enemy["atk"] + enemy["attribute"]["for"]*3
    hp_entity = entity["max_hp"] + entity["attribute"]["vit"] *5
    hp_enemy = enemy["max_hp"] + enemy["attribute"]["vit"] *5
    while entity["damage"] < hp_entity and enemy["damage"] < hp_enemy:
        print(f"--- Turno {round} ---")
        
        time.sleep(1)
        print(f'{entity["name"]} ataca {enemy["name"]} causando {atk_entity} de dano.')
        print(f'{enemy["name"]} ataca {entity["name"]} causando {atk_enemy} de dano.\n')

        enemy["damage"] += atk_entity
        entity["damage"] += atk_enemy
        time.sleep(0.5)

        print(f'{entity["name"]}: {hp_entity - entity["damage"]} HP restante.')
        print(f'{enemy["name"]}: {hp_enemy - enemy["damage"]} HP restante.\n')
        round += 1
        time.sleep(0.5)
        
    if entity["damage"] >= hp_entity and enemy["damage"] >= hp_enemy:
        print("💀 Ambos caíram ao mesmo tempo. Empate mortal!\n")
        entity["damage"] = hp_entity  # força a morte do player
        return "draw"
    
    if entity["damage"] >= hp_entity:
        print("Você lutou bravamente até o final,"
        "tendo uma morte honrosa em batalha...\n"
        "Os céus lembrarão de sua glória!!")
    else:
        level_up(entity, enemy["level"]*14)

    print("⚔️  Fim da batalha!")
    winner = entity if entity["damage"] <= hp_entity else enemy
    print(f"🏆 Vencedor: {winner['name']}\n\n")

def endless_battle(player: dict, monsters: list):
    """infinite mode"""
    spawm_monsters(monsters)
    
    for mob in monsters:
        print(f"\n🌑 Um novo inimigo aparece: {mob['name']}!\n")

        result = battle_loop(player, mob)

        if result == "draw" or player["damage"] >= player["max_hp"]+player["attribute"]["vit"]*5:
            print("☠️ Você foi derrotado.")
            return
        print("✨ Vitória! Você respira fundo e avança...\n")

        input("Pressione qualquer tecla para prosseguir \n>>> ")
        
    print("🎉 Parabéns! Você derrotou todos os inimigos.")
    for mob in monsters:
        mob["damage"] = 0    
#_____________Menu methods _________________
ACTIONS = {
    "1": lambda: show_entity(format_stats(player_01)),
    "2": lambda: show_entity(format_stats(get_monster(monsters))),
    "3": lambda: battle_loop(player_01, get_monster(monsters)),
    "4": lambda: endless_battle(player_01, monsters),
    "5": lambda: heal(player_01),
    "6": lambda: spawm_monsters(monsters),
    "7": lambda: player_menu(player_01),
    "8": lambda: sys.exit(),
    "stats": {
        "1": lambda: screen_attributes(player_01),
        "2": lambda: add_point(player_01)
    }
    
}

def player_menu(entity: dict):

    print(f"Perfil de {entity['name']}\n\n")
    screen_attributes(entity)
    MENU_TEXT = (
        "\n··· Menu de Ações ···\n"
        "1. Ver atributos\n"
        "2. Adicionar atributos\n"
        "5. Sair"
    )

    while True:
        print(MENU_TEXT)
        choice = input(">>> ").strip()
        action = ACTIONS["stats"].get(choice)

        if choice == "5":
            break
            
        if action:
            action()
        else:
            print("Opção inválida")
            
def main_menu():
    """main menu
    Use by control interection of player"""
    
    MENU_TEXT = (
        "··· Menu de Ações ···\n"
        "1. Ver jogador\n"
        "2. Ver monstro\n"
        "3. Iniciar batalha\n"
        "4. Modo infinito\n"
        "5. Curar\n"
        "6. Resetar monstros\n"
        "7. perfil\n"
        "8. Sair \n"
    )

    while True:
        print(MENU_TEXT)
        choice = input(">>> ").strip()

        action = ACTIONS.get(choice)

        if action:
            action()  # chama a função correspondente
        else:
            print("Opção inválida.\n")

spawm_monsters(monsters)
main_menu()
