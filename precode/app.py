import os
import random

from flask import Flask, render_template, request, redirect, url_for
from arena import Arena
from classes import Gamer, Cyberperson
from implemented import eq, skills

BASEDIR = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

heroes = {}
game = Arena()


@app.route("/", methods=["GET", "POST"])
def page_index():
    return render_template('index.html')


@app.route("/choose-hero/", methods=["GET", "POST"])
def choose_hero():
    result = {
        "header": 'Выберите героя',  # для названия страниц
        "classes": ['Воин', 'Вор'],  # для названия классов
        "weapons": eq.get_weapon_names,  # для названия оружия
        "armors": eq.get_armor_names  # для названия брони
    }
    if request.method == "POST":
        name = request.form.get('name')
        armor = request.form.get('armor')
        weapon = request.form.get('weapon')
        unit_class = request.form.get('unit_class')
        gamer = Gamer(name=name, name_unit=unit_class)
        gamer.equip_weapon(eq.get_weapon(weapon))
        gamer.equip_armor(eq.get_armor(armor))
        skill_name = random.choice(skills.get_skill_names)
        gamer.set_skill(skill=skills.get_skill(skill_name))
        heroes["player"] = gamer
        return redirect(url_for('choose_enemy'))
    if request.method == "GET":
        return render_template('hero_choosing.html', result=result)


@app.route("/choose-enemy/", methods=["GET", "POST"])
def choose_enemy():
    result = {
        "header": 'Выберите врага',  # для названия страниц
        "classes": ['Воин', 'Вор'],  # для названия классов
        "weapons": eq.get_weapon_names,  # для названия оружия
        "armors": eq.get_armor_names  # для названия брони
    }
    if request.method == "POST":
        name = request.form.get('name')
        armor = request.form.get('armor')
        weapon = request.form.get('weapon')
        unit_class = request.form.get('unit_class')
        enemy = Cyberperson(name=name, name_unit=unit_class)
        enemy.equip_weapon(eq.get_weapon(weapon))
        enemy.equip_armor(eq.get_armor(armor))
        skill_name = random.choice(skills.get_skill_names)
        enemy.set_skill(skill=skills.get_skill(skill_name))
        heroes["enemy"] = enemy
        return redirect(url_for('fight'))

    if request.method == "GET":
        return render_template('hero_choosing.html', result=result)


@app.route("/fight/", methods=["GET", "POST"])
def fight():
    if request.method == "GET":
        result = 'Бой начался!'
        game.begin_game(gamer=heroes.get('player'), enemy=heroes.get('enemy'))
        return render_template('fight.html', heroes=heroes, result=result)


@app.route("/fight/hit", methods=["GET", "POST"])
def fight_hit():
    if request.method == "GET":
        battle_result = 'test'
        if not game.game_progress:
            result = game.finish_game()
        else:
            result = game.hit()
        return render_template('fight.html', heroes=heroes, result=result)

@app.route("/fight/use-skill", methods=["GET", "POST"])
def use_skill():
    if request.method == "GET":
        if not game.game_progress:
            result = game.finish_game()
        else:
            result = game.hit(use_skill=True)
        return render_template('fight.html', heroes=heroes, result=result)

@app.route("/fight/pass-turn", methods=["GET", "POST"])
def pass_turn():
    if request.method == "GET":
        if not game.game_progress:
            result = game.finish_game()
        else:
            result = f'{game.gamer.name}: пропускаю ход.'
            result += game.next_move()
        return render_template('fight.html', heroes=heroes, result=result)

@app.route("/fight/end-fight", methods=["GET", "POST"])
def end_fight():
    if request.method == "GET":
        return redirect(url_for('page_index'))

# if __name__ == "__main__":
#     app.run('127.0.0.1', 8000, debug=True)
