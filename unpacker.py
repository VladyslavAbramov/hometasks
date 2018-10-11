def unpacker(*args):
    result = []
    for item in args:
        if type(item) not in (str, list, set, frozenset, tuple):
            result.append(item)
        else:
            result = result + unpacker(*item)
    return result


print(unpacker(1, 2, [3, 4, (5, 6, [7, 8], 9)], 10))

