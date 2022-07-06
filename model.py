import string
import random

# Enigmo sestavljajo trije ključni deli: plugboard, rotorji in "zrcalo"
# Mehanično je delovala tako, da se je ob pritisku na tipko sklenil električni tok
# Ta je potoval skozi posamezne dele enigme, kjer se je večkrat spremenil v drugo črko
# Programsko bomo te posamezne dele enigme predstavili kot permutacije črk oz. številk, ki črke predstavljajo
# Prvi del modula zajema programiranje rotorjev, plugboarda in zrcala
# Drugi del zajema združitev različnih možnosti teh nastavitev v razred "Koda", ki nam omogoča kodiranje
# Tretji del zajema funkcije, ki potem kodirajo posamezno črko in besedilo

#_____________________________________________________________________________________________________________
#_____________________________________________________________________________________________________________
# 1. del:

# Za kodiranje naša enigma potrebuje 3 rotorje, v vsakemu od katerega se črka spremeni v drugo črko
# te rotorje bomo oblikovali kot razred
# Rotor je vresnici permutacija 26 črk angleške abecede brez negibnih točk z možnim zamikom (če se rotor obrne)
# črka bo potovala skozi te tri rotorje, se v vsakemu spremenila, se spremenila v zrcalu in šla nazaj skozi rotorje
# Posamezne črke bomo ponazorili z njihovo zaporedno številko v abecedi. a je 0, b je 1, c 2 itd.
# Sestavimo najprej funkcijo, ki preveri, če je dan seznam prvih 26 številk res ustrezna permutacija
# Identiteta je, kot bi ime namigovalo, le urejen seznam številk 1 do 26

identiteta = list(range(26))

def preveri_rotor(per):
    for i in range(len(per)):
        if per.count(i) != 1:
            return False
    
    for i in per:
        if per.index(i) == i:
            return False
    
    return True


# Sedaj potrebujemo funkcijo, ki nam sestavi naključno permutacijo za rotor
def ustvari_rotor():
    rotor = random.sample(identiteta, len(identiteta))
    if preveri_rotor(rotor):
        return rotor
    else:
        return ustvari_rotor()
    
# V fizični obliki enigme so imeli dostop do petih rotorjev, iz katerih so izbrali 3 za posamezno kodiranje
# Ker nimam dostopa do informacije, kakše točne permutacije so bili te rotorji, jih bomo naključno generirali
# Zapišimo jih kot konstante
per1 = [9, 13, 7, 18, 25, 20, 3, 4, 2, 22, 23, 6, 1, 24, 16, 11, 5, 15, 12, 0, 19, 8, 14, 10, 17, 21]
per2 = [5, 17, 9, 7, 6, 18, 23, 0, 12, 13, 14, 10, 25, 24, 20, 8, 1, 3, 22, 11, 21, 19, 2, 15, 16, 4]
per3 = [25, 11, 15, 21, 0, 10, 20, 3, 24, 12, 13, 5, 1, 19, 23, 7, 18, 9, 22, 4, 16, 8, 6, 2, 14, 17]
per4 = [14, 20, 18, 25, 3, 17, 10, 13, 15, 24, 4, 6, 22, 1, 12, 23, 9, 21, 7, 5, 11, 8, 16, 2, 0, 19]
per5 = [13, 12, 18, 16, 7, 21, 5, 22, 19, 25, 24, 23, 4, 0, 3, 17, 14, 8, 6, 15, 1, 10, 2, 11, 20, 9]

# Definirajmo sedaj razred Rotor skupaj z nekaj osnovnimi funkcijami
class Rotor:

    def __init__(self, per, pozicija):
        self.per = per
        self.poz = pozicija % 26
    
    def __str__(self):
        return 'Rotor s permutacijo {0} in pozicijo {1}'.format(self.per, self.poz)

    def __rept__(self):
        return 'Rotor({0}, {1})'.format(self.per, self.poz)

# Po tem, ko enigma kodira posamezno črko, se rotorji obrnejo, tako da za naslednjo črko koda ne ostane ista
# Ta obrat bomo simulirali z zamikom, ki smo ga definirali preko argumenta pozicija
    def rotiraj(self):
        return Rotor(self.per, (self.poz + 1) % 26)

# Funkcija, ki nam da rotor z inverzno permutacijo prvotnega rotorja
# Funkcijo bomo potrebovali, ko pošljemo črko nazaj skozi rotor
    def inverz(self):
        inverz = [0] * 26
        for i in self.per:
            inverz[i] = self.per.index(i)
        return Rotor(inverz, self.poz)

# Potrebujemo še funkcijo, ki permutira dano črko (številko) ko ta gre skozi rotor
# Če je rotor obrnjen (ni na opziciji 0) se črka x permutira za enak faktor, kot bi se permutirala črka x + poz
def kodiraj_rotor(x, rotor):
    y = rotor.per[(x + rotor.poz) % 26]
    return (y - rotor.poz) % 26
    
