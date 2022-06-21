import pandas as pd

from WlosyProbne import data_e


class Wlosy:
    def __init__(self):
        self.cechy=None

    @property
    def cechy(self):
        return self._cechy
    @cechy.setter
    def cechy(self,v):
        self._cechy=v

    slownik = {"baby hair": "nowo wyrastające włoski, które mierzą zazwyczaj od 1 do 4 cm",
               "B/S": "skrót od bez spłukiwania. Innym terminem określającym odżywkę bez spłukiwania to leave in",
               "bad hair day": "zły włosowy dzień, czyli taki, podczas którego włosy prezentują się źle lub nie chcą się układać",
               "cassia": "bezbarwna henna do włosów. Henna to zioło barwiące włosy. W składach kosmetyków widnieje jako Lawsonia Inermis Extract",
               "chelatowanie włosów": " zabieg polegający na oczyszczaniu włosów z białego osadu minerałów, które znajdują się w twardej wodzie",
               "CG": "pielęgnacja Curly Girl, czyli bezsilikonowa pielęgnacja kręconych włosów",
               "emolienty": "Element składający się na równowagę PEH,tworzą warstwę ochronną, wygładzają, dociążają, np oleje",
               "emulgowanie": "proces łączenia dwóch niemieszalnych substancji (na przykład wody i oleju) poprzez dodanie emulgatora, prowadzący do powstania trwałej emulsji",
               "glutek lniany": "inaczej żel lniany uzyskiwany poprzez zagotowanie w wodzie niezmielonych ziaren siemienia lnianego. Żel stosuje się do stylizacji włosów jako odżywkę b/s lub jako nawilżającą włosy maskę",
               "henna": "naturalny barwnik otrzymywany z liści i pędów rośliny o nazwie lawsonia bezbronna (w składach kosmetyków występuje jako Inermis Lawsonia Leaf Extract).Wraz z innymi ziołami wykorzystywany jest do nietrwałej koloryzacji włosów. Taka koloryzująca mieszanka ziół nazywana jest potocznie henną.",
               "humektanty": "substancje, które mają zdolność wiązania wody i utrzymywania wilgoci; przykłady półproduktów nawilżających: wyciąg z liścia aloesu, gliceryna, kwas hialuronowy, mleczan sodu, mocznik, sorbitol, glikol propylenowy, betaina",
               "metoda kubeczkowa": "metoda spieniania/rozcieńczania szamponu; tuż przed użyciem wlewa się porcję szamponu do kubka i rozcieńcza się go z wodą pod ciśnieniem.",
               "PEH": "Akronim P-Proteiny, E-Emolienty, H-Humektanty",
               "plopping": " (inaczej ręcznikowanie) - ostatni etap stylizacji kręconych lub falowanych włosów, dzięki któremu uzyskuje się zdefiniowany skręt i efekt push-up. Ręcznikowanie polega na specyficznym zawinięciu włosów pokrytych stylizatorem w gładki bawełniany ręcznik lub koszulkę z długimi rękawami. ",
               "płukanka": "roztwór, który używany jest tuż po umyciu włosów, do ostatniego płukania włosów. Płukanka powinna być chłodna i mieć lekko kwaśne pH, aby ściągnąć łuski włosów (uszczelnić osłonkę).",
               "proteiny": " białka, które można podzielić na proteiny wielkocząsteczkowe (proste) oraz małocząsteczkowe (hydrolizowane).",
               "przeproteinowanie": "wynik nałożenia na włosy zbyt dużej dawki protein (jednorazowo lub w wyniku systematycznej pielęgnacji). Takie włosy stają się suche, matowe i tracą elastyczność, przez co są bardziej podatne na zniszczenia.",
               "przenawilżenie": " efekt niepoprawnego stosowania substancji nawilżających. Zastosowanie zbyt dużej ilości humektantów w stosunku do emolientów. W deszczu włosy będą się puszyć i będą mokre w dotyku, a podczas suszy włosy będą suche i sztywne.",
               "skalp": "skóra głowy",
               "silikony": " substancje, które pokrywają włosy nietrwałym filmem ochronnym. Dzięki temu włosy nabierają blasku, sprężystości, przestają się puszyć i plątać, a także są chronione przed urazami oraz szkodliwym wpływem czynników atmosferycznych.",
               "wcierka": " odżywka do skóry głowy o działaniu stymulująco-wzmacniającym. Może pełnić wiele funkcji: ograniczać przetłuszczanie lub łupież, zagęszczać włosy, przyspieszać przyrost włosów czy nawilżać skórę głowy.",
               "zabezpieczanie końcówek": "zabieg polegający na pokryciu końcówek silikonowym serum lub odrobiną naturalnego oleju. Nadaje to włosom elastyczności oraz chroni przed nadmierną utratą wody i zniszczeniami"
               }

    emolienty_name = "emolienty_skladniki.csv"
    data_e = pd.read_csv(emolienty_name)

    humektanty_name = "humektanty_sklaniki.csv"
    data_h = pd.read_csv(humektanty_name)

    proteiny_name = "proteiny_skladniki.csv"
    data_p = pd.read_csv(proteiny_name)


    def wyswietl_slownik(self):
        for key, value in self.slownik.items():
            print(key, " : ", value)


    def czy_zawiera(kolekcja,nazwa):
        for i in kolekcja:
            if str(i).__contains__(nazwa):
                return True


    def zwroc_ze_slownika(self,kolekcja, nazwa):
        for i in kolekcja:
            if str(i).__contains__(nazwa):
                return str(i) + " - " + str(kolekcja.get(str(i)))


    def znajdz_w_slowniku(self):
        pojecie = input("Podaj szukane pojęcie: ")
        if (Wlosy.czy_zawiera(self.slownik, pojecie)):
            print(self.zwroc_ze_slownika(self.slownik, pojecie))
        else:
            print("Nie ma takiego pojecia w słowniku")

    def znajdz_w_slowniku_defult(self):
        pojecie = "PEH"
        if (Wlosy.czy_zawiera(self.slownik, pojecie)):
            print(self.zwroc_ze_slownika(self.slownik, pojecie))
        else:
            print("Nie ma takiego pojecia w słowniku")

    def znajdz_typ_skladnika(self):
        ingredient_name = input('Wpisz szukany składnik: ')
        if (self.data_e.values.__contains__(str(ingredient_name))):
            print("Skladnik ten nalezy do grupy emolientow")
        elif(self.data_h.values.__contains__(str(ingredient_name))):
            print("Skladnik ten nalezy do grupy humektantów")
        elif(self.data_p.values.__contains__(str(ingredient_name))):
            print("Skladnik ten nalezy do grupy protein")
        else:
            print("Skladnik nie wystepuje w naszej bazie!")

    def znajdz_typ_skladnika_defult(self):
        ingredient_name = 'Mel'
        if (self.data_e.values.__contains__(str(ingredient_name))):
            print("Skladnik ten nalezy do grupy emolientow")
        elif (self.data_h.values.__contains__(str(ingredient_name))):
            print("Skladnik ten nalezy do grupy humektantów")
        elif (self.data_p.values.__contains__(str(ingredient_name))):
            print("Skladnik ten nalezy do grupy protein")
        else:
            print("Skladnik nie wystepuje w naszej bazie!")

    def rownowaga_peh_quiz(self):
        proteiny = 0
        emolienty = 0
        humektanty = 0

        suche = input('Czy twoje wlosy sa suche?(tak/nie):\n ')
        matowe = input('Czy twoje wlosy sa matowe?(tak/nie):\n ')
        pozbawione_objetosci = input('Czy twoje wlosy sa pozbawione objetosci?(tak/nie):\n ')
        puszace_sie = input('Czy twoje wlosy sa puszace sie?(tak/nie):\n ')
        skoltunione = input('Czy twoje wlosy sa sklonne do placzeniasie lub koltunienia?(tak/nie):\n ')


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
            print("Uzywasz za duzo protein (tzw. przeproteinowanie)")
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


    def porowatosc_quiz(self):
        niskopory = 0
        sredniopory = 0
        wysokopory = 0

        p1_kondycja = input(
            'Jakie są twoje włosy?\n1- Gładkie i lśniące\n2-W dobrej kondycji, ale czasem się puszą\n3-Suche lub zniszczone:\nOdp: ')
        p2_schniecie = input(
            'Jak długo schną twoje włosy?\n1- Długo (więcej niż 3 godziny)\n2- Średnio (od 1,5 do 3 godzin)\n3- Krótko(mniej niż 1,5 godziny):\nOdp: ')
        p3_blask = input(
            'Czy twoje wlosy błyszczą w słabym świetle?\n1- Zdecydowanie błyszczą\n2-Trochę błyszczą\n3-Nie:\nOdp:  ')
        p4_pasemko = input(
            'Jeżeli przerzucisz pasemko włosów na drugą stronę?\n1- Szybko powróci na swoją stronę\n2-Powoli wróci na swoją stronę\n3-Zostanie w tym miejscu:\nOdp:  ')
        p5_podatnosc = input(
            'Czy są podatne?\n1- Loki lub falr nie robią się wcale lub bardzo szybko się roprostowują\n2-Loki lub fale  utrzymują się przez jakiś czas\n3-Loki albo fale po warkoczu sa na nich widoczne przez długi czas:\nOdp:  ')
        p6_objetosc = input(
            'Co się dzieje gdy rozczeszesz włosy?\n1- Tracą objętość \n2-Objętość się nie zmienia\n3- Nabranie objętości:\nOdp:  ')
        p7_dotyk = input(
            'Jakie w dotyku są twoje włosy?\n1- Gładkie i miękkie \n2-W miarę gładkie\n3- Sztywne i szorstkie:\nOdp:  ')
        p8_platanie = input('Czy twoje włosy się plączą?\n1- Nie \n2-Czasami\n3- Tak, bardzo:\nOdp:  ')
        p9_puszenie = input(
            'Czy twoje włosy często się puszą?\n1- Nigdy się nie puszą \n2-Czasami się puszą\n3- Tak, praktycznie zawsze są napuszone:\nOdp:  ')
        p10_niszczenie = input(
            'Czy twoje włosy łatwo się niszczą?\n1- Nie, praktycznie nigdy nie widzę u siebie rozdwojonych końcówek \n2-Średnio - wystarczy, że podetnę włosy raz na kilka miesięcy\n3- Tak, muszę często podcinać rozdwjone końce:\nOdp:  ')
        p11_krecenie_prostowanie = input(
            'Czy zdarza ci się rozjaśniać lub prostować/kręcić włosy na lokówce?\n1- Nie \n2-Sporadycznie\n3- Tak, regularnie: \nOdp: ')

        if (
                p1_kondycja == '1' or p2_schniecie == '1' or p3_blask == '1' or p4_pasemko == '1' or p5_podatnosc == '1' or p6_objetosc == '1' or p7_dotyk == '1' or p8_platanie == '1' or p9_puszenie == '1' or p10_niszczenie == '1' or p11_krecenie_prostowanie == '1'):
            niskopory = niskopory + 1
        if (
                p1_kondycja == '2' or p2_schniecie == '2' or p3_blask == '2' or p4_pasemko == '2' or p5_podatnosc == '2' or p6_objetosc == '2' or p7_dotyk == '2' or p8_platanie == '2' or p9_puszenie == '2' or p10_niszczenie == '2' or p11_krecenie_prostowanie == '2'):
            sredniopory = sredniopory + 1
        if (
                p1_kondycja == '3' or p2_schniecie == '3' or p3_blask == '3' or p4_pasemko == '3' or p5_podatnosc == '3' or p6_objetosc == '3' or p7_dotyk == '3' or p8_platanie == '3' or p9_puszenie == '3' or p10_niszczenie == '3' or p11_krecenie_prostowanie == '3'):
            wysokopory = wysokopory + 1


        print("WYNIK: ")
        if (wysokopory > niskopory):
            if (wysokopory > sredniopory):
                print("Porowatość wysoka")
            elif (wysokopory < sredniopory):
                print("Porowatosc srednia")
        elif (wysokopory < niskopory):
            if (niskopory > sredniopory):
                print("Porowatość niska")
            elif (niskopory < sredniopory):
                print("Porowatosc srednia")
        elif (wysokopory == sredniopory):
            print("Porowatosc srednia w stronę wysokiej")
        elif (niskopory == sredniopory):
            print("Porowatosc srednia w strone niskiej")

    def sprawdz_sklad(self):
        sklad = input("Podaj sklad do analizy:\n").split(", ")
        # print(sklad)
        emolienty = 0
        humektanty = 0
        proteiny = 0
        for i in sklad:
            if (self.data_e.values.__contains__(str(i))):
                emolienty = emolienty + 1
            if (self.data_h.values.__contains__(str(i))):
                humektanty = humektanty + 1
            if (self.data_p.values.__contains__(str(i))):
                proteiny = proteiny + 1

        if (emolienty > proteiny):
            if (emolienty > humektanty):
                print("Sklad jest emolientowy")
            elif (humektanty > proteiny):
                print("Sklad jest humektanowy")
        elif (proteiny > humektanty):
            print("Skład jest proteinowy")

        if (emolienty == proteiny):
            print("Skład jest emolientowo-proteinowy")
        elif (emolienty == humektanty):
            print("Skład jest emolientowo-humektantowy")
        elif (humektanty == proteiny):
            print("Skład jest humektantowo-proteinowy")
        elif (emolienty == proteiny == humektanty):
            print("Skład jest PEH")

    def sprawdz_sklad_default(self):
        sklad = "Aqua, Cetearyl Alcohol, Coco-Caprylate/Caprate, Hydrolyzed Wheat Protein, Behentrimonium Chloride, Wheat Amino Acids, Soy Amino Acids, Arginine HCI, Threonine, Serine, Tocopherol, Cetrimonium Chloride, Citric Acid, Benzyl Alcohol, Benzoic Acid, Guar Hydroxypropyltrimonium Chloride, Sodium Benzoate, Potassium Sorbate, Dehydroacetic Acid, Parfum"
        # print(sklad)
        emolienty = 0
        humektanty = 0
        proteiny = 0
        for i in sklad:
            if (self.data_e.values.__contains__(str(i))):
                emolienty = emolienty + 1
            if (self.data_h.values.__contains__(str(i))):
                humektanty = humektanty + 1
            if (self.data_p.values.__contains__(str(i))):
                proteiny = proteiny + 1

        if (emolienty > proteiny):
            if (emolienty > humektanty):
                print("Sklad jest emolientowy")
            elif (humektanty > proteiny):
                print("Sklad jest humektanowy")
        elif (proteiny > humektanty):
            print("Skład jest proteinowy")

        if (emolienty == proteiny):
            print("Skład jest emolientowo-proteinowy")
        elif (emolienty == humektanty):
            print("Skład jest emolientowo-humektantowy")
        elif (humektanty == proteiny):
            print("Skład jest humektantowo-proteinowy")
        elif (emolienty == proteiny == humektanty):
            print("Skład jest PEH")

    def dobierz_produkt(self):
        porowatosc = input("Jaka jest twoja porowatosc?\nwysoka\nsrednia\nniska\nPorowatosc: ")
        drogeria = input("Z jakiej drogerii maja byc produkty?\n1-Rossmann\n2-Hebe\n3-Natura\nWybór:")
        if (drogeria == '1'):
            if (porowatosc == 'wysoka'):
                print('Emolienty: Anwen Emolientowa Róża lub Anwen Emolientowy Irys')
                print('Humektanty: ISANA Intensive Care')
                print('Proteiny: Only Bio odżywka proteinowa')
            if (porowatosc == 'srednia'):
                print('Emolienty: Only Bio, odżywka emolientowa')
                print('Humektanty: YOPE Hydrate odżywka do włosów z humektantami')
                print('Proteiny: Anwen Proteinowa Magnolia')
            if (porowatosc == 'niska'):
                print('Emolienty: Joanna Vegan odżywka pielęgnująca do włosów z bergamotką')
                print('Humektanty: YOPE Świeża Trawa odżywka do włosów przetłuszczających się')
                print('Proteiny: Anwen Zielona Herbata')
        if (drogeria == '2'):
            if (porowatosc == 'wysoka'):
                print('Emolienty: Revuele Oil Therapy')
                print('Humektanty: Joanna Vegan odżywka nawilżająca do włosów')
                print('Proteiny: Joanna Vegan odżywka regenerująca do włosów')
            if (porowatosc == 'srednia'):
                print('Emolienty: Biovax, maska Bambud i Awokado')
                print('Humektanty: Only Bio maska do włosów średnioporowatych')
                print('Proteiny: Yumi odżywka proteinowa do włosów')
            if (porowatosc == 'niska'):
                print('Emolienty: Gosh odżywka Rose Oil')
                print('Humektanty: Vis Plantis Lipa odżywka do włosów suchych i matowych z lukrecją, lipą i prawoślazem')
                print('Proteiny: HAIR OF THE DAY BY ONLY BIO dżywka proteinowa do włosów każdej porowatości')
        if (drogeria == '3'):
            if (porowatosc == 'wysoka'):
                print('Emolienty: Botanic Hair Food maska odżywcza')
                print('Humektanty: Sylveco Betulina Balsam Do Włosów ')
                print('Proteiny: Joanna Vegan odżywka z proteinami migdałów')
            if (porowatosc == 'srednia'):
                print('Emolienty: Inecto, odżywka Argan')
                print('Humektanty: Seyo arganowa')
                print('Proteiny: Cafe Mimi, maska Keratin')
            if (porowatosc == 'niska'):
                print('Emolienty: Inecto Shea')
                print('Humektanty: Anwen Nawilżający Bez')
                print('Proteiny: Dr Sante, maska kokosowa')


