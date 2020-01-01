# API:
# textbox: user can input all the acceptable unit representations.
# no checkbox.
# if non-compatible units, raise error
# significance number

import json

with open('units.json', 'r') as f:
    unitDB = json.load(f)     # unitDB is dict
    # TODO handle duplicate key, otherwise probably will raise keyError

unitDB_category = set(unitDB.keys())
# ?????
# set is un-ordered, so not sequence, but does it has __inter__ or __next__
# I don't think set is necessary, because json file shall not allow duplicate key.
# However, set is more intuitive to describe.

# CHALLENGE: given a str, return the category.
# OPTION 1: make a dict, k: category, v: set/list.
# OPTION 2: make separate variables for each category as set/list
# OPTION 3: make each name as k, category as value.

# Option 1 seems to be the one that db will be implemented.

def check_category(inputUnit: str, unitNameDB: dict) -> str:
    """return the category of the str. length/volume..
    para: unitNameDB: dict. k: category; v: list
    """
    for category in unitNameDB.keys():
        if inputUnit in unitNameDB[category]:
            return category

    return None


def get_units_names_in_category(unitDB: dict) -> dict:
    """return dict. k: category; v: list of unit names"""
    unitNameDB = {}
    for category in unitDB_category:
        for unit_doc in unitDB[category]:
            unitNameDB[category] = unitNameDB.setdefault(category, []) + unit_doc["name"]

    return unitNameDB


def check_type(ini_unit: str) -> str:
    """return the type of the str. USC/SI.."""
    for units_array in unitDB.values():
        if









SI_prefix = {'k': 1000,
             'd': 0.1,
             'c': 0.01,
             'm': 0.001}


class Unit:
    def __init__(self):
        pass

    def check_category(self):
        """return the category"""
        with open('units.json') as f:


    def check_type(self):
        pass


    def convert(self, ini_unit, res_unit):
        if ini_unit.type is "USC" and res_unit.type is "USC":
            res = self.USC2USC_convert(ini_unit, res_unit)
        elif ini_unit.type is "USC" and res_unit.type is "SI":
            res = self.USC2SI_convert(ini_unit, res_unit)
        elif ini_unit.type is "SI" and res_unit.type is "USC":
            res = self.SI2USC_convert(ini_unit, res_unit)
        else:
            res = self.SI2SI_convert(ini_unit,res_unit)

        return res

    def USC2USC_convert(self, ini_unit, res_unit):
        pass

    def USC2SI_convert(self, ini_unit, res_unit):
        pass

    def SI2USC_convert(self, ini_unit, res_unit):
        pass

    def SI2SI_convert(self, ini_unit, res_unit):
        """process the prefix, but the length/area/volume is different."""
        res_unit = SI_prefix[ini_unit.prefix]/SI_prefix[res_unit]

    def __getattr__(self, item):
        pass


class Convert:
    pass

class LengthUnit(Unit):
    def __init__(self):
        pass

    def convert(self, ini_unit, res_unit):
        pass

    def USC2USC_convert(self):
        pass

    def USC2SI_convert(self):
        pass

    def SI2SI_convert(self):
        pass

    def SI_USC_convert(self):



def convert_unit():
    ini_unit = Unit()
    ini_unit.convert()

