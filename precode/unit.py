from abc import ABC, abstractmethod
import random
from typing import Union, Optional, Tuple

from equipment import Weapon, Armor
from skills import Skill


class BaseUnit(ABC):
    """
        абстрактный класс BaseUnit
    """
    STAMINA_RECOVERY = 1  # константа (базовое восстановление выносливости за ход)

    def __init__(self, name_unit: str, max_health=100, max_stamina=100,
                 weapon: Optional[Weapon] = None,
                 skill: Optional[Skill] = None,
                 armor: Optional[Armor] = None,
                 mod_stamina: Union[int, float] = 0.9,
                 name: str = None,
                 attack=1,
                 defence=1) -> None:
        self.name_unit = name_unit  # класс игрока
        self.name = name  # Имя игрока
        self.health = max_health  # Текущеее здоровье
        self.weapon = weapon  # Текущеее оружие
        self.armor = armor  # Текущеее защита
        self.skill = skill  # Текущий навык
        self.mod_attack = attack  # модификатор атаки
        self.mod_defence = defence  # модификатор защиты
        self.skill_used = False  # Использованы ли умения
        self.stamina = max_stamina  # Текущая выносливость
        self.max_stamina = max_stamina  # максимальное количество выносливости
        self.max_health = max_health  # максимальное количество здоровья
        self.mod_stamina = mod_stamina  # модификатор выносливости класса

    @abstractmethod
    def strike(self, unit: 'BaseUnit') -> str:
        pass

    def equip_weapon(self, weapon: Weapon) -> None:
        self.weapon = weapon

    def set_skill(self, skill: Skill) -> None:
        self.skill = skill

    def equip_armor(self, armor: Armor) -> None:
        self.armor = armor

    @property
    def stamina_ponts(self):
        return round(self.stamina, 2)

    @property
    def health_ponts(self):
        return round(self.health, 2)

    # Защита
    def defence(self, unit: 'BaseUnit', damage: Union[int, float]) -> str:
        defence = 0
        if self.armor:
            if self.stamina >= self.armor.stamina_per_turn:
                self.stamina -= self.armor.stamina_per_turn
                defence = self.armor.defence * self.mod_defence
        if defence < damage:
            self.health -= damage - defence
            result_str = f'{unit.name}: Наношу общий урон оружием {unit.weapon.name} равный {damage:.2f}!'
        else:
            result_str = f'{unit.name}, используя {unit.weapon.name}, наносит удар равный {damage:.2f}, но {self.armor.name} соперника его останавливает.'
        return result_str

    # восстановление за ход
    @property
    def stamina_recovery(self) -> Union[float, int]:
        return self.STAMINA_RECOVERY * self.mod_stamina

    # Общая цифра восстановления после хода
    def recover_stamina(self):
        self.stamina = self.stamina + self.stamina_recovery
        if self.stamina > self.max_stamina:
            self.stamina = self.max_stamina

    # Урон
    def total_damage(self, use_skill) -> Tuple[Union[float, int], str]:
        result = 0
        result_str = ''
        if self.weapon:
            if self.stamina >= self.weapon.stamina_per_hit:
                result += random.uniform(self.weapon.min_damage,
                                         self.weapon.max_damage) * self.mod_attack  # Урон без умения
                self.stamina -= self.weapon.stamina_per_hit
                if self.skill and use_skill:
                    if not self.skill_used and self.stamina >= self.skill.stamina_per_use:
                        self.stamina -= self.skill.stamina_per_use
                        result += self.skill.damage
                        self.skill_used = True
                        result_str = f'{self.name} использует {self.skill.name} и наносит урон от умения {self.skill.damage:.2f} сопернику.'
                    elif self.skill_used:
                        result_str = f'Навык уже применен!'
                    else:
                        result_str = f'{self.name} попытался использовать {self.skill.name}, но у него не хватило выносливости.'
            else:
                result_str = f'{self.name} попытался использовать {self.weapon.name}, но у него не хватило выносливости.'
        return result, result_str
