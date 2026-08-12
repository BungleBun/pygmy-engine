import json
import os

from engine.blocks.blocks import *
from engine.entities.player import *

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_json(path):
    with open(path, 'r') as f:
        return json.load(f)

type_registry = {
    'anim_block': AnimBlock,
    'cutscene_block': CutsceneBlock,
    'fight_block': FightBlock,
    'game_block': GameBlock,
    'dialog_block': DialogBlock,
    'choice_block': ChoiceBlock,
    'inventory_block': InventoryBlock,
    'shop_block': ShopBlock,
    'start_block': StartBlock,
    'menu_block': MenuBlock,
    'credits_block': CreditsBlock,

    'player': Player,
    'enemy': Enemy,

}

def load_file_type(path):
    data = load_json(path)
    file_type = data.get('file_type')

    if not file_type:
        raise ValueError(f"The file {path} does not have a file_type.")

    type_reg = type_registry.get(file_type)

    if not type_reg:
        raise ValueError(f"Unknown file type: {file_type} found in {path}.")

    return type_reg(data)

