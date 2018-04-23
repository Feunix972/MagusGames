#!/usr/bin/env python
"""This module is for the caracteristics of the character create"""


class Caracteristics(object):
    """docstring for Caracteristics

    param: character_name: name of the character
    param: character_gender: sex of the character
    param: character_race: race of the character
    param: life_point: life of the character
    param: skill_power: the strength skill power multiplicator
    param: stamina_stats: values of the character stamina
    param: energy_stats: values of the character mana
    """

    def __init__(self, name, gender, race):
        """methode for initialise the caracteristics of the character"""
        self.character_name = name
        self.character_race = race
        self.character_gender = gender
        self.life_point = 0
        self.skill_power = 0
        self.stamina_stats = 0
        self.energy_stats = 0

    def show_values(self):
        """function to display the values of the character"""
        print("The character {} , sex: {}, race: {}, Life Point: {},\
         Skill Power: {}, Stamina: {}, Energy: {}" .format(
         self.character_name,
         self.character_gender,
         self.character_race,
         self.life_point,
         self.skill_power,
         self.stamina_stats,
         self.energy_stats))

    def change_name(self, new_name):
        """function to change the name of the character"""
        self.character_name = new_name
        print("The character has changed his name for {} ".format(self.character_name))

    def change_gender(self, new_gender):
        """function to change the gender of the character"""
        self.character_gender = new_gender
        print("The character has changed his sex for {} ".format(self.character_gender))

    def change_race(self, new_race):
        """function to change the race of the character"""
        self.character_race = new_race
        print("The character has changed his race for {} ".format(self.character_race))
