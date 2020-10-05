import unittest
from conversions import convertCelsiusToKelvin, convertCelsiusToFahrenheit, covertFahrenheitToCelsius, \
    convertFahrenheitToKelvin, convertKelvinToCelsius, convertKelvinToFahrenheit
from conversions_refactored import convert, ConversionNotPossible


class Conversions(unittest.TestCase):
    def test_celsius_to_kelvin_func(self):
        print("""\nTesting convertCelsiusToKelvin func 
        it should return correct value""")
        result1 = convertCelsiusToKelvin(5)
        result2 = convertCelsiusToKelvin(300)
        result3 = convertCelsiusToKelvin(68)
        result4 = convertCelsiusToKelvin(251)
        result5 = convertCelsiusToKelvin(-20)
        print("5 celsius should equal to 278.15 kelvin")
        self.assertEqual(278.15, result1)
        print("300 celsius should equal to 573.15 kelvin")
        self.assertEqual(573.15, result2)
        print("68 celsius should equal to 341.15 kelvin")
        self.assertEqual(341.15, result3)
        print("251 celsius should equal to 524.15 kelvin")
        self.assertEqual(524.15, result4)
        print("-20 celsius should equal to 253.15 kelvin")
        self.assertEqual(253.15, result5)

    def test_celsius_to_fahrenheit_func(self):
        print("""\nTesting convertCelsiusToFahrenheit func 
        it should return correct value""")
        result1 = convertCelsiusToFahrenheit(5)
        result2 = convertCelsiusToFahrenheit(300)
        result3 = convertCelsiusToFahrenheit(68)
        result4 = convertCelsiusToFahrenheit(251)
        result5 = convertCelsiusToFahrenheit(-20)
        print("5 celsius should equal to 41.0 fahrenheit")
        self.assertEqual(41.0, result1)
        print("300 celsius should equal to 572.0 fahrenheit")
        self.assertEqual(572.0, result2)
        print("68 celsius should equal to 154.4 fahrenheit")
        self.assertEqual(154.4, result3)
        print("251 celsius should equal to 483.8 fahrenheit")
        self.assertEqual(483.8, result4)
        print("-20 celsius should equal to -4 fahrenheit")
        self.assertEqual(-4.0, result5)

    def test_fahrenheit_to_celsius_func(self):
        print("""\nTesting covertFahrenheitToCelsius func 
        it should return correct value""")
        result1 = covertFahrenheitToCelsius(5)
        result2 = covertFahrenheitToCelsius(300)
        result3 = covertFahrenheitToCelsius(68)
        result4 = covertFahrenheitToCelsius(251)
        result5 = covertFahrenheitToCelsius(-20)
        print("5 fahrenheit should equal to -15 celsius")
        self.assertEqual(-15, result1)
        print("300 fahrenheit should equal to 148.89 celsius")
        self.assertEqual(148.89, result2)
        print("68 fahrenheit should equal to 20 celsius")
        self.assertEqual(20, result3)
        print("251 fahrenheit should equal to 121.67 celsius")
        self.assertEqual(121.67, result4)
        print("-20 fahrenheit should equal to -28.89 celsius")
        self.assertEqual(-28.89, result5)

    def test_fahrenheit_to_kelvin_func(self):
        print("""\nTesting convertFahrenheitToKelvin func 
        it should return correct value""")
        result1 = convertFahrenheitToKelvin(5)
        result2 = convertFahrenheitToKelvin(300)
        result3 = convertFahrenheitToKelvin(68)
        result4 = convertFahrenheitToKelvin(251)
        result5 = convertFahrenheitToKelvin(-20)
        print("5 fahrenheit should equal to 258.15 kelvin")
        self.assertEqual(258.15, result1)
        print("300 fahrenheit should equal to 422.04 kelvin")
        self.assertEqual(422.04, result2)
        print("68 fahrenheit should equal to 293.15 kelvin")
        self.assertEqual(293.15, result3)
        print("251 fahrenheit should equal to 394.82 kelvin")
        self.assertEqual(394.82, result4)
        print("-20 fahrenheit should equal to 244.26 kelvin")
        self.assertEqual(244.26, result5)

    def test_kelvin_to_celsius_func(self):
        print("""\nTesting convertKelvinToCelsius func 
        it should return correct value""")
        result1 = convertKelvinToCelsius(5)
        result2 = convertKelvinToCelsius(300)
        result3 = convertKelvinToCelsius(68)
        result4 = convertKelvinToCelsius(251)
        result5 = convertKelvinToCelsius(-20)
        print("5 kelvin should equal to -268.15 celsius")
        self.assertEqual(-268.15, result1)
        print("300 kelvin should equal to 26.85 celsius")
        self.assertEqual(26.85, result2)
        print("68 kelvin should equal to -205.15 celsius")
        self.assertEqual(-205.15, result3)
        print("251 kelvin should equal to -22.15 celsius")
        self.assertEqual(-22.15, result4)
        print("-20 kelvin should equal to -293.15 celsius")
        self.assertEqual(-293.15, result5)

    def test_kelvin_to_fahrenheit_func(self):
        print("""\nTesting convertKelvinToFahrenheit func 
        it should return correct value""")
        result1 = convertKelvinToFahrenheit(5)
        result2 = convertKelvinToFahrenheit(300)
        result3 = convertKelvinToFahrenheit(68)
        result4 = convertKelvinToFahrenheit(251)
        result5 = convertKelvinToFahrenheit(-20)
        print("5 kelvin should equal to -450.67 fahrenheit")
        self.assertEqual(-450.67, result1)
        print("300 kelvin should equal to 80.33 fahrenheit")
        self.assertEqual(80.33, result2)
        print("68 kelvin should equal to -337.27 fahrenheit")
        self.assertEqual(-337.27, result3)
        print("251 kelvin should equal to -7.87 fahrenheit")
        self.assertEqual(-7.87, result4)
        print("-20 kelvin should equal to -495.67 fahrenheit")
        self.assertEqual(-495.67, result5)

    def test_general_convert_func(self):
        print("""\nTesting convert func 
        it should return correct value""")
        same_unit = convert('c', 'c', 100)
        c_to_f = convert('c', 'f', 50)
        c_to_k = convert('c', 'k', 80)
        f_to_c = convert('f', 'c', 40)
        f_to_k = convert('f', 'k', 20)
        k_to_c = convert('k', 'c', -20)
        k_to_f = convert('k', 'f', 49)
        mi_to_m = convert('mi', 'm', 10)
        mi_to_yd = convert('mi', 'yd', 2)
        m_to_mi = convert('m', 'mi', 1890)
        m_to_yd = convert('m', 'yd', 89)
        yd_to_m = convert('yd', 'm', 38)
        yd_to_mi = convert('yd', 'm', 489)


        print("same unit returns value")
        self.assertEqual(100, same_unit)
        print("50 celsius should equal to 122.0 fahrenheit")
        self.assertEqual(122.0, c_to_f)
        print("80 celsius should equal to 353.15 kelvin")
        self.assertEqual(353.15, c_to_k)
        print("40 kelvin should equal to 4.44 fahrenheit")
        self.assertEqual(4.44, f_to_c)
        print("20 fahrenheit should equal to 266.48 kelvin")
        self.assertEqual(266.48, f_to_k)
        print("-20 kelvin should equal to -293.15 fahrenheit")
        self.assertEqual(-293.15, k_to_c)
        print("49 kelvin should equal to -371.47 fahrenheit")
        self.assertEqual(-371.47, k_to_f)
        print("10 miles should equal to 16093.47 meters")
        self.assertEqual(16093.47, mi_to_m)
        print("2 miles should equal to 3520.0 yards")
        self.assertEqual(3520.0, mi_to_yd)
        print("1890 meters should equal to 1.17 miles")
        self.assertEqual(1.17, m_to_mi)
        print("89 meters should equal to 97.33 yards")
        self.assertEqual(97.33, m_to_yd)
        print("38 yards should equal to 34.75 meters")
        self.assertEqual(34.75, yd_to_m)
        print("489 yards should equal to 447.15 miles")
        self.assertEqual(447.15, yd_to_mi)
        #






if __name__ == '__main__':
    unittest.main()
