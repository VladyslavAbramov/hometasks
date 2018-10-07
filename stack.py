class Stack:
    def __init__(self, data_type=object, limit=None):
        self.data_type = data_type
        self.limit = limit
        self.items = []

    def _push(self, element):
        """проверяет возможность добавления элемента в стэк (по лимиту и типу)"""
        if type(element) is not self.data_type:
            return 'TypeError'
        if len(self.items) == self.limit:
            return 'LimitExceedError'

    def push(self, item):
        self.items.append(item)

    def pull(self):
        if len(self.items) == 0:
            return 'EmptyStackError'
        return self.items.pop()

    def count(self):
        return len(self.items)

    def clear(self):
        self.items = []

    def type(self):
        return type(self.items[0])

    def __str__(self):
        return 'Stack' + str(self.data_type)




p = Stack(int, 1)
print(p._push(2))
print(p.push(3))
print(p.push(4))
print(p.count())
print(p.__str__())
print(p.clear())
print(p.count())
print(p._push(2))
print(p.push(2))
print(p._push(2))
print(p._push(False))
print(p)


