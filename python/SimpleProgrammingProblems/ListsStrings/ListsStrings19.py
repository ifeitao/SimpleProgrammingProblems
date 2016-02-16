def translate(sentence):
    words = sentence.split()
    for i in range(len(words)):
        if words[i].isalpha():
            letters = list(words[i])
            first = letters.pop(0)
            first_upper = first.isupper()
            if first_upper:
                first = first.lower()
            letters.append(first)
            letters.append('a')
            letters.append('y')
            if first_upper:
                letters[0] = letters[0].upper()
            words[i] = "".join(letters)
    return " ".join(words)


def translate_back(sentence):
    words = sentence.split()
    for i in range(len(words)):
        if words[i].isalpha():
            letters = list(words[i])
            first_upper = letters[0].isupper()
            if first_upper:
                letters[0] = letters[0].lower()
            letters.pop()
            letters.pop()
            letters.insert(0, letters.pop())
            if first_upper:
                letters[0] = letters[0].upper()
            words[i] = "".join(letters)
    return " ".join(words)


print(translate("The quick brown fox"))
print(translate_back(translate("The quick brown fox")))
