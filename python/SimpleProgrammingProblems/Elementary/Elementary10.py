def is_leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


counter = 0
index = 2016
while counter < 20:
    if is_leap_year(index):
        print(index)
        counter += 1
    index += 1
