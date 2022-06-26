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

# Za kodiranje naša enigma potrebuje 3 rotorje, v vsakemu od katerega se črka spremeni
# te rotorje bomo oblikovali kot razred
# rotor je vresnici permutacija 26 črk angleške abecede brez negibnih točk
# Posamezne črke bomo ponazorili z njihovo zaporedno številko v abecedi. c npr. bi bila 3
# sestavimo funkcijo, ki preveri, če je dan seznam prvih 26 številk res ustrezna permutacija
# identiteta je, kot bi ime namigovalo, le urejen seznam številk 1 do 26

identiteta = list(range(1,27))

def preveri_rotor(sez):
    if len(sez) != 26:
        return False
    
    for i in sez:
        if i not in identiteta:
            return False
        if sez.index(i) == identiteta.index(i):
            return False
    
    return True


# še funkcija, ki nam sestavi naključni rotor (potrebno import random)
def ustvari_rotor():
    rotor = random.sample(identiteta, len(identiteta))
    if preveri_rotor(rotor):
        return rotor
    else:
        return ustvari_rotor()
    
# v fizični obliki enigme so imeli dostop do petih rotorjev, iz katerih so izbrali 3 za posamezno kodiranje
# ker nimam dostopa do informacije, kakše točne permutacije so bili te rotorji, jih bomo naključno generirali

rot1 = [7, 24, 18, 14, 15, 25, 9, 20, 10, 5, 13, 2, 1, 4, 12, 6, 3, 17, 11, 8, 19, 16, 26, 22, 21, 23]
rot2 = [4, 3, 21, 23, 20, 9, 2, 14, 18, 26, 8, 13, 6, 16, 24, 7, 22, 15, 12, 17, 19, 11, 25, 5, 10, 1]
rot3 = [17, 22, 6, 20, 4, 24, 3, 26, 13, 7, 15, 8, 12, 18, 23, 25, 10, 5, 14, 19, 11, 1, 9, 2, 21, 16]
rot4 = [24, 8, 2, 3, 19, 9, 17, 6, 5, 21, 23, 25, 14, 10, 26, 22, 11, 13, 12, 18, 7, 15, 16, 4, 1, 20]
rot5 = [2, 18, 19, 12, 24, 15, 3, 14, 1, 21, 22, 17, 5, 13, 20, 23, 25, 16, 6, 7, 11, 26, 9, 4, 10, 8]

# definirajmo sedaj razred Rotor skupaj z nekimi osnovnimi funkcijami

class Rotor:
    
    def __init__(self, permutacija, pozicija):
        self.perm = permutacija
        self.poz = pozicija

    def __str__(self):
        return 'Rotor z permutacijo: {0} in pozicijo: {1}'.format(self.perm, self.poz)
    
    def __repr__(self):
        return 'Rotor({0}, {1})'.format(self.perm, self.poz)
    
    def rotiraj(self):
        i = self.poz
        if i != 26:
            i += 1
        else:
            i = 1
        return 'Rotor({0}, {1})'.format(self.perm, i)



