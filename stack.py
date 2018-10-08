class Stack:
    def __init__(self, data_type=object, limit=None):
        """создаю конструктор"""
        self.data_type = data_type
        self.limit = limit
        self.items = []

    def __str__(self):
        """возвращающий строку вида 'Stack<тип данных>'"""
        return 'Stack<' + str(self.data_type.__name__) + '>'

    def _push(self, element):
        """проверяет возможность добавления элемента в стэк (по лимиту и типу)"""
        if type(element) is not self.data_type:
            return 'TypeError'
        if len(self.items) == self.limit:
            return 'LimitExceedError'

    def push(self, item):
        """добавляет новый объект в стэк"""
        self.items.append(item)

    def pull(self):
        """извлекает верхний элемент стэка и возвращает его. В случае пустого стэка генерит исключение EmptyStackError"""
        if len(self.items) == 0:
            return 'EmptyStackError'
        return self.items.pop()

    def count(self):
        """возвращает количество элементов в стэке"""
        return len(self.items)

    def clear(self):
        """очищает стэк"""
        self.items = []

    def type(self):
        """возвращает тип данных стэка"""
        return self.data_type
