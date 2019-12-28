# LOG
# V1.1d: hint for res_unit.
# V1.1c: make every category work.
# V1.1b: Modify USC_length_units. Use option2,3 to find k through v.
# V1.1a: popup menu. Cons: a. only works for length. has to modularize the category-based process.
# V1: three inputs(). Cons:  a. has to input the exact unit.

# TODO Treat an entry and ini_unit as a single object.
# TODO Make json file
# TODO Make a framework for dealing with different category.


# ref: https://en.wikipedia.org/wiki/United_States_customary_units
# Exactly defined in 1959
LB2G = 453.59237
YD2M = 0.9144


# The fluid ounce derives its name originally from being the volume of one ounce avoirdupois of water
# But in the US it is defined as ​1⁄128 of a US gallon.
# Consequently, a fluid ounce of water weighs about 1.041 ounces avoirdupois.
GAL2L = 3.785411784         # 1cu m = 10**3 L


def convert_unit(entry: float, ini_unit: str, res_unit: str, category: str) -> float:
    """Convert the ini_unit into res_unit."""
    # So far, only deal with special case: usc2si, no usc2usc/si2usc
    # OPTION 1: lots of if smt
    if category == 'temperature':
        return USC2SI_temp_convert(entry)
    else:
        if category == 'length':
            res_default = USC2SI_length_convert(entry, ini_unit)
        elif category == 'area':
            res_default = USC2SI_area_convert(entry, ini_unit)
        elif category == 'volume':
            res_default = USC2SI_volume_convert(entry, ini_unit)
        elif category == 'cooking':
            res_default = USC2SI_cooking_convert(entry, ini_unit)
        else:                    # category == 'weight'
            res_default = USC2SI_weight_convert(entry, ini_unit)
    # TODO visitor DP? according to different category, use different convert func.

    return SI2SI_convert(res_unit=res_unit, value=res_default)


# -> yard
USC2USC_length_table = {
    'inch(in)': 1/(12*3),       # in * ft
    'foot(ft)': 1/3,            # ft
    'yard(yd)': 1,
    'mile(mi)': 1760
}

# Directly -> sq m. Survey foot ≠ International foot. Not exact.
USC2SI_area_table = {
    'sq ft': 0.09290341,
    'acre': 4046.873
}

# -> cu yard
USC2USC_volume_table = {
    'cubic inch(cu in)': 1/(12*3)**3,
    'cubic foot(cu ft)': 1/3**3,
    'cubic yard(cu yd)': 1,
}

# Directly -> L
# 1 L ≡ 1 cu dm = 0.001 m
USC2SI_volume_table = {
    'cubic inch(cu in)': 0.016387064,
    'cubic foot(cu ft)': 28.316846592,
    'cubic yard(cu yd)': 764.554857984,
    'acre-foot(acre ft)': 0.00123348183754752,
}

# Fluid & Dry: -> gallon
# volume
USC2USC_cooking_table = {
    'teaspoon(tsp)': 1/(3 * 2 * 8 * 2 * 2 * 4),     # tsp * Tbsp * oz * cp * pt * qt
    'tablespoon(Tbsp)': 1/(2 * 8 * 2 * 2 * 4),      # Tbsp * oz * cp * pt * qt
    'US fluid ounce(fl oz)': 1/(8 * 2 * 2 * 4),     # oz * cp * pt * qt
    'US cup(cp)': 1/(2 * 2 * 4),                    # cp * pt * qt
    'US pint(pt)': 1/(2 * 4),                       # pt * qt
    'US quart(qt)': 1/4,                            # qt
    'US gallon(gal)': 1,
    'peck(pk)': 2,                                  # dry
    'bushel(bu)': 2 * 4,                            # dry
}

# avoirdupois weight: -> lb
USC2USC_weight_table = {
    'grain(gr)': 1/7000,
    'dram(dr)': 1/16 * 1/16,
    'ounce(oz)': 1/16,
    'pound(lb)': 1,
    'US hundredweight(cwt)': 100,
    'long hundredweight(long cwt)': 112,
    'short ton(ton)': 2000,
    'long ton': 2240
}


SI_base_unit = {'length': 'm',
                'area': 'sq m',             # TODO this shall be treated differently
                'volume': 'L',
                'cooking': 'L',
                'weight': 'g',
                'temp': 'C',
                }

SI_prefix = {'k': 0.001,
             'd': 10,
             'c': 100,
             'm': 1000,
             }


category_table = ['temperature', 'length', 'area', 'volume', 'cooking', 'weight']

