from equipment import EquipmentData, Equipment
from helpers.functions import read_json
from skills import All_skill, Skill_data

eq_dict: dict = read_json('data/equipment.json')
skill_dict: dict = read_json('data/skills.json')
skills = All_skill(skill_dict, Skill_data)
eq = Equipment(eq_dict, EquipmentData)