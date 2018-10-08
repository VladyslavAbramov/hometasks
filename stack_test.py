import stack


def test():
    p = stack.Stack(int, 1)
    if p._push(2) is not None:
        return 'Fail _push()'
    if p._push('qwerty') != 'TypeError':
        return 'Fail _push()'
    p.push(3)
    if p._push(4) != 'LimitExceedError':
        return 'Fail push()'
    if p.count() != 1:
        return 'Fail count()'
    if p.pull() != 3:
        return 'Fail pull()'
    p.push(0)
    p.clear()
    if p.count() != 0:
        return 'Fail clear()'
    if p._push('string') is None:
        return 'Fail push()'
    if p.__str__() != 'Stack<int>':
        return 'Fail __str__()'
    if p.type() is not int:
        return 'Fail type()'
    return 'Test OK'


print(test())
