import decimal
import sys

print("Radek")
print('Radek')

print(type('Radek'))  # <class 'str'>
print('39')
print(39)
print(type(39))
print(sys.int_info)
# sys.int_info(bits_per_digit=30, sizeof_digit=4,
#              default_max_str_digits=4300,
#              str_digits_check_threshold=640)
# print('Radek") # SyntaxError: unterminated string literal (detected at line 14)
# ctrl / - automatyczny komentarz
# print("59" + 90) 3 TypeError: can only concatenate str (not "int") to str
#
print("59" + "90")  # 5990
print(59 * "*")
print(59 * "9")
# ***********************************************************
# 99999999999999999999999999999999999999999999999999999999999
print(int("59"))  # int() rzutowanie, zamiana, 59
print("59" + str("90"))

print(3.99)
print(type(3.99))  # <class 'float'>
print(sys.float_info)
# sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021,
#                min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)
print(0.1 + 0.5)  # 0.6
print(0.1 + 0.2)  # 0.30000000000000004
#  the sum 12.345 + 1.0001 = 13.3451 might be rounded to 13.345.

# decimal - obejscie problemu zaokroglęnia
# zmienna - pudełko na dane
a = decimal.Decimal("10")
print(a)  # 10
a = decimal.Decimal(10)
print(a)
# ctrl d - powielanie lini
a = decimal.Decimal("1.2345")
b = decimal.Decimal("2.3456")
print(a + b)  # 3.5801
precyzja = decimal.Decimal("0.00")
print((a + b).quantize(precyzja))  # 3.58

# typ logiczne
# prawda fałsz
# True False
print(True)
print(False)
# True
# False
print(int(True))
print(int(False))
# 1
# 0
print(bool(1))
print(bool(0))
print(bool(100))

print(bool(None))  # nie wiem, nieokreslony stan, False
print(bool(""))  # False

# teksty są niemutowalne
tekst = 'Radek'
tekst.upper()  # """ Return a copy of the string converted to uppercase. """
print(tekst)
print(tekst.upper())
zm = tekst.upper()
print(zm)  # RADEK

# kolekcje - przechowuje wiele elemntów
# lista, krotka (tupla), zbior (set), słownik (dict)

lista = [5, 6, 7, 8, 9]
print(lista)  # [5, 6, 7, 8, 9], nie zmienia kolejności

lista2 = lista  # kopia referencji, adres w pamięci
print(lista2)
print(lista)
lista_copy = lista.copy()
lista.clear()  # kasowanie elementów z listy
print(lista)
print(lista2)
# [5, 6, 7, 8, 9]
# [5, 6, 7, 8, 9]
# []
# []
print(lista_copy)  # [5, 6, 7, 8, 9]

krotka = tuple(lista_copy)
print(type(krotka))  # lista do odczytu, pozwala efektywniej zarzadzac pamięcią
print(krotka)  # (5, 6, 7, 8, 9)

zbior = {5, 6, 5, 6, 6, 7, 8, 9, 0}
print(zbior)  # przechowuje unikalne wartości, {0, 5, 6, 7, 8, 9}
# nie zachowuje kolejności przy dodawaniu elementów

# słownik
# odwzorowanie jsona
# {'name' : "Radek", 'age': 45}
slownik = {'name': "Radek", 'age': 45}
print(type(slownik))
print(slownik)  # {'name': 'Radek', 'age': 45}
slownik = {'name': ["Radek", 'Tomek', "Marek"], 'age': 45}
print(slownik["name"]) # ['Radek', 'Tomek', 'Marek']
# name
# Radek
# Tomek
# Marek