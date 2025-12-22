#Реализация односвязного списка


from typing import Any, Iterator, Optional


class Node:
    """Узел односвязного списка"""
    
    def __init__(self, value: Any, next_node: Optional['Node'] = None) -> None:
        self.value = value
        self.next = next_node
    
    def __repr__(self) -> str:
        return f"[{self.value}]"


class SinglyLinkedList:
    """Односвязный список"""
    
    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self._size: int = 0
    
    def append(self, value: Any) -> None:
        """
        Добавить элемент в конец списка.
        Сложность: O(1) с tail, O(n) без tail
        """
        new_node = Node(value)
        
        if self.head is None:
            # Список пуст
            self.head = new_node
            self.tail = new_node
        else:
            # Добавляем после tail
            self.tail.next = new_node
            self.tail = new_node
        
        self._size += 1
    
    def prepend(self, value: Any) -> None:
        """
        Добавить элемент в начало списка.
        Сложность: O(1)
        """
        new_node = Node(value, self.head)
        self.head = new_node
        
        if self.tail is None:
            # Список был пуст
            self.tail = new_node
        
        self._size += 1
    
    def insert(self, idx: int, value: Any) -> None:
        """
        Вставить элемент по индексу.
        Сложность: O(n) в худшем случае
        
        Raises:
            IndexError: если индекс вне диапазона
        """
        if idx < 0 or idx > self._size:
            raise IndexError(f"Index {idx} out of range [0, {self._size}]")
        
        if idx == 0:
            # Вставка в начало
            self.prepend(value)
        elif idx == self._size:
            # Вставка в конец
            self.append(value)
        else:
            # Вставка в середину
            current = self.head
            for _ in range(idx - 1):
                current = current.next
            
            new_node = Node(value, current.next)
            current.next = new_node
            self._size += 1
    
    def remove(self, value: Any) -> bool:
        """
        Удалить первое вхождение значения.
        Сложность: O(n)
        
        Returns:
            bool: True если элемент был удалён, False если не найден
        """
        if self.head is None:
            return False
        
        # Удаление из начала
        if self.head.value == value:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self._size -= 1
            return True
        
        # Поиск и удаление из середины или конца
        current = self.head
        while current.next is not None:
            if current.next.value == value:
                current.next = current.next.next
                if current.next is None:
                    self.tail = current
                self._size -= 1
                return True
            current = current.next
        
        return False
    
    def remove_at(self, idx: int) -> Any:
        """
        Удалить элемент по индексу.
        Сложность: O(n)
        
        Returns:
            Значение удалённого элемента
            
        Raises:
            IndexError: если индекс вне диапазона
        """
        if idx < 0 or idx >= self._size:
            raise IndexError(f"Index {idx} out of range [0, {self._size})")
        
        if idx == 0:
            # Удаление из начала
            value = self.head.value
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self._size -= 1
            return value
        
        # Удаление из середины или конца
        current = self.head
        for _ in range(idx - 1):
            current = current.next
        
        value = current.next.value
        current.next = current.next.next
        
        if current.next is None:
            self.tail = current
        
        self._size -= 1
        return value
    
    def __iter__(self) -> Iterator[Any]:
        """Итератор по значениям списка"""
        current = self.head
        while current is not None:
            yield current.value
            current = current.next
    
    def __len__(self) -> int:
        """Количество элементов в списке"""
        return self._size
    
    def __repr__(self) -> str:
        """Строковое представление списка"""
        values = list(self)
        return f"SinglyLinkedList({values})"
    
    def visual_repr(self) -> str:
        """Визуальное представление связей между узлами"""
        if self.head is None:
            return "None"
        
        parts = []
        current = self.head
        while current is not None:
            parts.append(f"[{current.value}]")
            current = current.next
        parts.append("None")
        
        return " -> ".join(parts)