# Ko se črka trikrat permutira v rotorjih, se zamenja v "zrcalu" in nato ponovno gre skozi rotorje
# Zrcalo je torej permutacija 26 črk z 13 različnimi transpozicijami
# Kot za rotor, ustvarimo funkcijo, ki preveri če permutacija primerna
# Za razliko od rotorjev, ki se, kot bi ime namigovalo, po vsaki črki obrnejo, je zrcalo konstantno
def preveri_zrcalo(per):
    if not preveri_rotor(per):
        return False
    for i in per:
        if per[i] != per.index(i):
            return False
    return True

# In še funkcija ki ustvari naključno zrcalo.
# Tu bo treba biti rahlo bolj zvit, saj z povsem naključno generacijo ponavadi ne dobimo ustrezne permutacije
def ustvari_zrcalo():
    zrc = [0] * 26
    preostale_stevilke = identiteta.copy()
    while len(preostale_stevilke) > 0:
        x = random.choice(preostale_stevilke)
        preostale_stevilke.remove(x)
        y = random.choice(preostale_stevilke)
        preostale_stevilke.remove(y)
        zrc[x] = y
        zrc[y] = x

    return zrc

# Konstantno zrcalo, ki ga bomo uporabljali je (vzel sem enega naključno generiranega)
zrcalo = [8, 14, 25, 19, 10, 22, 9, 18, 0, 6, 4, 13, 16, 11, 1, 17, 12, 15, 7, 3, 23, 24, 5, 20, 21, 2]

# Za konec potrebujemo še funkcijo, ki permutira črko ko ta pride do zrcala
def kodiraj_zrcalo(x, zrc = zrcalo):
    return zrc[x]


# Zadnja stvar, ki jo potrebujemo za uspešno kodiranje, je plugboard
# Plugboard omogoča nastavitve, da povežemo 2 črki, ki se potem zamenjate preden in/ali po tem, ko črka pride iz rotorjev
# Plugboard je torej sestavljen iz 1 do 13 transpozicij črk, na ostalih črkah pa je identiteta
# Ponovno sestavimo funkcijo, ki preveri, če je permutacija ustrezna
def preveri_plugboard(per):
    for i in range(26):
        if per.count(i) != 1:
            return False
    for i in per:
        if (not (per.index(i) == i)) and per[i] != (per.index(i)):
            return False
    return True


# Definiramo funkcijo, ki nam ustvari naključen plugboard.
# Verjetnost, da se 2 naključno izbrani številki povežeta je arbitrarno določena na 2/3. Lahko bi bila karkoli
def ustvari_plugboard():
    pb = [0] * 26
    indeks = [0, 1, 2]
    
    preostale_stevilke = identiteta.copy()
    while len(preostale_stevilke) > 0:
        x = random.choice(preostale_stevilke)
        preostale_stevilke.remove(x)
        y = random.choice(preostale_stevilke)
        preostale_stevilke.remove(y)
        ran = random.choice(indeks)
        if ran == 0:
            pb[x] = x
            pb[y] = y
        else:
            pb[x] = y
            pb[y] = x

    return pb

# Za testne primere bomo uporabljali arbitrarno določene plugboard nastavitve
plugboard = [0, 23, 3, 2, 4, 17, 6, 11, 8, 13, 10, 7, 22, 9, 16, 19, 14, 5, 18, 15, 20, 21, 12, 1, 24, 25]

# Za konec seveda še funkcija, ki permutira črko, ko ta gre skozi plugboard
def kodiraj_plugboard(x, pb = plugboard):
    return pb[x]


#_____________________________________________________________________________________________________________
#_____________________________________________________________________________________________________________
# 2. del:

# Definirajmo razred "Koda", ki vsebuje 3 rotorje v določenem vrstnem redu, plugboard in zrcalo
class Koda:

    def __init__(self, rot1, rot2, rot3, pb = plugboard,  zrc = zrcalo):
        self.rot1 = rot1
        self.rot2 = rot2
        self.rot3 = rot3
        self.zrc = zrc
        self.pb = pb
    
    def __str__(self):
        x1 = self.rot1
        x2 = self.rot2
        x3 = self.rot3
        return ('Koda:\n'
                    'rotorji:\n'
                    '\t{0}\n'
                    '\t{1}\n'
                    '\t{2}\n'
                    'plugboard: {3}\n'
                    'zrcalo:{4}').format(x1, x2, x3, self.pb, self.zrc)
