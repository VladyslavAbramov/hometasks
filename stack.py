class Stack:

    def __init__(self, data_type=object, limit=None):
        """создаю конструктор"""
        self.data_type = data_type
        self.limit = limit
        self.items = []

    def __str__(self):
        """возвращающий строку вида 'Stack<тип данных>'"""
        return 'Stack<' + str(self.data_type.__name__) + '>'

    def _push(self, item):
        if type(item) is not self.data_type:
            raise ValueError('TypeError')
        if len(self.items) == self.limit:
            raise ValueError('LimitExceedError')

    def push(self, item):
        """проверяет возможность добавления элемента в стэк (по лимиту и типу),
            если это возможно - добавляет новый объект в стэк"""
        self._push(item)
        self.items.append(item)

    def pull(self):
        """извлекает верхний элемент стэка и возвращает его.
            В случае пустого стэка генерит исключение EmptyStackError"""
        if len(self.items) == 0:
            raise ValueError('EmptyStackError')
        return self.items.pop()

    def count(self):
        """возвращает количество элементов в стэке"""
        return len(self.items)

    def clear(self):
        """очищает стэк"""
        self.items = []

    @property
    def type(self):
        """возвращает тип данных стэка"""
        return self.data_type
