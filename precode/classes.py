import random

from unit import BaseUnit


class Gamer(BaseUnit):
    def strike(self, unit: BaseUnit, use_skill=False) -> str:
        result_str = ''
        if not self.skill_used and use_skill:
            use_skill = True
        damage, result_str = self.total_damage(use_skill)
        result_str += unit.defence(self, damage)
        return result_str


class Cyberperson(BaseUnit):

    def strike(self, unit: BaseUnit) -> str:
        use_skill = False
        result_str = ''
        if not self.skill_used:
            if random.randint(0, 9) == 5:
                use_skill = True
        damage, result_str = self.total_damage(use_skill)
        result_str += unit.defence(self, damage)
        return result_str
