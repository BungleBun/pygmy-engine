import time
from engine.utils import clear_terminal
from engine.entities.enemy import Enemy
from engine.blocks.base_block import Block

class AnimBlock(Block):
    def run(self):
        print("Running anim scene")

class CutsceneBlock(Block):
    def run(self):
        pass

class FightBlock(Block):
    def run(self):
        pass

class GameBlock(Block):
    def run(self):
        pass

class DialogBlock(Block):
    def run(self):
        pass

class ChoiceBlock(Block):
    def run(self):
        pass

class InventoryBlock(Block):
    def run(self):
        pass

class ShopBlock(Block):
    def run(self):
        pass

class StartBlock(Block):
    def run(self):
        pass

class MenuBlock(Block):
    def run(self):
        pass

class CreditsBlock(Block):
    def run(self):
        pass