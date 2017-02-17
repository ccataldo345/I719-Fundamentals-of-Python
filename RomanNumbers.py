def roman_to_int(string):
    if string == "I":
        return 1
    if string == "V":
        return 5
    if string == "X":
        return 10
    if string == "L":
        return 50
    if string == "C":
        return 100
    if string == "D":
        return 500
    if string == "M":
        return 1000

print(roman_to_int("X"))