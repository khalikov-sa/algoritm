import time


class Queue:
    def __init__(self, items=None):
        self.items = items if items is not None else []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Удаление из пустой очереди")
        
    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Просмотр из пустой очереди")

    def size(self):
        return len(self.items)
    
def process_tasks(tasks):
    # Создаем очередь и добавляем все задачи
    queue = Queue()
    for task in tasks:
        queue.enqueue(task)
    
    current_time = 0
    completion_times = []
    
    # Обрабатываем задачи, пока очередь не пуста
    while not queue.is_empty():
        task_id, duration = queue.dequeue()
        start_time = current_time
        current_time = start_time + duration
        completion_times.append((task_id, current_time))
    
    return completion_times


# Пример списка задач: (идентификатор, время выполнения)
tasks = [
    (1, 5),
    (2, 3),
    (3, 7),
    (4, 2)
]

# Обрабатываем задачи и выводим результат
print("Процесс обработки задач:")
results = process_tasks(tasks)
for task_id, completion_time in results:
    print(f"Задача {task_id} завершена в момент времени {completion_time}")