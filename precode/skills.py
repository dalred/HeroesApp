from dataclasses import dataclass
from typing import List
from base_data import Base_data


@dataclass
class Skill:
    name: str
    damage: int
    stamina_per_use: int


@dataclass
class Skill_data:
    skill_names: List[Skill]



class All_skill(Base_data):
    """
        Класс отвечающий за умения игрока
    """
    def get_skill(self, skill_name: str) -> Skill:
        for item in self.data.skill_names:
            if item.name == skill_name:
                return item

    @property
    def get_skill_names(self) -> List:
        return [item.name for item in self.data.skill_names]