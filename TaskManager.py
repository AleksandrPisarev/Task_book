from Task import Task

class TaskManager:
    __tasks = list()
    def __init__(self):
        pass

    def __del__(self):
        pass

    def add_task(self, title):
        self.__tasks.append(Task(title))
        print(f"Задача '{title}' добавлена.")

    def mark_task_done(self, title):
        for i in self.__tasks:
            if i.title == title:
                i.mark_done()
                return print(f"Задача '{title}' отмечена как выполненная.")
        return print(f"Задача '{title}' в списке не значится.")

    def __str__(self):
        if len(self.__tasks) == 0:
            return "В списке нет задач."
        else:
            list_task = ""
            count = 1
            for i in self.__tasks:
                list_task += str(count) + ". " + str(i) + "\n"
                count += 1
            return f"{list_task}"
