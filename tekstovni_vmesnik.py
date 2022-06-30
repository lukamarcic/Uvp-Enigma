import model

# Funkcij za nastavitev zrcala
def nastavi_zrcalo():
    x = input(  'Zrcalo je permutacija 26 znakov, zapisana kot seznam številk 0 - 25 \n'
                'Permutacija paroma zamenja črke (številke)\n'
                'Torej gre za produkt 13 disjunktnih transpozicij \n'
                'Na voljo imamo tri opcije: \n'
                '\t (a): Uporabimo v naprej nastavljeno zrcalo \n'
                '\t (b): Uporabimo novo, naključno generirano zrcalo \n'
                '\t (c): Uporabimo zrcalo, ki ga boste določili sami \n'
                'Prosim izberite črko pred ustrezno izbiro (a/b/c):')
    if x.lower() == 'a':
        return model.zrcalo
    elif x.lower() == 'b':
        zrc = model.ustvari_zrcalo()
        print('Prosim zapišite si zrcalo, če želite svoje sporočilo kdaj dekodirati')
        print(zrc)
        return zrc
    elif x.lower() == 'c':
        y = input('Vnesite zrcalo kot ustrezen seznam [a1, ... , a25]:\t')
        y1 = y.lstrip('[').rstrip(']').replace(' ', '').split(',')
        if all(i.isnumeric() for i in y1):
            y2 = list(map(int, y1))
            if model.preveri_zrcalo(y2):
                return y2
            else:
                print('Žal vnesen seznam ni ustrezen. Prosim, poskusite ponovno')
                return nastavi_zrcalo()
        else:
            print('Žal vnesen seznam ni ustrezen. Prosim, poskusite ponovno')
            return nastavi_zrcalo()
    else:
        print('Odgovor je lahko le oblike "a", "b" ali "c". Prosim, poskusite ponovno')
        return nastavi_zrcalo()

# Funkcija za nastavitev posameznega rotorja
def nastavi_rotor():
    fail_msg = 'Žal vnos ni pravilen. Prosim, poskusite ponovno'
    rotor_poz = 'Prosim, izberite začetno pozicijo rotorja (0-25):'
    x = input('Na voljo imamo tri opcije: \n'
            '\t (a): Uporabimo v naprej nastavljeno permutacijo za rotor \n'
            '\t (b): Uporabimo novo, naključno generirano permutacijo za rotor \n'
            '\t (c): Uporabimo permutacijo, ki jo boste določili sami \n'
            'Prosim izberite črko pred ustrezno izbiro (a/b/c):')

    if x.lower() == 'a':
        y = input('Prosim, izberite eno izmed petih v naprej določenih permutacij (1/2/3/4/5):')
        if y == '1':
            z = input(rotor_poz)
            if z.isnumeric() and ( 0 <= int(z) <= 25):
                return model.Rotor(model.per1, int(z))
            else:
                print(fail_msg)
                return nastavi_rotor()
        elif y == '2':
            z = input(rotor_poz)
            if z.isnumeric() and ( 0 <= int(z) <= 25):
                return model.Rotor(model.per2, int(z))
            else:
                print(fail_msg)
                return nastavi_rotor()
        elif y == '3':
            z = input(rotor_poz)
            if z.isnumeric() and ( 0 <= int(z) <= 25):
                return model.Rotor(model.per3, int(z))
            else:
                print(fail_msg)
                return nastavi_rotor()
        elif y == '4':
            z = input(rotor_poz)
            if z.isnumeric() and ( 0 <= int(z) <= 25):
                return model.Rotor(model.per4, int(z))   
            else:
                print(fail_msg)
                return nastavi_rotor()                 
        elif y == '5':
            z = input(rotor_poz)
            if z.isnumeric() and ( 0 <= int(z) <= 25):
                return model.Rotor(model.per5, int(z))
            else:
                print(fail_msg)
                return nastavi_rotor()
        else:
            print(fail_msg)
            return nastavi_rotor()

    elif x.lower() == 'b':
        print('Prosim, zapišite si permutacijo rotorja, če želite svojo spročilo kdaj dekodirati')
        per = model.ustvari_rotor()
        print(per)
        z = input(rotor_poz)
        if z.isnumeric() and ( 0 <= int(z) <= 25):
            return model.Rotor(per, int(z))
        else:
            print(fail_msg)
            return nastavi_rotor()
    
    elif x.lower() == 'c':
        y = input('Vnesite primerno permutacijo kot seznam [a1, ... , an]:\t')
        y1 = y.lstrip('[').rstrip(']').replace(' ', '').split(',')
        if all(i.isnumeric() for i in y1):
            y2 = list(map(int, y1))
            if model.preveri_rotor(y2):
                z = input(rotor_poz)
                if z.isnumeric() and ( 0 <= int(z) <= 25):
                    return model.Rotor(y2, int(z))
                else:
                    print(fail_msg)
                    return nastavi_rotor()
            else:
                print(fail_msg)
                return nastavi_rotor()
        else:
            print(fail_msg)
            return nastavi_rotor()
    
    else:
        print(fail_msg)
        return nastavi_rotor()

