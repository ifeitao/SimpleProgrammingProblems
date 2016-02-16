def alternatingly_combines(elements1, elements2):
    length1 = len(elements1)
    length2 = len(elements2)
    length_total = length1 + length2
    if length1 > length2:
        elements1, elements2 = elements2, elements1
    combined = [0] * length_total
    combined[:length1 * 2:2] = elements1[0:length1]
    combined[1:length1 * 2:2] = elements2[0:length1]
    combined[length1 * 2:length_total] = elements2[length1:length2]
    return combined


def alternatingly_combines2(elements1, elements2):
    length1 = len(elements1)
    length2 = len(elements2)
    if length1 > length2:
        elements1, elements2 = elements2, elements1
    combined = []
    for i in range(length1):
        combined.append(elements1[i])
        combined.append(elements2[i])
    combined += elements2[length1:length2]
    return combined


if __name__ == "__main__":
    print(alternatingly_combines([1, 2], ['a', 'b', 'c']))
    print(alternatingly_combines2([1, 2], ['a', 'b', 'c']))
    print(alternatingly_combines([1, 2, 3], ['a', 'b', 'c']))
    print(alternatingly_combines2([1, 2, 3], ['a', 'b', 'c']))
    print(alternatingly_combines([1, 2, 3], ['a', 'b', 'c', 'd']))
    print(alternatingly_combines2([1, 2, 3], ['a', 'b', 'c', 'd']))
