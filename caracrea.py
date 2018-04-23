#!/usr/bin/env python
"""this module can create a character"""
import Caracteristics as Caract


class Creator(object):
    """docstring for Creator

    """

    def __init__(self, name="Random", sex="Random", race="Human"):
        self.character = Caract.Caracteristics(name, sex, race)
        print("new character created")
        self.character.show_values()

    def show_values_carac(self):
        self.character.show_values()

    def change_name_carac(self):
        new_name = raw_input("Enter the new character name\n")
        self.character.change_name(new_name)

    def change_gender_carac(self):
        new_gender = raw_input("Select your gender:\nMale or Female\nType the one you choose\n")
        self.character.change_gender(new_gender)

    def change_race_carac(self):
        new_race = raw_input("Enter the new character race\n")
        self.character.change_race(new_race)
