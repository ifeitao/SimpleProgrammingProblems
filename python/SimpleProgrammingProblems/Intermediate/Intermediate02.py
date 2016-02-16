import math


def init_leap_year_rule(fractional, error):
    rule = []
    margin = fractional
    leap_period = 1
    while margin > error:
        rate = math.floor(1 / margin)
        leap_period *= rate
        rule.append(leap_period)
        margin = 1 - rate * margin
    return rule


def __test__():
    error = pow(0.1, 10)
    print(init_leap_year_rule(0.1, error))
    print(init_leap_year_rule(0.31, error))
    print(init_leap_year_rule(0.88, error))
    print(init_leap_year_rule(0.2422, error))  # earth


if __name__ == "__main__":
    __test__()
