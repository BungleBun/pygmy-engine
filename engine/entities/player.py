from engine.entities.entity import Entity
from engine.utils import load_json

class Player(Entity):
    def __init__(self):
        player_data = load_json('data/player/player.json')