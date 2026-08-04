import time
from engine.utils import clear_terminal
from engine.entities.enemy import Enemy
from engine.scenes.base_scene import Scene

class AnimScene(Scene):
    def run(self):
        print("Running anim scene")

class CutScene(Scene):
    def run(self):
        pass

class FightScene(Scene):
    def run(self):
        pass

class GameScene(Scene):
    def run(self):
        pass

class DialogScene(Scene):
    def run(self):
        pass

class ChoiceScene(Scene):
    def run(self):
        pass