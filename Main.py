# Менеджер задач
# Задача: Создай класс Task, который позволяет управлять задачами (делами). У задачи должны быть атрибуты: описание задачи,
# срок выполнения и статус (выполнено/не выполнено). Реализуй функцию для добавления задач, отметки выполненных задач и
# вывода списка текущих (не выполненных) задач.

class Task():
    def __init__(self, description, time):
        self.description = description
        self.time = time
        self.completed = False
    def mark_as_completed(self):
        self.completed = True
    def display(self):
        status = "Выполнено" if self.completed else "Не выполнено"
        return f"{self.description}(Срок: {self.time}) - {status}"
class Task_Manager:
    def __init__(self):
        self.task =[]
    def add_task(self, description, time):
        self.task.append(Task(description, time))
    def mark_task_completed(self, task_index):
        if 0 <= task_index < len(self.task):
            self.task[task_index].mark_as_completed()
        else:
            print("задачи с таким индексом не существует")
    def get_current_tasks(self):
        return [task for task in self.task if not task.completed]

    def display_tasks(self):
        for task in self.task:
            print(task.display())

task_manager = Task_Manager()
task_manager.add_task("Вынести мусор", "11.05.2024")
task_manager.add_task("Купить продукты","11.05.2024")
task_manager.add_task("Приготовить ужин", "12.05.2024")



task_manager.mark_task_completed(1)

print("Все задачи:")
task_manager.display_tasks()
print("\nТекущие задачи:")
current_tasks = task_manager.get_current_tasks()
for task in current_tasks:
    print(task.display())