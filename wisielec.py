import random
# Lista słów, które komputer może wybrać
slowa = ["python", "programowanie", "komputer", "programista", "inteligencja"]
# Wybieranie losowego słowa z listy
slowo = random.choice(slowa)
slowo_lista = list(slowo)
ukryte_slowo = ['*' for _ in slowo_lista]
maksymalna_proba = 5
liczba_prob = 0
litery_wprowadzone = []

while liczba_prob < maksymalna_proba:
    print(''.join(ukryte_slowo))

    litera = input("Podaj literę: ").lower()

    # Sprawdź, czy litera jest już wprowadzona
    if litera in litery_wprowadzone:
        print("Ta litera została już wprowadzona.")
        continue

    # Dodaj literę do listy wprowadzonych liter
    litery_wprowadzone.append(litera)

    # Sprawdź, czy litera jest w słowie
    if litera in slowo_lista:
        print("Poprawna litera!")
        for i, litera_slowa in enumerate(slowo_lista):
            if litera_slowa == litera:
                ukryte_slowo[i] = litera
    else:
        print("Błędna litera!")
        liczba_prob += 1

    # Sprawdź, czy gracz odgadł słowo
    if ''.join(ukryte_slowo) == slowo:
        print(f"Gratulacje! Odgadłeś słowo: {slowo}")
        break

# Jeśli gracz nie odgadł słowa
if liczba_prob == maksymalna_proba:
    print(f"Przegrałeś! Słowo to: {slowo}")