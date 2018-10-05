def get_ascii(string):
    assert type(string) is str
    arr = list(string)
    result = []
    for char in arr:
        result.append(ord(char))
    return tuple(result)