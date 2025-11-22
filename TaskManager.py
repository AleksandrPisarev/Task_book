from Task import Task
import json

class TaskManager:
    __tasks = list()
    def __init__(self):
        with open('source\\journal.json', 'r', encoding='utf-8') as file:
            for line in file:
                dictionary = json.loads(line)
                task = Task(dictionary['Задача'])
                if task.is_done != dictionary['Статус']:
                    task.mark_done()
                self.__tasks.append(task)

    def write_file(self):
        with open("source\\journal.json", "w", encoding="utf-8") as file:
            for i in self.__tasks:
                dictionary = {"Задача": i.title, "Статус": i.is_done}
                json.dump(dictionary, file,  ensure_ascii=False)
                file.write("\n")


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
