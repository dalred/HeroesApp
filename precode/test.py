
from abc import ABC
from typing import List

import marshmallow
import marshmallow_dataclass

from helpers.functions import read_json
from skills import Skill, Skill_data


class Base_data(ABC):
    def __init__(self, data: dict, object_dataclass) -> None:
        self.data = self.__get_data(data, object_dataclass)

    def __get_data(self, data: dict, object_dataclass):
        try:
            schema = marshmallow_dataclass.class_schema(object_dataclass)
            return schema().load(data)
        except marshmallow.exceptions.ValidationError:
            raise ValueError


class test_skill(Base_data):
    def get_skill(self, skill_name: str) -> Skill:
        for item in self.data.skill_names:
            if item.name == skill_name:
                return item

    @property
    def get_skill_names(self) -> List:
        return [item.name for item in self.data.skill_names]



data_skill: dict = read_json('data/skills.json')
skills = test_skill(data_skill, Skill_data)
print(skills.get_skill('Powerful thrust'))
