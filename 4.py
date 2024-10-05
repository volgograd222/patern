from abc import ABC, abstractmethod

class User(ABC):
    @abstractmethod
    def get_permissions(self):
        pass
class AdminUser(User):
    def get_permissions(self):
        return "Полные права доступа: чтение, запись, удаление, управление пользователями."

class ManagerUser(User):
    def get_permissions(self):
        return "Права доступа: чтение, запись, управление проектами."

class GuestUser(User):
    def get_permissions(self):
        return "Ограниченные права доступа: только чтение."
class UserFactory:
    @staticmethod
    def create_user(user_type):
        if user_type == 'admin':
            return AdminUser()
        elif user_type == 'manager':
            return ManagerUser()
        elif user_type == 'guest':
            return GuestUser()
        else:
            raise ValueError(f"Неизвестный тип пользователя: {user_type}")
def main():
    # Создаем различных пользователей через фабрику
    users = [
        UserFactory.create_user('admin'),
        UserFactory.create_user('manager'),
        UserFactory.create_user('guest'),
    ]

    # Проверяем права доступа для каждого пользователя
    for user in users:
        print(f"{user.__class__.__name__}: {user.get_permissions()}")

if __name__ == "__main__":
    main()
