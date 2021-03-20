from enum import Enum
import threading


class AccountStatus(Enum):
    Open = "Open"
    Close = "Close"
    Processing = "Processing"


def ensure_open_account(func):
    def _decorator(self, *args, **kwargs):
        if self.status != AccountStatus.Open:
            raise ValueError("Closed Account")
        return func(self, *args, **kwargs)

    return _decorator


class BankAccount:
    def __init__(self):
        self.status = AccountStatus.Close
        self.balance = 0
        self.lock = threading.Lock()

    @ensure_open_account
    def get_balance(self):
        return self.balance

    def open(self):
        if self.status == AccountStatus.Open:
            raise ValueError("Account already open.")
        self.status = AccountStatus.Open

    @ensure_open_account
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError(f"Wrong Amount => {amount}.")
        with self.lock:
            self.balance += amount

    @ensure_open_account
    def withdraw(self, amount):
        if amount <= 0 or amount > self.balance:
            raise ValueError(
                f"Wrong Amount => {amount}, current balance: {self.balance}."
            )
        with self.lock:
            self.balance -= amount

    @ensure_open_account
    def close(self):
        self.balance = 0
        self.status = AccountStatus.Close
