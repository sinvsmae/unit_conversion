# LOG
# v2.3: in units.json, unitList -> dict
# v2.2e: handle range
# v2.2d: to_categoryObjList -> to_categoryObjDict
# V2.1c: handle nested dict.
# V2.1b: create a dict. k: category, v: unitObjs.
# V2.1a: unit object, generic traverse get function
# V2: check the category

# API 2.0:
# mere input, not GUI, using BNF to define grammar
# data driven program
# parse json once, and create object.
# API:
# textbox: user can input all the acceptable unit representations.
# no checkbox.
# if non-compatible units, raise error
# significance number


import json


def to_categoryObjList(d: dict) -> list:
    """return a list of categoryObj.
    obj.attr = unitObjList
    """
    categoryObjList = []
    for category, unitDocList in d.items():
        unitObjList = to_unitObjList(unitDocList)
        categoryObjList.append(Category(category, unitObjList))

    return categoryObjList


# compared to list, return dict is more intuitive and easy to access later.
# set is not ok cuz no access via idx or key.
# k: categoryName, v: obj
def to_categoryObjDict(d: dict) -> dict:
    """return a dict of categoryObj. k: category name, v: unitObjList"""
    return {category: Category(category, unitDocList)
            for category, unitDocList in d.items()}


def to_unitObjList(l: list) -> list:
    """given an array of documents, return a list of unitObj"""
    unitObjList = []
    for unitDoc in l:
        unitObjList.append(Unit(unitDoc))
    return unitObjList


def to_unitObjDict(l:list) -> dict:
    """given an array of documents, return a dict of unitObj.
    k: unit_name; v: unitObj
    """
    return {unitDoc['id']: Unit(unitDoc) for unitDoc in l}


class Category:
    def __init__(self, name: str, unitDocList: list):
        self.name = name
        self.unitObjDict = to_unitObjDict(unitDocList)

    def __repr__(self):
        return self.name.capitalize()


class Unit:
    def __init__(self, unitDoc: dict):
        self.id = unitDoc['id']
        self.traverse_dict(unitDoc)

    # def __repr__(self):
    #     return self.name.capitalize()

    def traverse_dict(self, unitDoc: dict):
        for key, value in unitDoc.items():
            # if hasattr __dict__
            print(key, value)
            if isinstance(value, dict):
                self.__dict__[key] = value
                self.traverse_dict(value)
            else:
                self.__dict__[key] = value

    def __repr__(self):
        return self.id.capitalize()


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


def check_system(ini_unit: str) -> str:
    """return the type of the str. USC/SI.."""
    for category in unitDB.keys():
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

