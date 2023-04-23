class Client:
    def __init__(self, name, age, phone):
        self.name = name
        self.age = age
        self.phone = phone

    def __str__(self):
        return f"Jméno: {self.name}\nVěk: {self.age}\nVěk: {self.phone}"

def main():
    clients = []

    while True:
        print("\n1. Nový klient\n2. Seznam klientů\n3. Vyhledat klienta\n4. Konec \n")

        choice = input("Zadejte volbu (1/2/3): ")

        if choice == "1":
            name = input("Zadejte jméno: ")
            age = int(input("Zadejte věk: "))
            phone = input("Zadejte tel. číslo: ")
            client = Client(name, age, phone)
            clients.append(client)
            print("\nNový klient úspěšně přidán.\n")

        elif choice == "2":
            if not clients:
                print("\nŽádní dostupní klienti.\n")
            else:
                for i, client in enumerate(clients):
                    print(f"ID {i+1}:\n{client}\n- - - - - - - - - - - - -\n")
        elif choice == "3":
            name = input("Zadejte celé jméno: ")
            found_clients = [client for client in clients if client.name == name]
            if not found_clients:
                print("Klient nenalezen.\n")
            else:
                for i, client in enumerate(found_clients):
                    print(f"ID {i+1}:\n{client}\n- - - - - - - - - - - - -\n")
        elif choice == "4":
            break
        else:
            print("\n Neplatná volba (1/2/3).\n")

if __name__ == "__main__":
    main()