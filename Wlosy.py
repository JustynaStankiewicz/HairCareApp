import pandas as pd

slownik = {"PEH": "Akronim P-Proteiny, E-Emolienty, H-Humektanty",
           "Emolienty": "Element składający się na równowagę PEH,tworzą warstwę ochronną, wygładzają, dociążają, np oleje",
           "baby hair": "nowo wyrastające włoski, które mierzą zazwyczaj od 1 do 4 cm",
           "B/S": "skrót od bez spłukiwania. Innym terminem określającym odżywkę bez spłukiwania to leave in"}

emolienty_name = "emolienty_skladniki.csv"
data_e = pd.read_csv(emolienty_name)

humektanty_name = "humektanty_sklaniki.csv"
data_h = pd.read_csv(humektanty_name)

proteiny_name = "proteiny_skladniki.csv"
data_p = pd.read_csv(proteiny_name)


def wyswietl_slownik(tytul, slownik):
    print(tytul)
    for key, value in slownik.items():
        print(key, " : ", value)


def znajdz_w_slowniku(slownik, pojecie):
    print(slownik.get(pojecie))


def czy_zawiera(kolekcja, nazwa):
    for i in kolekcja:
        if str(kolekcja[i]).__contains__(nazwa):
            return True


def znajdz_typ_skladniku():
    ingredient_name = input('Wpisz szukany składnik: ')
    if (czy_zawiera(data_e, ingredient_name)):
        print("Skladnik ten nalezy do grupy emolientow")
    elif (czy_zawiera(data_h, ingredient_name)):
        print("Skladnik ten nalezy do grupy humektantow")
    elif (czy_zawiera(data_p, ingredient_name)):
        print("Skladnik ten nalezy do grupy protein")
    else:
        print("Skladnik nie wystepuje w naszej bazie!")


def rownowaga_peh_quiz():
    proteiny = 0
    emolienty = 0
    humektanty = 0

    suche = input('Czy twoje wlosy sa suche?(tak/nie): ')
    matowe = input('Czy twoje wlosy sa matowe?(tak/nie): ')
    pozbawione_objetosci = input('Czy twoje wlosy sa pozbawione objetosci?(tak/nie): ')
    puszace_sie = input('Czy twoje wlosy sa puszace sie?(tak/nie): ')
    skoltunione = input('Czy twoje wlosy sa sklonne do placzeniasie lub koltunienia?(tak/nie): ')
    pozbawione_blasku = input('Czy twoje wlosy sa  pozbawione blasku?(tak/nie): ')

    if (suche == 'tak'):
        proteiny = proteiny + 1
        emolienty = emolienty - 1
    if (matowe == 'tak'):
        proteiny = proteiny + 1
        humektanty = humektanty - 1
    if (pozbawione_objetosci == 'tak'):
        proteiny = proteiny - 1
        emolienty = emolienty + 1
    if (puszace_sie == 'tak'):
        emolienty = emolienty - 1
        humektanty = humektanty + 1
    if (skoltunione == 'tak'):
        emolienty = emolienty - 1
        humektanty = humektanty + 1
    if (matowe == 'tak'):
        proteiny = proteiny - 1
        emolienty = emolienty - 1

    if (proteiny > 0):
        print("Uzywasz za duzo protein")
    elif (proteiny < 0):
        print("Uzywasz za malo protein.")
    if (emolienty > 0):
        print("Uzywasz za duzo emolientów")
    elif (emolienty < 0):
        print("Uzywasz za malo emolientów.")
    if (humektanty > 0):
        print("Uzywasz za duzo humektantów")
    elif (humektanty < 0):
        print("Uzywasz za malo humektantów")


def main():
    wyswietl_slownik("Słownik pojęć", slownik)
    znajdz_w_slowniku(slownik, "PEH")
    print(data_e)
    print(data_h)
    print(data_p)
    znajdz_typ_skladniku()
    rownowaga_peh_quiz()


if __name__ == '__main__':
    main()
