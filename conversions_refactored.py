class ConversionNotPossible(Exception):
    def __init__(self, message):
        self.message = message


def convert(fromUnit, toUnit, value):
    convert_chart = {
        'f': {'c': '(value - 32) / 1.8', 'k': '(value - 32) / 1.8 + 273.15', 'f': 'value'},
        'c': {'f': '(value * 1.8) + 32', 'k': 'value + 273.15', 'c': 'value'},
        'k': {'c': 'value - 273.15', 'f': '1.8*(value - 273.15) + 32', 'k': 'value'},
        'mi': {'yd': 'value * 1760.0', 'm': 'value / 0.00062137', 'mi': 'value'},
        'm': {'yd': 'value * 1.0936', 'mi': 'value * 0.00062137', 'm': 'value'},
        'yd': {'mi': 'value * 0.00056818', 'm': 'value / 1.0936', 'yd': 'value'}}

    err = True
    for key in convert_chart:
        if key == fromUnit:
            err = False
            obj = convert_chart[key]

            length = 0
            for x in obj:
                length += 1
                if x == toUnit:
                    return round(float(eval(obj[x])), 2)
                elif x != toUnit and length == len(obj):
                    err = True

    if not err:
        return 0
    else:
        raise ConversionNotPossible("Conversion Not Possible!!")


print(convert('yd', 'yd', 100))
