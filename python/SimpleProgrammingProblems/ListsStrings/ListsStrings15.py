# todo subtraction & multiplication
def digit_list_sum(list1, list2):
    more = len(list1) - len(list2)
    if more > 0:
        for i in range(more):
            list2.insert(0, '0')
    if more < 0:
        for i in range(-more):
            list1.insert(0, '0')
    list_sum = []
    carry = '0'
    for index in range(-1, -len(list1) - 1, -1):
        sum_list = digit_sum(list1[index], list2[index], carry)  # todo look in table
        list_sum.insert(0, sum_list[1])
        carry = sum_list[0]
    if carry != '0':
        list_sum.insert(0, carry)
    return list_sum


def digit_sum(digit1, digit2, carry):
    list_sum = list(str((int(digit1) + int(digit2) + int(carry))))
    if len(list_sum) < 2:
        list_sum.insert(0, '0')
    return list_sum


if __name__ == "__main__":
    a = 5234432432142134312
    b = 567897678678686786786786
    digit_list = digit_list_sum(list(str(a)), list(str(b)))
    c = int("".join(digit_list))
    print("{0}+{1}={2}, {3}".format(a, b, c, c == a + b))
