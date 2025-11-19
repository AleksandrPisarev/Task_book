class Task:
    __is_done = "Не выполнено"
    def __init__(self, title):
        self.__title = title

    def mark_done(self):
        self.__is_done = "Выполнено"

    @property
    def title(self):
        return self.__title

    def __str__(self):
        return f"{self.__title} - {self.__is_done}."