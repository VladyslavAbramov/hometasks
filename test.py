import lesson1

def test():
    if lesson1.get_ascii('qwerty') == (113, 119, 101, 114, 116, 121):
        print('OK')
    else:
        print('NOT OK')

test()