from Wlosy import Wlosy




class Zarzadzanie:
    def __init__(self, funkcje):
        self._funkcje=funkcje

    @property
    def funkcje(self):
        return self._funkcje

    @funkcje.setter
    def funkcje(self, wartosc):
        self._funkcje=wartosc

    def panel_wyboru_funkcji(self):
        funkcja =-1

        while funkcja !=8:
            if funkcja==1:
                self.funkcje.wyswietl_slownik()
            if funkcja==2:
                self.funkcje.znajdz_w_slowniku()
            if funkcja==3:
                self.funkcje.porowatosc_quiz()
            if funkcja==4:
                self.funkcje.rownowaga_peh_quiz()
            if funkcja==5:
                self.funkcje.znajdz_typ_skladnika()
            if funkcja==6:
                self.funkcje.sprawdz_sklad()
            if funkcja==7:
                self.funkcje.dobierz_produkt()

            funkcja = int(input("Wybierz funkcję, która cię interesuje:\n"
                                  "1 - Wyświetl słownik pojęć\n"
                                  "2 - Znajdź pojęcie w słowniku\n"
                                  "3 - Quiz: Poznaj swoją porowatość\n"
                                  "4 - Quiz:  Potrzeby twoich włosów\n"
                                  "5 - Znajdź typ składnika\n"
                                  "6 - Analiza składu\n"
                                  "7 - Przykładowe produkty do wybranych porowatości\n"
                                  "8 - Koniec\n"
                                  "Wybór: "))

