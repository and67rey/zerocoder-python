from datetime import datetime

class Task:
    def __init__(self):
        """Инициализация списка задач."""
        self.tasks = []

    class TaskItem:
        """Вложенный класс, представляющий отдельную задачу."""

        def __init__(self, description: str, due_date: str):
            """
            Инициализация задачи.
            :param description: Описание задачи.
            :param due_date: Срок выполнения задачи в формате 'YYYY-MM-DD'.
            """
            self.description = description
            self.due_date = datetime.strptime(due_date, '%Y-%m-%d')
            self.is_completed = False

        def mark_as_completed(self):
            """Отмечает задачу как выполненную."""
            self.is_completed = True

        def to_string(self):
            """Возвращает строковое представление задачи."""
            status = "Выполнено" if self.is_completed else "Не выполнено"
            return f"[{status}] {self.description} (до {self.due_date.strftime('%Y-%m-%d')})"

    def add_task(self, description: str, due_date: str):
        """
        Добавляет новую задачу в список.
        :param description: Описание задачи.
        :param due_date: Срок выполнения задачи в формате 'YYYY-MM-DD'.
        """
        task = self.TaskItem(description, due_date)
        self.tasks.append(task)

    def mark_task_completed(self, task_index: int):
        """
        Отмечает задачу как выполненную.
        :param task_index: Индекс задачи в списке (начиная с 0).
        """
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_as_completed()
        else:
            print("Ошибка: Неверный индекс задачи!")

    def show_pending_tasks(self):
        """Выводит все текущие (не выполненные) задачи"""
        for i, task in enumerate(self.tasks):
            if not task.is_completed:
                print(f"{i}. {task.to_string()}")  # Используем метод to_string()

    def show_tasks(self):
        """Выводит все задачи."""
        for i, task in enumerate(self.tasks):
            print(f"{i}. {task.to_string()}")  # Используем метод to_string()


# Пример использования

task_manager = Task()
task_manager.add_task("Принять участие в вебинаре", "2024-11-12")
task_manager.add_task("Сделать домашнюю работу", "2024-11-15")
task_manager.add_task("Прочитать книгу", "2024-12-01")

print("Список задач:")
task_manager.show_tasks()

n = 0
description = task_manager.tasks[n].description
print(f"\nОтмечаем задачу {description} как выполненную.")
task_manager.mark_task_completed(n)

n = 1
description = task_manager.tasks[n].description
print(f"\nОтмечаем задачу {description} как выполненную.")
task_manager.mark_task_completed(n)

print("\nТекущие задачи:")
task_manager.show_pending_tasks()