# Funkcija za nastavitev vseh treh rotorjev
def nastavi_rotorje():
    print('Rotor je permutacija 26 znakov, zapisana kot seznam številk 0 - 25 \n'
            'Rotor vsako črko spremeni v neko drugo črko\n'
            'Torej gre za permutacijo brez fiksih točk \n'
            'Rotor lahko potem še poljubno obrnemo na eno izmed 26 pozicij (označeno z 0-25)')
    print('Prosim določite prvi rotor in njegovo začetno pozicijo')
    rotor1 = nastavi_rotor()
    print('Prosim določite drugi rotor in njegovo začetno pozicijo')
    rotor2 = nastavi_rotor()
    print('Prosim določite tretji rotor in njegovo začetno pozicijo')
    rotor3 = nastavi_rotor()
    return [rotor1, rotor2, rotor3]

# Funkcija za nastavitev plugboarda
def nastavi_plugboard():
    x = input('Tudi plugboard je permutacija 26 znakov, zapisana kot seznam številk 0 - 25 \n'
                'Permutacija paroma zamenja črke (številke) ali pa jih pusti na miru \n'
                'Torej gre za produkt 1 - 13 disjunktnih transpozicij, drugje pa je identiteta'
                'Spet imamo na voljo tri opcije: \n'
                '\t (a): Uporabimo v naprej nastavljen plugboard \n'
                '\t (b): Uporabimo nov, naključno generiran plugboard \n'
                '\t (c): Uporabimo plugboard, ki ga boste določili sami \n'
                'Prosim izberite črko pred ustrezno izbiro (a/b/c):')
    if x.lower() == 'a':
        return model.plugboard
    elif x.lower() == 'b':
        pb = model.ustvari_plugboard()
        print('Prosim zapišite si plugboard, če želite svoje sporočilo kdaj dekodirati')
        print(pb)
        return pb
    elif x.lower() == 'c':
        y = input('Vnesite plugboard kot ustrezen seznam [a1, ... , a25]:\t')
        y1 = y.lstrip('[').rstrip(']').replace(' ', '').split(',')
        if all(i.isnumeric() for i in y1):
            y2 = list(map(int, y1))
            if model.preveri_plugboard(y2):
                return y2
            else:
                print('Žal vnesen seznam ni ustrezen. Prosim, poskusite ponovno')
                return nastavi_plugboard()
        else:
            print('Žal vnesen seznam ni ustrezen. Prosim, poskusite ponovno')
            return nastavi_plugboard()
    else:
        print('Odgovor je lahko le oblike "a", "b" ali "c". Prosim, poskusite ponovno')
        return nastavi_plugboard()

# Funkcija za nastavitev začetne kode
def nastavi_kodo():
    print('Za kodiranje potrebujemo določiti začetno pozicijo naše enigme')
    print('Najprej določimo t.i. "zrcalo"')
    zrc = nastavi_zrcalo()
    print('Nadaljno moramo določiti rotorje')
    rotorji = nastavi_rotorje()
    print('Za konec potrebujemo določiti še plugboard')
    pb = nastavi_plugboard()
    print('Odlično! Sedaj imamo začetno pozicijo naše kode')
    koda = model.Koda(rotorji[0], rotorji[1], rotorji[2], pb, zrc)
    print('Spodaj je izpisana koda. Zapišite si jo, če želite sporočilo kdaj v prihodnosti dekodirati\n')
    print(koda)
    return koda

# Funkcija za vnos besedila
def vnos_besedila():
    besedilo = input('Prosim, vnesite besedilo, ki bi ga radi kodirali:\t')
    print('Ker enigma deluje kot permutiranje črk, bomo besedilo malo spremenili:\n'
            '\t-Šumnike bomo spremenili v črke brez strešice (č -> c, š -> s, ž -> z)\n'
            '\t-Vse črke bomo spremenili v male črke\n'
            '\t-Vse preostale znake, ki niso v angleški abecedi, bomo odstranili')
    print('Spremenjeno besedilo, ki ga bomo kodirali, je:')
    urejeno_besedilo = model.uredi_besedilo(besedilo)
    print(urejeno_besedilo)
    x = input('Ste z besedilom zadovoljni? (J/N):')
    if x.lower() == 'j':
        return urejeno_besedilo
    else:
        print('Potem prosim ponovno vnesite besedilo, ki bi ga radi kodirali:')
        return vnos_besedila()

