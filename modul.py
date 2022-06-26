import string
import random

# Najprej sestavimo funkcijo, ki besedilo spremeni v sprejemljivo obliko
# To pomeni da odstrani vse znake, ki niso v angleški abecedi in spremeni vse črke v male
# Presledke pusti pri miru, če nastane več zaporednih presledkov jih spremeni v enega
# Šumnike spremeni v črke brez strešice
# Za angleško abecedo importamo string

def uredi_besedilo(tekst):
    delno_urejen1 = tekst.lower().replace('č', 'c').replace('š', 's').replace('ž', 'z')
    delno_urejen2 = ''
    ang_abc = list(string.ascii_lowercase)

    for znak in delno_urejen1:
        if znak in ang_abc or znak == ' ':
            delno_urejen2 += znak

    urejen_tekst = ' '.join(delno_urejen2.split())

    return urejen_tekst


testno_besedilo = 'Jaz pišem besedilo s katerim bom \t preveril kaj dogaja 123:::___// SDŠŠĆĆŽŽČčč \n \n \t'

# Za kodiranje naša enigma potrebuje 3 rotorje, v vsakemu od katerega se črka spremeni v drugo črko
# te rotorje bomo oblikovali kot razred
# rotor je vresnici permutacija 26 črk angleške abecede brez negibnih točk
# Posamezne črke bomo ponazorili z njihovo zaporedno številko v abecedi. a je 0, b je 1, c 2 itd.
# sestavimo funkcijo, ki preveri, če je dan seznam prvih 26 številk res ustrezna permutacija
# identiteta je, kot bi ime namigovalo, le urejen seznam številk 1 do 26

identiteta = list(range(26))

def preveri_rotor(per):
    for i in range(len(per)):
        if per.count(i) != 1:
            return False
    
    for i in per:
        if per.index(i) == i:
            return False
    
    return True


# še funkcija, ki nam sestavi naključno permutacijo za rotor (potrebno import random)
def ustvari_rotor():
    rotor = random.sample(identiteta, len(identiteta))
    if preveri_rotor(rotor):
        return rotor
    else:
        return ustvari_rotor()
    
# v fizični obliki enigme so imeli dostop do petih rotorjev, iz katerih so izbrali 3 za posamezno kodiranje
# ker nimam dostopa do informacije, kakše točne permutacije so bili te rotorji, jih bomo naključno generirali
# zapišimo jih kot konstante
rot1 = [9, 13, 7, 18, 25, 20, 3, 4, 2, 22, 23, 6, 1, 24, 16, 11, 5, 15, 12, 0, 19, 8, 14, 10, 17, 21]
rot2 = [5, 17, 9, 7, 6, 18, 23, 0, 12, 13, 14, 10, 25, 24, 20, 8, 1, 3, 22, 11, 21, 19, 2, 15, 16, 4]
rot3 = [25, 11, 15, 21, 0, 10, 20, 3, 24, 12, 13, 5, 1, 19, 23, 7, 18, 9, 22, 4, 16, 8, 6, 2, 14, 17]
rot4 = [14, 20, 18, 25, 3, 17, 10, 13, 15, 24, 4, 6, 22, 1, 12, 23, 9, 21, 7, 5, 11, 8, 16, 2, 0, 19]
rot5 = [13, 12, 18, 16, 7, 21, 5, 22, 19, 25, 24, 23, 4, 0, 3, 17, 14, 8, 6, 15, 1, 10, 2, 11, 20, 9]

# definirajmo sedaj razred Rotor skupaj z nekimi osnovnimi funkcijami (prvo pa pomožna funkcija za indeks 1 do 26)
#class Rotor:
#
#    def __init__(self, per, indeks):
#        self.per = per
#        self.per =


# ko se črke trikrat permutira skozi rotorje, se zamenja v "zrcalu" in nato ponovno gre skozi rotorje
# zrcalo je torej permutacija 26 črk z 13 različnimi transpozicijami
# kot za rotor, ustvarimo funkcijo, ki preveri če je zrcalo res to
# za razliko od rotorjev, ki se, kot bi ime namigovalo, po vsaki črki obrnejo, je zrcalo konstantno

def preveri_zrcalo(per):
    if not preveri_rotor(per):
        return False
    for i in per:
        if per[i] != per.index(i):
            return False
    return True

# in še funkcija ki ustvari naključno zrcalo.
# Tu bo treba biti rahlo bolj zvit, saj z povsem naključno generacijo ponavadi ne dobimo ustrezne permutacije
def ustvari_zrcalo():
    zrc = []
    for i in range(26):
        zrc.append(0)
    
    preostale_stevilke = identiteta.copy()
    while len(preostale_stevilke) > 0:
        x = random.choice(preostale_stevilke)
        preostale_stevilke.remove(x)
        y = random.choice(preostale_stevilke)
        preostale_stevilke.remove(y)
        zrc[x] = y
        zrc[y] = x

    return zrc

# Konstantno zrcalo, ki ga bomo uporabljali je
zrcalo = [8, 14, 25, 19, 10, 22, 9, 18, 0, 6, 4, 13, 16, 11, 1, 17, 12, 15, 7, 3, 23, 24, 5, 20, 21, 2]
# definirajmo funkcijo, kaj se zgodi s številko, ko gre skozi zrcalo:
def kodiraj_zrcalo(x, zrc = zrcalo):
    return zrc[x]


# Zadnja stvar, ki jo potrebujemo za uspešno kodiranje, je plugboard
# plugboard omogoča nastavitve, da povežemo 2 črki, ki se potem zamenjate preden in/ali po tem, ko črka pride iz rotorjev
# plugboard je torej sestavljen iz 1 do 13 permutacij črk

def preveri_plugboard(per):
    for i in range(26):
        if per.count(i) != 1:
            return False
    for i in per:
        if (not (per.index(i) == i)) and per[i] != (per.index(i)):
            return False
    return True


# definiramo funkcijo, ki nam ustvari naključen plugboard.
# verjetnost, da se 2 naključno izbrani številki povežeta je arbitrarno določena na 2/3

def ustvari_plugboard():
    pb = []
    for i in range(26):
        pb.append(0)
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

plugboard = [0, 23, 3, 2, 4, 17, 6, 11, 8, 13, 10, 7, 22, 9, 16, 19, 14, 5, 18, 15, 20, 21, 12, 1, 24, 25]

def kodiraj_plugboard(x, pb = plugboard):
    return pb[x]

# Funkciji ki preko seznama črk iz abecede spremenita črko v njeno zaporedno št v abecedi in obratno
def crka_v_stevilko(crka):
    stevilka = list(string.ascii_lowercase).index(crka)
    return stevilka

def stevilka_v_crko(stevilka):
    crka = list(string.ascii_lowercase)[stevilka]
    return crka