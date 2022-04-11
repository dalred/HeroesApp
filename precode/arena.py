from typing import Union

from classes import Gamer, Cyberperson


class Arena:
    def __init__(self, gamer: Gamer = None, enemy: Cyberperson = None,
                 game_progr: bool = False):
        self.enemy = enemy
        self.gamer = gamer
        self.game_progress = game_progr

    def begin_game(self, gamer: Gamer, enemy: Cyberperson):
        self.gamer = gamer
        self.enemy = enemy
        self.game_progress = True

    def next_move(self):
        if not self.health_check():
            return self.finish_game()
        else:
            self.regeneration()
            return self.enemy.strike(self.gamer)

    def health_check(self):
        if self.enemy.health <= 0 or self.gamer.health <= 0:
            self.finish_game()
        return self.game_progress

    def finish_game(self):
        name = self.gamer.name
        self.game_progress = False
        if self.enemy.health > self.gamer.health:
            name = self.enemy.name
        result = f'Игра окончена!Победил: {name}!'
        return result

    def regeneration(self):
        self.gamer.recover_stamina()
        self.enemy.recover_stamina()

    def hit(self, use_skill: bool = False):
        result = self.gamer.strike(self.enemy, use_skill)
        result += self.next_move()
        return result
