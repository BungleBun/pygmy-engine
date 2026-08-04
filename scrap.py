import json

with open("data/main.json", "r") as f:
    data = json.load(f)

class Player:
    def __init__(self, name, health):
        self.name = name
        self.health = health

player = Player(**data)

print(player.name)

class GameEngine:
    def __init__(self):
        self.scenes = {
            "anim_scene": AnimScene,
            "cut_scene": CutScene,
            "fight_scene": FightScene,
            "game_scene": GameScene,
            "dialog_scene": DialogScene,
            "choice_scene": ChoiceScene
        }

