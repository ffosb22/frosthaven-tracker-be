from pony.orm import PrimaryKey, Required, Set

from .base import db


class CharacterClass(db.Entity):
    id = PrimaryKey(int, auto=True)
    class_name = Required(str, unique=True)
    ability_cards = Set('AbilityCard')
    num_cards = Required(int)
    from_game = Required(str)
    characters = Set('Character')


class AbilityCard(db.Entity):
    id = PrimaryKey(int, auto=True)
    ability_name = Required(str)
    character_class = Required(CharacterClass)
    ability_lvl = Required(int)

