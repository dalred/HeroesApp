from abc import ABC
from typing import Any

import marshmallow
import marshmallow_dataclass


class Base_data(ABC):
    def __init__(self, data: dict, object_dataclass: Any) -> None:
        self.data = self.__get_data(data, object_dataclass)

    def __get_data(self, data: dict, object_dataclass):
        try:
            schema = marshmallow_dataclass.class_schema(object_dataclass)
            return schema().load(data)
        except marshmallow.exceptions.ValidationError:
            raise ValueError
