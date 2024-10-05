from abc import ABC, abstractmethod

# Абстракция транзакции
class Transaction(ABC):
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    @abstractmethod
    def execute(self):
        pass

# Реализация банковского перевода
class BankTransfer(Transaction):
    def execute(self):
        print(f"Bank Transfer: {self.amount} {self.currency}")

# Реализация перевода через мобильное приложение
class MobileAppTransfer(Transaction):
    def execute(self):
        print(f"Mobile App Transfer: {self.amount} {self.currency}")

# Сценарий использования
def main():
    # Создание и выполнение транзакций
    bank_transfer = BankTransfer(100, "USD")
    bank_transfer.execute()

    mobile_transfer = MobileAppTransfer(150, "EUR")
    mobile_transfer.execute()

if __name__ == "__main__":
    main()
