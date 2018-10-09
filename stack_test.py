import stack


def test():
    p = stack.Stack(int, 1)

    if p.push(2) is not None:
        return 'Fail _push()'

    try:
        p.push('qwerty')
    except ValueError:
        print('push() OK')
    else:
        return 'Fail _push()'

    try:
        p.push(4)
    except ValueError:
        print('push() OK')
    else:
        return 'Fail push()'

    if p.count() != 1:
        return 'Fail count()'
    if p.pull() != 2:
        return 'Fail pull()'
    p.clear()
    if p.count() != 0:
        return 'Fail clear()'
    if p.__str__() != 'Stack<int>':
        return 'Fail __str__()'
    if p.type != 'Stack<int>':
        return 'Fail type()'
    return 'Test OK'


print(test())
