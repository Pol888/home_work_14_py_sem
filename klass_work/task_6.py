import json


class User:

    def __init__(self, name, i_d, access_level=None):
        self.name = name
        self.id = i_d
        self.access_level = access_level

    def __str__(self):
        return f'Имя - {self.name}, id - {self.id}, уровень доступа - {self.access_level}'

    def __eq__(self, other):
        return self.name == other.name and self.id == other.id

    def __hash__(self):
        return hash((self.name, self.id))


# ------------------------------------------------------------------------------------------------------------

class Project:

    def __init__(self, file_name, sys_access_level=1):
        self.file_name = file_name
        self.lots_of_users: set = self.__loading_data()
        self.sys_access_level = sys_access_level
        self.system_users: list = []

    def __loading_data(self) -> set:
        with open(self.file_name, 'r', encoding='utf-8') as f:
            res_f: list = json.load(f)
            result: set[User] = set()
            for i in res_f:
                result.add(User(i['name'], i['id'], i['access_level']))
            return result

    def log_in_to_the_system(self):
        f = False
        while not f:
            print("Вход в систему....\n")
            name = input("Введите имя пользователя: ")
            i_d = input("Введите id пользователя: ")
            user_sys = None
            for i in self.lots_of_users:
                if i == User(name, i_d):
                    user_sys = i
            if isinstance(user_sys, User):
                self.__to_add_a_user(user_sys)
                f = True
            else:
                raise AccessError(name, i_d)

    def __to_add_a_user(self, user: User):
        if int(user.access_level) < self.sys_access_level:
            raise LevelError(user.access_level, self.sys_access_level)
        else:
            print("Пользователь в системе")
            self.system_users.append(user)


# ------------------------------------------------------------------------------------Errors_class
class MyFavoriteErrors(Exception):
    pass


class LevelError(MyFavoriteErrors):
    def __new__(cls, user_level, allowed_level):
        cls.user_level = user_level
        cls.allowed_level = allowed_level
        return super().__new__(cls)

    def __str__(self):
        return f'Ваш уровень доступа {self.user_level} меньше разрешенного {self.allowed_level}'


class AccessError(MyFavoriteErrors):
    def __new__(cls, name, i_d):
        cls.name = name
        cls.i_d = i_d
        return super().__new__(cls)

    def __str__(self):
        return f'Пользователя с именем {self.name} с id {self.i_d} не существует в базе'
