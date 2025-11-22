class Task:
    def __init__(self, title, is_done = "Не выполнено"):
        self.__title = title
        self.__is_done = is_done

    def mark_done(self):
        self.__is_done = "Выполнено"

    @property
    def title(self):
        return self.__title

    @property
    def is_done(self):
        return self.__is_done

    def __str__(self):
        return f"{self.__title} - {self.__is_done}."