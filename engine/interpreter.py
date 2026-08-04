from engine.utils import load_json
from engine.entities.player import Player
from engine.scenes.scenes import AnimScene,CutScene,FightScene, GameScene, DialogScene, ChoiceScene

scene_map = {
    "anim_scene": AnimScene,
    "cut_scene": CutScene,
    "fight_scene": FightScene,
    "game_scene": GameScene,
    "dialog_scene": DialogScene,
    "choice_scene": ChoiceScene,
}

class GameEngine:
    def __init__(self, start_file):
        start_data = load_json(start_file)
        self.current_file = start_file
        self.game_name = start_data["game_name"]
        self.game_developer = start_data["game_developer"]
        self.game_version = start_data["game_version"]
        print(self.game_name)
        print(self.game_developer)
        print(self.game_version)

    def launch(self):
        scene_data = load_json(self.current_file)
        start_scene = scene_data["start_scene"]
        print(start_scene)

