class IINnotFoundError(Exception):
    message = 'Пользователь с таким ИИН не найден'

    def __str__(self):
        return self.message

class IINfound(Exception):
    message = 'Пользователь с таким ИИН уже существует'

    def __str__(self):
        return self.message
