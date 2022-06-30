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
        y = input('Vnesite zrcalo kot ustrezen seznam [a1, ... , a25]')
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
        y = input('Vnesite primerno permutacijo kot seznam [a1, ... , an]:')
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
        y = input('Vnesite plugboard kot ustrezen seznam [a1, ... , a25]')
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