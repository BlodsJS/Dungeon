import random

class setup():
    def spawn_monsters(monsters: dict) -> dict: 
        """Set monster to game"""
        monsters.clear()
        
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
        for i in range(100):
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

        return monsters
        
    def spawn_boss(bosses: dict) -> dict:
        """spawn version boss """
        bosses.clear()
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
        for i in range(100):
            name = random.choice(names)
            level = random.randint.randint(1, 100)
            mob = {
                "name": name,
                "max_hp": int(100*(i+1)*0.5+50),
                "level": level,
                "atk": int(i/0.5+3),
                "damage": 0,
                "xp": 0,
                "attribute": {
                    "for": random.randint(1, level),
                    "vit": random.randint(1, level),
                    "agi": random.randint(1, level)
                }
            }
            bosses.append(mob)

        return bosses