# Kot sem že prej omenil, se po vsaki črki rotorji obrnejo, tako da se koda spremeni
# Obrnejo se po naslednjem pravilu:
#   - 1. rotor se vedno obrne
#   - 2. rotor se obrne na vsakih 26 obratov prvega. Torej le ko gre pozicija 1. iz 25 na 0
#   - 3. rotor se obrne na vsakih 26 obratov drugega
    def spremeni(self):
        if self.rot1.poz == 25:
            if self.rot2.poz == 25:
                return Koda(self.rot1.rotiraj(), self.rot2.rotiraj(), self.rot3.rotiraj(), self.pb, self.zrc)
            return Koda(self.rot1.rotiraj(), self.rot2.rotiraj(), self.rot3, self.pb, self.zrc)
        return Koda(self.rot1.rotiraj(), self.rot2, self.rot3, self.pb, self.zrc)

#_____________________________________________________________________________________________________________
#_____________________________________________________________________________________________________________
# 3. del:

# Sedaj lahko sestavimo fukncije, ki nam kodirajo besedilo
# Najprej sestavimo funkcijo, ki besedilo spremeni v sprejemljivo obliko
# To pomeni da odstrani vse znake, ki niso v angleški abecedi in spremeni vse črke v male
# Presledke pusti pri miru, če nastane več zaporednih presledkov jih spremeni v enega
# Šumnike spremeni v črke brez strešice. Ostale črke (npr ć, đ) izbriše
# Za angleško abecedo importamo string
def uredi_besedilo(tekst):
    delno_urejen1 = tekst.lower().replace('č', 'c').replace('š', 's').replace('ž', 'z').replace('\n', ' ').replace('\t', ' ')
    delno_urejen2 = ''
    ang_abc = list(string.ascii_lowercase)

    for znak in delno_urejen1:
        if znak in ang_abc or znak == ' ':
            delno_urejen2 += znak

    urejen_tekst = ' '.join(delno_urejen2.split())

    return urejen_tekst

# Funkciji, ki preko seznama črk iz abecede spremenita črko v njeno zaporedno št v abecedi in obratno
def crka_v_stevilko(crka):
    stevilka = list(string.ascii_lowercase).index(crka)
    return stevilka

def stevilka_v_crko(stevilka):
    crka = list(string.ascii_lowercase)[stevilka]
    return crka

# Funkcija, ki kodira posamezno črko glede na nastavitev kode
# Funkcija je vresnici zmnožek permutacij črk: na koncu dobimo transpozicije
# Funkcija je torej sam svoj inver: če iz kodirane črke želimo originalno, jo le vstavimo pod istimi pogoji
def kodiraj_crko(crka, koda):
    # Črko najprej spremenimo v številko
    x0 = crka_v_stevilko(crka)
    # Potem številko pošlemo skozi plugboard (morda se spremeni morda pa ne)
    x1 = kodiraj_plugboard(x0, koda.pb)
    # Nato skozi vse 3 rotorje
    x2 = kodiraj_rotor(x1, koda.rot1)
    x3 = kodiraj_rotor(x2, koda.rot2)
    x4 = kodiraj_rotor(x3, koda.rot3)
    # Skozi zrcalo
    x5 = kodiraj_zrcalo(x4, koda.zrc)
    # Nazaj skozi rotorje
    x6 = kodiraj_rotor(x5, koda.rot3.inverz())
    x7 = kodiraj_rotor(x6, koda.rot2.inverz())
    x8 = kodiraj_rotor(x7, koda.rot1.inverz())
    # In še enkrat skozi plugboard (spet, morda se spremeni morda ne)
    x9 = kodiraj_plugboard(x8, koda.pb)
    # Številka se tako spremeni 7 do 9 krat, odvisno od plugboard nastavitev
    # Sedaj številko spremenimo nazaj v črko
    return stevilka_v_crko(x9)

# Za konec še funkcija, ki kodira celotno besedilo
# Funkcija vzame besedilo in ga uredi po pravilih opisanih zgoraj
# Nato gre čez vse znake urejenega besedila:
# Če je znak presledek, ga pusti pri miru
# Če pa je znak črka, jo kodira preko funkcije kodiraj_crko, nato pa ustrezno spremeni kodo
def kodiraj_besedilo(besedilo, koda):
    urejeno_besedilo = uredi_besedilo(besedilo)
    kodirano_besedilo = ''
    for znak in urejeno_besedilo:
        if znak == ' ':
            kodirano_besedilo += znak
        else:
            kodirano_besedilo += kodiraj_crko(znak, koda)
            koda = koda.spremeni()
    return kodirano_besedilo

# Za dekodiranje besedila uporabimo isto funkcijo
# Kot opisano prej v opisu funkcije kodiraj_crko, je funkcija sam svoj inverz
# Torej moramo le vstaviti kodirano besedilo pod istimi začetnimi pogoji (Kodo)