# get key list sorted by value
# OPTION 1: key(),values(),index()
USC_length_units = [list(USC2USC_length_table.keys())[list(USC2USC_length_table.values()).index(v)]
                    for v in sorted(USC2USC_length_table.values())]


# OPTION 2: def get_key()
def get_key(d, value) -> str:
    for k, v in d.items():
        if v == value:
            return k
    # return k for k,v in d.items() if v == value       # doesn't work, need [] or other comprehension


USC_length_units2 = [get_key(USC2USC_length_table, v)
                     for v in sorted(USC2USC_length_table.values())]


# OPTION 3: reverse dict
USC_length_units3 = [{v: k for k, v in USC2USC_length_table.items()}[v]
                     for v in sorted(USC2USC_length_table.values())]

USC_area_units = [{v: k for k, v in USC2SI_area_table.items()}[v]
                  for v in sorted(USC2SI_area_table.values())]

USC_volume_units = [{v: k for k, v in USC2USC_volume_table.items()}[v]
                    for v in sorted(USC2USC_volume_table.values())]

USC_cooking_units = [{v: k for k, v in USC2USC_cooking_table.items()}[v]
                     for v in sorted(USC2USC_cooking_table.values())]

USC_weight_units = [{v: k for k, v in USC2USC_weight_table.items()}[v]
                    for v in sorted(USC2USC_weight_table.values())]


# TODO modularize and generate automatically
SI_length_units = []
SI_area_units = []
SI_volume_units = []
SI_cooking_units = []
SI_weight_units = []


def SI2SI_convert(res_unit: str, value: float) -> int:
    if len(res_unit) == 2:
        return value * SI_prefix[res_unit[0]]
    elif res_unit.startswith('sq') and len(res_unit) == 5:
        return value * SI_prefix[res_unit[-2]] ** 2
    elif res_unit.startswith('cu') and len(res_unit) == 5:
        return value * SI_prefix[res_unit[-2]] ** 3
    else:
        return value


# -> m
def USC2SI_length_convert(entry: float, ini_unit: str) -> float:    # default_unit = m
    return entry * USC2USC_length_table[ini_unit] * YD2M


# -> sq m
def USC2SI_area_convert(entry: float, ini_unit: str) -> float:      # default_unit = sq m
    return entry * USC2SI_area_table[ini_unit]


# -> L
def USC2SI_volume_convert(entry: float, ini_unit: str) -> float:    # default_unit = L
    return entry * USC2SI_volume_table[ini_unit]


# -> L
def USC2SI_cooking_convert(entry: float, ini_unit: str) -> float:
    return entry * USC2USC_cooking_table[ini_unit] * GAL2L


# -> g
def USC2SI_weight_convert(entry: float, ini_unit: str) -> float:    # default_unit = g
    return entry * USC2USC_weight_table[ini_unit] * LB2G


# F -> C
def USC2SI_temp_convert(entry: float) -> float:                     # default_unit = C
    return (entry-32)/1.8


if __name__ == '__main__':
    print('Please input the value to convert:')
    entry = float(input())
    print('Choose the number representing the following categories:')
    for i in enumerate(category_table):
        print('{}: {}'.format(i[0], i[1]))
    category = category_table[int(input())]
    print('Choose the number representing the following units of the entry value:')
    # Lots of if smt is the dumbest way to do that.
    # TODO Change to a category based process, not if smt.
    if category == 'length':
        for i in enumerate(USC_length_units):
            print('{}: {}'.format(i[0], i[1]))
        ini_unit = USC_length_units[int(input())]
    elif category == 'area':
        for i in enumerate(USC_area_units):
            print('{}: {}'.format(i[0], i[1]))
        ini_unit = USC_area_units[int(input())]
    elif category == 'volume':
        for i in enumerate(USC_volume_units):
            print('{}: {}'.format(i[0], i[1]))
        ini_unit = USC_volume_units[int(input())]
    elif category == 'cooking':
        for i in enumerate(USC_cooking_units):
            print('{}: {}'.format(i[0], i[1]))
        ini_unit = USC_cooking_units[int(input())]
    elif category == 'weight':
        for i in enumerate(USC_weight_units):
            print('{}: {}'.format(i[0], i[1]))
        ini_unit = USC_weight_units[int(input())]
    else:           # category == 'temperature'
        print('0: F')
        ini_unit = 'F'      # TODO try/except to deal with wrong index

    print('Please input the unit to be converted into:')
    print('Hint: The SI base unit for {} is {}'.format(category, SI_base_unit[category]))
    res_unit = input()
    res = convert_unit(entry, ini_unit, res_unit, category)
    print('%.3f' % res)             # TODO print .3f only when longer than .3f, and manage significant digits
    # TODO loop the process
