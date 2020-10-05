def convertCelsiusToKelvin(c):
    return round(float(c + 273.15), 2)


def convertCelsiusToFahrenheit(c):
    return round(float((c * 1.8) + 32), 2)


def covertFahrenheitToCelsius(f):
    return round(float((f - 32) / 1.8), 2)


def convertFahrenheitToKelvin(f):
    return round(float((f - 32) / 1.8 + 273.15), 2)


def convertKelvinToCelsius(k):
    return round(float(k - 273.15), 2)


def convertKelvinToFahrenheit(k):
    return round(float(1.8*(k - 273.15) + 32), 2)

