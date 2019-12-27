# Todo: treat an entry and ini_unit as a single object.


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
    if category is 'temperature':
        return USC2SI_temp_convert(entry)
    else:
        if category is 'length':
            res_default = USC2SI_length_convert(entry, ini_unit)
        elif category is 'area':
            res_default = USC2SI_area_convert(entry, ini_unit)
        elif category is 'volume':
            res_default = USC2SI_volume_convert(entry, ini_unit)
        else:                    # category is 'weight'
            res_default = USC2SI_weight_convert(entry, ini_unit)
    # Todo: visitor DP? according to different category, use different convert func.

    return SI2SI_convert(res_unit=res_unit, entry=res_default)


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
                'area': 'sq m',             # Todo: this shall be treated differently
                'volume': 'L',
                'weight': 'g',
                'temp': 'C',
                }

SI_prefix = {'k': 10**3,
             'd': 10**(-1),
             'c': 10**(-2),
             'm': 10**(-3),
             }


category_table = ['temperature', 'length', 'area', 'volume', 'cooking', 'weight']

# get key list sorted by value
# OPTION 1: key(),values(),index()

for v in sorted(d.values()):
    k = list(USC2USC_length_table.keys())[list(USC2USC_length_table.values()).index(v)]
    print(k)


USC_length = [k ]
USC_area = ['sq ft, ']


def SI2SI_convert(res_unit: str, entry: float) -> int:
    if len(res_unit) == 2:
        return SI_base_unit[res_unit] * float
    else:
        return entry


# -> m
def USC2SI_length_convert(entry: float, ini_unit: str) -> float:    # default_unit = m
    return entry * USC2USC_length_table[ini_unit] * YD2M


# -> sq m
def USC2SI_area_convert(entry: float, ini_unit: str) -> float:      # default_unit = sq m
    return entry * USC2SI_area_table[ini_unit]


# -> L
def USC2SI_volume_convert(entry: float, ini_unit: str) -> float:    # default_unit = L
    return entry * USC2USC_volume_table[ini_unit] * GAL2L


# -> g
def USC2SI_weight_convert(entry: float, ini_unit: str) -> float:    # default_unit = g
    return entry * USC2USC_weight_table[ini_unit] * LB2G


# F -> C
def USC2SI_temp_convert(entry: float) -> float:                     # default_unit = C
    return (entry-32)/1.8


if __name__ == '__main__':
    entry = float(input())
    print('Choose the number representing the following categories:\n')
    for i in enumerate(category_table):
        print('{}: {}'.format(i[0], i[1]))
    category = category_table[input()]
    print('Choose the number representing the following units:')
    print()
    res_unit = input()
    res = convert_unit(entry, ini_unit, res_unit)
    print('%.3f' % res)
