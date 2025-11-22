from unittest import case

from TaskManager import*

def menu(journal):
    try:
        _choice = input(
    '''
    Выберите действие:
    add - добавить новую задачу
    done - отметить задачу как выполненную
    show - вывести список задач
    exit - сохранить данные в файл и завершить программу
    '''
        )
        if _choice not in ["add", "done", "show", "exit"]:
            raise Exception
    except:
        print("Введена не коректная команда. Выберите команду из списка.")
        menu(journal)
    match _choice:
        case "add": journal.add_task(input("Введите название задачи: "))
        case "done": journal.mark_task_done(input("Введите название задачи: "))
        case "show": print(journal)
        case "exit":
                    journal.write_file()
                    print("Данные сохранены. Программа завершена.")
                    exit()

if __name__ == "__main__":
    journal = TaskManager()
    while True:
        menu(journal)