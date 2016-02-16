def rectangular_print(words):
    max_length = max([len(word) for word in words])
    print('*' * (max_length + 4))
    for word in words:
        print("* {0}{1} *".format(word, ' ' * (max_length - len(word))))
    print('*' * (max_length + 4))


rectangular_print(["Hello", "World", "in", "a", "frame"])
