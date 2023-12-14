import random
from datetime import datetime

class User:
    def __init__(self, ID, Haslo):
        self.ID = ID
        self.Haslo = Haslo
        self.Saldo = random.randint(0, 20000)
        self.transaction_history = []
        self.logged = False

def powitanie():
    print("Witaj w Banku!")

def logowanie(uzytkownik):
    login = input("Podaj login: ")
    if login == uzytkownik.ID:
        password = input("Podaj hasło: ")
        if password == uzytkownik.Haslo:
            print("Zalogowano pomyślnie!")
            uzytkownik.logged = True
        else:
            print(f"Dla loginu {login} nie pasuje hasło.")
            choice = input("Czy chcesz spróbować jeszcze raz? y/n: ")
            if choice.lower() == "y":
                logowanie(uzytkownik)
    else:
        print("Nie znaleziono loginu.")
        choice = input("Czy chcesz spróbować jeszcze raz? y/n: ")
        if choice.lower() == "y":
            logowanie(uzytkownik)
        else:
            print(f"Dla loginu {login} nie pasuje hasło.")

def stanKonta(uzytkownik):
    print("Twój stan konta wynosi:", uzytkownik.Saldo)
    return uzytkownik.Saldo

def wyplacSrodki(uzytkownik):
    stanKonta(uzytkownik)
    typ = "Wypłata"
    data = datetime.now()
    value = int(input("Podaj ile środków chciałbyś wypłacić: "))
    if value <= uzytkownik.Saldo:
        uzytkownik.Saldo -= value
        kwota = value
        dodajTransakcje(uzytkownik, typ, kwota, data)
        stanKonta(uzytkownik)
    else:
        print("Nie masz wystarczających środków na koncie.")

def displayMenu():
    print("1. WYŚWIETL SALDO KONTA\n2. WYPLAC SRODKI\n3. WPLAC SRODKI\n4. HISTORIA TRANSAKCJI")

def wplacSrodki(uzytkownik):
    stanKonta(uzytkownik)
    typ = "Wpłata"
    data = datetime.now()
    value = int(input("Podaj ile środków chciałbyś wpłacić: "))
    uzytkownik.Saldo += value
    kwota = value
    dodajTransakcje(uzytkownik, typ, kwota, data)
    stanKonta(uzytkownik)

def dodajTransakcje(uzytkownik, typ, kwota, data):
    transaction = {"typ": typ, "kwota": kwota, "data": data}
    uzytkownik.transaction_history.append(transaction)

def pokazTransakcje(uzytkownik):
    for transakcja in uzytkownik.transaction_history:
        typ = transakcja["typ"]
        kwota = transakcja["kwota"]
        data = transakcja["data"]
        print(f"Typ: {typ}, Kwota: {kwota}, Data: {data}")

def userChoice(uzytkownik, value):
    match value:
        case 1:
            stanKonta(uzytkownik)
        case 2:
            wyplacSrodki(uzytkownik)
        case 3:
            wplacSrodki(uzytkownik)
        case 4:
            pokazTransakcje(uzytkownik)

Adam = User("Adam", "XYZ")
while True:
    if not Adam.logged:
        powitanie()
        logowanie(Adam)
    else:
        displayMenu()
        choice = input("Wprowadź wartość (1, 2, 3, 4), lub wpisz 'exit' aby wyjść z programu: ")

        if choice == 'exit':
            break
        userChoice(Adam, int(choice))
