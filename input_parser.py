# LOG
# input_parser v1.2: entry str->number, significance number
# input_parser v1.1: get 3 variables.
# API
# input ::= <number> <ini_unit> to <res_unit>


def input_parser(s: str)-> tuple:
    # l = s.partition(" to ")
    l = s.split(' to ')
    res_unit = l[-1]
    entry, ini_unit = l[0].partition(' ')[0], l[0].partition(' ')[-1]
    return entry, ini_unit, res_unit        # entry is str.


if __name__ == "__main__":
    s = input()
    print(input_parser(s))