# Funkcija za kodiranje besedila
def kodiraj():
    koda = nastavi_kodo()
    besedilo = vnos_besedila()
    kodirano_besedilo = model.kodiraj_besedilo(besedilo, koda)
    return(kodirano_besedilo)

# Sporočilo, ki razloži delovanje enigme
sporocilo = (
            'Enigma je bil kodirni stroj, ki so ga uporabljale nemške sile v času pred in med 2. svetovno vojno.'
            'Če damo na stran mnoge zli namene, za katere se je stroj uporabljal, dobimo zanimiv način kodiranja iz časov, '
            'ko te naloge niso še prevzeli računalniki s svojo sposobnostjo obratovanja z zello velikimi številkami.'
            'Stroj je deloval povsem mehanično. Ob pritisku tipke za posamezno črko, se je povezal električen krog, '
            'ki je potem potoval skozi stroj in prižgal luč pod črko, v katero se je prvotna črko kodirala.'
            'Tako sta s strojem ponavadi obratovali 2 osebi: prva je tipkala besedilo, druga pa si je zapisovala črke, '
            'pod katerimi se je prižgala luč. To je bilo potem kodirano besedilo.'
            'Samo kodiranje deluje na nasleden način:'
            'Ob pritisku tipke za posamezno črko je signal potoval najprej skozi plugboard.'
            'Plugboard je bil sestavljen iz večih žic, s katerimi so poljubno povezali dve po dve črki.'
            'Če je bila črka povezana z drugo črko, sta se zamenjali, ko je električni signal šel čez plugboard.'
            'Ko je signal šel skozi plugboard (kjer se je morda zamenjal v signal druge črke) je šel skozi 3 rotorje.'
            'V vsakem rotorju se je zamenjal v drugo črko'
            'Ko je prišel skozi vse 3, je šel skozi "zrcalo"'
            'Tam so se paroma zamenjale črke. Pot je signal nadaljeval nazaj skozi 3 rotorje, kjer se je zamenjal še trikrat.'
            'Za konec je signal šel še enkrat skozi plugboard, kjer se je morda zamenjal še enkrat.'
            'Posamezna črka se je takro zamenjala 7-krat do 9-krat.'
            'Ko se je kodirala črka, so se rotorji obrnili: prvi rotor se je obrnil po vsaki črki, drugi po 25ih obratih '
            'prvega, tretji pa po 25ih obratih drugega, s tem da je prvi obrat drugega ali tretjega lahko prvič prišel prej, '
            'saj se rotorji v začetnem položaju lahko poljubno obrnejo.'
            'Nemški koderji so imeli v naprej določen koledar, kdaj se uporablja katera koda.'
            'Dekodiranje nemških sporočil, kodiranih z enigmo, je bila za Anglijo pomembna prednost v vojni.'
            'Sporočila so dekodirali tako, da so imeli svojo lastno enigmo, potem so pa na podlagi tega, da so vedli majhen '
            'del sporočila ugibali začetno kodo. Oseba, ki je zaslovela s tem delom v širši publiki je seveda Alan Turing.'
            )

# Naš program enigma
def enigma():
    print('Pozdravljeni v program "Enigma"\n'
            'V programu lahko prostovoljno kodirate besedilo, kot bi to storil slaven stroj iz 2. svetovne vojne\n'
            'Če želite besedilo dekodirati, ga morate le ponovno kodirati z istimi nastavitvami za kodo\n')
    vprasanje = input('Kaj bi zeleli storiti?\n'
                        '\t (a): Kodirati/dekodirati besedilo\n'
                        '\t (b): Zanima me, kako deluje enigma\n'
                        'Prosim izberite črko pred ustrezno izbiro (a/b):')
    if vprasanje.lower() == 'a':
        print('Sledite navodilom in kodirajte besedilo')
        kodirano_besedilo = kodiraj()
        print('Vaše kodirano besedilo je:\n')
        print(kodirano_besedilo)
        x = input('Bi želeli v programu storiti še kaj? (J/N):')
        if x.lower() == 'n':
            return None
        else:
            return enigma()
    if vprasanje.lower() == 'b':
        print(sporocilo)
        print('Sedaj vas vračam na začetek programa.\n')
        return enigma()
    else:
        print('Vašega vnosa žal nisem razumel. Prosim, poskusite ponovno')
        return enigma()

#enigma()
