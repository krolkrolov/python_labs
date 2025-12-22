"""
Простые тесты для лабораторной работы 10
"""

from structures import Stack, Queue
from linked_list import SinglyLinkedList


def test_stack():
    """Тестирование стека"""
    print("=== Тестирование Stack ===")
    s = Stack()
    
    # Добавляем элементы
    s.push(1)
    s.push(2)
    s.push(3)
    print(f"После push(1,2,3): {s}")
    print(f"Peek: {s.peek()}")
    print(f"Длина: {len(s)}")
    
    # Удаляем элементы
    print(f"Pop: {s.pop()}")
    print(f"Pop: {s.pop()}")
    print(f"После двух pop: {s}")
    print(f"Пустой ли? {s.is_empty()}")
    
    # Очищаем
    s.pop()
    print(f"После очистки: пустой={s.is_empty()}")
    
    # Проверка исключения
    try:
        s.pop()
    except IndexError as e:
        print(f"Исключение при пустом стеке: {e}")
    
    print()


def test_queue():
    """Тестирование очереди"""
    print("=== Тестирование Queue ===")
    q = Queue()
    
    # Добавляем элементы
    q.enqueue("A")
    q.enqueue("B")
    q.enqueue("C")
    print(f"После enqueue(A,B,C): {q}")
    print(f"Peek: {q.peek()}")
    print(f"Длина: {len(q)}")
    
    # Удаляем элементы
    print(f"Dequeue: {q.dequeue()}")
    print(f"Dequeue: {q.dequeue()}")
    print(f"После двух dequeue: {q}")
    print(f"Пустой ли? {q.is_empty()}")
    
    # Очищаем
    q.dequeue()
    print(f"После очистки: пустой={q.is_empty()}")
    
    # Проверка исключения
    try:
        q.dequeue()
    except IndexError as e:
        print(f"Исключение при пустой очереди: {e}")
    
    print()


def test_linked_list():
    """Тестирование связного списка"""
    print("=== Тестирование SinglyLinkedList ===")
    lst = SinglyLinkedList()
    
    # Добавляем элементы
    lst.append(10)
    lst.append(20)
    lst.append(30)
    print(f"После append(10,20,30): {lst}")
    print(f"Визуально: {lst.visual_repr()}")
    
    # Добавляем в начало
    lst.prepend(5)
    print(f"После prepend(5): {lst}")
    print(f"Визуально: {lst.visual_repr()}")
    
    # Вставляем по индексу
    lst.insert(2, 15)
    print(f"После insert(2, 15): {lst}")
    print(f"Визуально: {lst.visual_repr()}")
    
    # Удаляем по значению
    lst.remove(20)
    print(f"После remove(20): {lst}")
    
    # Удаляем по индексу
    removed = lst.remove_at(1)
    print(f"После remove_at(1) (удалено {removed}): {lst}")
    
    # Итерация
    print("Итерация по списку:", end=" ")
    for item in lst:
        print(item, end=" ")
    print()
    
    print(f"Длина списка: {len(lst)}")
    print()


def benchmark():
    """Простой бенчмарк"""
    print("=== Простой бенчмарк (1000 операций) ===")
    
    import time
    
    # Stack бенчмарк
    s = Stack()
    start = time.time()
    for i in range(1000):
        s.push(i)
    for _ in range(1000):
        s.pop()
    stack_time = time.time() - start
    
    # Queue бенчмарк
    q = Queue()
    start = time.time()
    for i in range(1000):
        q.enqueue(i)
    for _ in range(1000):
        q.dequeue()
    queue_time = time.time() - start
    
    # LinkedList бенчмарк (только append)
    lst = SinglyLinkedList()
    start = time.time()
    for i in range(1000):
        lst.append(i)
    linked_list_time = time.time() - start
    
    print(f"Stack (1000 push+pop): {stack_time:.6f} сек")
    print(f"Queue (1000 enqueue+dequeue): {queue_time:.6f} сек")
    print(f"LinkedList (1000 append): {linked_list_time:.6f} сек")
    print()


def demo_for_screenshots():
    """Демонстрация для создания скриншотов"""
    print("="*50)
    print("ДЕМОНСТРАЦИЯ ДЛЯ СКРИНШОТОВ")
    print("="*50)
    
    print("\n1. Создание и работа со стеком:")
    print("-" * 30)
    s = Stack()
    s.push("первый")
    s.push("второй")
    s.push("третий")
    print(f"stack = Stack()")
    print(f"stack.push('первый')")
    print(f"stack.push('второй')")
    print(f"stack.push('третий')")
    print(f"stack.peek() = {s.peek()}")
    print(f"stack.pop() = {s.pop()}")
    print(f"stack.pop() = {s.pop()}")
    print(f"Теперь stack = {s}")
    
    print("\n2. Создание и работа с очередью:")
    print("-" * 30)
    q = Queue()
    q.enqueue("Иван")
    q.enqueue("Мария")
    q.enqueue("Петр")
    print(f"queue = Queue()")
    print(f"queue.enqueue('Иван')")
    print(f"queue.enqueue('Мария')")
    print(f"queue.enqueue('Петр')")
    print(f"queue.peek() = {q.peek()}")
    print(f"queue.dequeue() = {q.dequeue()}")
    print(f"queue.dequeue() = {q.dequeue()}")
    print(f"Теперь queue = {q}")
    
    print("\n3. Создание и работа со связным списком:")
    print("-" * 30)
    lst = SinglyLinkedList()
    lst.append(100)
    lst.append(200)
    lst.prepend(50)
    print(f"lst = SinglyLinkedList()")
    print(f"lst.append(100)")
    print(f"lst.append(200)")
    print(f"lst.prepend(50)")
    print(f"lst = {lst}")
    print(f"lst.visual_repr() = {lst.visual_repr()}")
    print(f"len(lst) = {len(lst)}")
    
    print("\n" + "="*50)
    print("Готово для скриншотов!")
    print("="*50)


def main():
    """Главная функция"""
    print("Лабораторная работа 10: Тестирование структур данных")
    print()
    
    # Выбираем что тестировать
    test_all = input("Тестировать все? (y/n): ").lower() == 'y'
    
    if test_all:
        test_stack()
        test_queue()
        test_linked_list()
        benchmark()
    else:
        print("\nВыберите что тестировать:")
        print("1 - Stack")
        print("2 - Queue")
        print("3 - SinglyLinkedList")
        print("4 - Бенчмарк")
        print("5 - Демо для скриншотов")
        print("6 - Всё сразу")
        
        choice = input("Ваш выбор (1-6): ")
        
        if choice == '1':
            test_stack()
        elif choice == '2':
            test_queue()
        elif choice == '3':
            test_linked_list()
        elif choice == '4':
            benchmark()
        elif choice == '5':
            demo_for_screenshots()
        elif choice == '6':
            test_stack()
            test_queue()
            test_linked_list()
            benchmark()
        else:
            print("Неверный выбор")
    
    input("\nНажмите Enter для выхода...")


if __name__ == "__main__":
    main()