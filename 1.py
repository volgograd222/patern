class DataBase:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, user, psw, port):
            self.user = user
            self.psw = psw
            self.port = port

    def connect(self):
        print(f"Соединение с БД: {self.user}, {self.psw}, {self.port}")

    def close(self):
        print("Закрытие соединения с БД")

    def read(self):
        return "Данные из БД"

    def write(self, data):
        print(f"Запись в БД: {data}")

# Пример использования
db = DataBase('root', '1234', 80)
db2 = DataBase('root2', '5678', 40)

db.connect()
db2.connect()

print(id(db), id(db2))
