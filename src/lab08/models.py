from dataclasses import dataclass
from datetime import datetime, date
from typing import Optional

@dataclass
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float
    
    def __post_init__(self):
        """Валидация данных после инициализации"""
        # Валидация формата даты
        try:
            datetime.strptime(self.birthdate, "%Y-%m-%d")
        except ValueError:
            raise ValueError(f"Некорректный формат даты: {self.birthdate}. Ожидается YYYY-MM-DD")
        
        # Валидация GPA
        if not (0 <= self.gpa <= 5):
            raise ValueError(f"GPA должен быть в диапазоне от 0 до 5, получено: {self.gpa}")
        
        # Валидация ФИО (минимум 2 слова)
        name_parts = self.fio.strip().split()
        if len(name_parts) < 2:
            raise ValueError(f"ФИО должно содержать минимум имя и фамилию: {self.fio}")
    
    def age(self) -> int:
        """Вычисление возраста в полных годах"""
        birth_date = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        today = date.today()
        
        # Вычисляем разницу в годах
        age = today.year - birth_date.year
        
        # Корректируем если день рождения в этом году еще не наступил
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1
        
        return age
    
    def to_dict(self) -> dict:
        """Сериализация объекта в словарь"""
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Student':
        """Десериализация из словаря"""
        return cls(
            fio=data["fio"],
            birthdate=data["birthdate"],
            group=data["group"],
            gpa=data["gpa"]
        )
    
    def __str__(self) -> str:
        """Строковое представление объекта"""
        return f"Студент: {self.fio}, Группа: {self.group}, GPA: {self.gpa:.2f}, Возраст: {self.age()} лет"
    
    def is_excellent(self) -> bool:
        """Проверка, является ли студент отличником"""
        return self.gpa >= 4.55
    
    def study_year(self) -> int:
        """Определение курса обучения на основе группы"""
        try:
            # Пытаемся найти цифры в названии группы
            import re
            numbers = re.findall(r'\d+', self.group)
            if numbers:
                # Берем первое число
                num = int(numbers[0])
                # Если число двузначное или трехзначное, берем первую цифру
                if num >= 10:
                    return int(str(num)[0])
                else:
                    return 1  # Если однозначное число
        except:
            pass
        return 1  # По умолчанию первый курс