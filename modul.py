import string

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
print(uredi_besedilo(testno_besedilo))


