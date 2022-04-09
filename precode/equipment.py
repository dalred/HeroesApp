from dataclasses import dataclass
from typing import List

from base_data import Base_data


@dataclass
class Weapon:
    id: int
    name: str
    min_damage: float
    max_damage: float
    stamina_per_hit: float  # выносливость для удара


@dataclass
class Armor:
    id: int
    name: str
    defence: int
    stamina_per_turn: int #количество затраченной выносливости за защиту


@dataclass
class EquipmentData:
    weapons: List[Weapon]
    armors: List[Armor]


class Equipment(Base_data):
    """
    Класс отвечающий за снаряжения игрока
    """
    def get_weapon(self, weapon_name: str) -> Weapon:
        for item in self.data.weapons:
            if item.name == weapon_name:
                return item

    def get_armor(self, armor_name: str) -> Armor:
        for item in self.data.armors:
            if item.name == armor_name:
                return item

    @property
    def get_weapon_names(self) -> List:
        return [item.name for item in self.data.weapons]

    @property
    def get_armor_names(self) -> List:
        return [item.name for item in self.data.armors]
