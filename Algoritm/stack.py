class Stack:
    def __init__(self, lst=None):
        self.lst = lst if lst is not None else []
        
    def push(self, value):
        self.lst.append(value)

    def pop(self):
        if self.is_empty():
            raise IndexError("Удаление из пустого стека")
        else:
            return self.lst.pop()

    def is_empty(self):
        return len(self.lst) == 0
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Просмотр верхнего элемента из пустого стека")
        else:
            return self.lst[-1]

    def size(self):
        return len(self.lst)
