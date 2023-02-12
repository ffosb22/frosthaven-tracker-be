from pony.orm import PrimaryKey, Required, Set

from .base import db


class Campaign(db.Entity):
    id = PrimaryKey(int, auto=True)
    party_name = Required(str)
    characters = Set("Character")
    game = Required(str)


class Character(db.Entity):
    id = PrimaryKey(int, auto=True)
    character_name = Required(str)
    character_class = Required("CharacterClass")
    campaign = Required('Campaign')
