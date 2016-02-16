def on_all(items, function):
    converted = []
    for item in items:
        converted.append(function(item))
    return converted


def square(x):
    return x * x

if __name__ == "__main__":
    print([i * i for i in range(1, 21)])
    print(on_all(range(1, 21), square))
    print(on_all(range(1, 21), lambda x: x * x))
    print(list(map(lambda x: x * x, range(1, 21))))
