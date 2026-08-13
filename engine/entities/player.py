from engine import Entity
from engine import load_json

class Player(Entity):
    def __init__(self):
        player_data = load_json('data/player/player.json')