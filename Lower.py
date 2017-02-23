def lower_than(number_1, number_2):
    if number_1 < number_2:
        return number_1
    if number_2 < number_1:
        return number_2
    if number_1 == number_2:
        return "EQUAL"

lower_than(2,5)


