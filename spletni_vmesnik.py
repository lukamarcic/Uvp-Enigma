import bottle
import model
import tekstovni_vmesnik

zrcalo = model.zrcalo
plugboard = model.plugboard
rotor1 = model.Rotor(model.per1, 0)
rotor2 = model.Rotor(model.per1, 0)
rotor3 = model.Rotor(model.per1, 0)

#========================================================================================================
@bottle.get('/')
def osnovni_zaslon():
    return bottle.template('osnovni_zaslon.tpl', sporocilo = tekstovni_vmesnik.sporocilo_skrajsano)

#========================================================================================================
@bottle.get('/izberi/')
def izbira_zrcala():
    return bottle.template('izberi_zrc.tpl')

#========================================================================================================
@bottle.get('/izberi_zrc/')
def izberi_zrc():
    try:
        izbira = bottle.request.query['izberi_zrcalo']
    except KeyError:
        return bottle.template('izberi_zrc.tpl')

    global zrcalo

    if izbira == 'a_zrc':
        zrcalo = model.zrcalo
        return bottle.template('izberi_rot_1.tpl', zrc= zrcalo)
        
    elif izbira == 'b_zrc':
        zrcalo = model.ustvari_zrcalo()
        return bottle.template('izberi_rot_1.tpl', zrc= zrcalo)

    elif izbira == 'c_zrc':
        vnos_zrc = bottle.request.query['doloci_zrc']
        vnos_zrc_2 = vnos_zrc.lstrip('[').rstrip(']').replace(' ', '').split(',')
        if all(i.isnumeric() for i in vnos_zrc_2) and vnos_zrc_2 != []:
            vnos_zrc_3 = list(map(int, vnos_zrc_2))
            if model.preveri_zrcalo(vnos_zrc_3):
                zrcalo = vnos_zrc_3
                return bottle.template('izberi_rot_1.tpl', zrc= zrcalo)
            else:
                return bottle.template('izberi_zrc.tpl')
        else:
            return bottle.template('izberi_zrc.tpl')

#========================================================================================================
@bottle.get('/izberi_rot_1/')
def izberi_rot_1():
    try:
        izbira = bottle.request.query['izberi_rotor1']
    except KeyError:
        return bottle.template('izberi_rot_1.tpl', zrc= zrcalo)
    
    global rotor1
    izbira_poz = int(bottle.request.query['rot1_poz'])
    poz = izbira_poz - 1


    if izbira == 'a_rot1':
        izbira_per = bottle.request.query['a_rot1_per']
        if izbira_per == '1':
            rotor1 = model.Rotor(model.per1, poz)
            return bottle.template('izberi_rot_2.tpl', rot1 = rotor1)
        elif izbira_per == '2':
            rotor1 = model.Rotor(model.per2, poz)
            return bottle.template('izberi_rot_2.tpl', rot1 = rotor1)
        elif izbira_per == '3':
            rotor1 = model.Rotor(model.per3, poz)
            return bottle.template('izberi_rot_2.tpl', rot1 = rotor1)
        elif izbira_per == '4':
            rotor1 = model.Rotor(model.per4, poz)
            return bottle.template('izberi_rot_2.tpl', rot1 = rotor1)
        elif izbira_per == '5':
            rotor1 = model.Rotor(model.per5, poz)
            return bottle.template('izberi_rot_2.tpl', rot1 = rotor1)
        

    elif izbira == 'b_rot1':
        rotor1 = model.Rotor(model.ustvari_rotor(), poz)
        return bottle.template('izberi_rot_2.tpl', rot1 = rotor1)

    elif izbira == 'c_rot1':
        vnos_rot = bottle.request.query['doloci_rot1']
        vnos_rot_2 = vnos_rot.lstrip('[').rstrip(']').replace(' ', '').split(',')
        if all(i.isnumeric() for i in vnos_rot_2) and vnos_rot_2 != []:
            vnos_rot_3 = list(map(int, vnos_rot_2))
            if model.preveri_rotor(vnos_rot_3):
                rotor1 = model.Rotor(vnos_rot_3, poz)
                return bottle.template('izberi_rot_2.tpl', rot1 = rotor1)
            else:
                return bottle.template('izberi_rot_1.tpl', zrc= zrcalo)
        else:
            return bottle.template('izberi_rot_1.tpl', zrc= zrcalo)

#========================================================================================================
@bottle.get('/izberi_rot_2/')
def izberi_rot_2():
    try:
        izbira = bottle.request.query['izberi_rotor2']
    except KeyError:
        return bottle.template('izberi_rot_2.tpl', rot1 = rotor1)
    
    global rotor2
    izbira_poz = int(bottle.request.query['rot2_poz'])
    poz = izbira_poz - 1


    if izbira == 'a_rot2':
        izbira_per = bottle.request.query['a_rot2_per']
        if izbira_per == '1':
            rotor2 = model.Rotor(model.per1, poz)
            return bottle.template('izberi_rot_3.tpl', rot2 = rotor2)
        elif izbira_per == '2':
            rotor2 = model.Rotor(model.per2, poz)
            return bottle.template('izberi_rot_3.tpl', rot2 = rotor2)
        elif izbira_per == '3':
            rotor2 = model.Rotor(model.per3, poz)
            return bottle.template('izberi_rot_3.tpl', rot2 = rotor2)
        elif izbira_per == '4':
            rotor2 = model.Rotor(model.per4, poz)
            return bottle.template('izberi_rot_3.tpl', rot2 = rotor2)
        elif izbira_per == '5':
            rotor2 = model.Rotor(model.per5, poz)
            return bottle.template('izberi_rot_3.tpl', rot2 = rotor2)
        

    elif izbira == 'b_rot2':
        rotor2 = model.Rotor(model.ustvari_rotor(), poz)
        return bottle.template('izberi_rot_3.tpl', rot2 = rotor2)

    elif izbira == 'c_rot2':
        vnos_rot = bottle.request.query['doloci_rot2']
        vnos_rot_2 = vnos_rot.lstrip('[').rstrip(']').replace(' ', '').split(',')
        if all(i.isnumeric() for i in vnos_rot_2) and vnos_rot_2 != []:
            vnos_rot_3 = list(map(int, vnos_rot_2))
            if model.preveri_rotor(vnos_rot_3):
                rotor2 = model.Rotor(vnos_rot_3, poz)
                return bottle.template('izberi_rot_3.tpl', rot2 = rotor2)
            else:
                return bottle.template('izberi_rot_2.tpl', rot1= rotor1)
        else:
            return bottle.template('izberi_rot_2.tpl', rot1= rotor1)

#========================================================================================================
@bottle.get('/izberi_rot_3/')
def izberi_rot_3():
    global rotor2
    try:
        izbira = bottle.request.query['izberi_rotor3']
    except KeyError:
        return bottle.template('izberi_rot_3.tpl', rot2 = rotor2)
    
    global rotor3
    izbira_poz = int(bottle.request.query['rot3_poz'])
    poz = izbira_poz - 1


    if izbira == 'a_rot3':
        izbira_per = bottle.request.query['a_rot3_per']
        if izbira_per == '1':
            rotor3 = model.Rotor(model.per1, poz)
            return bottle.template('izberi_pb.tpl', rot3 = rotor3)
        elif izbira_per == '2':
            rotor2 = model.Rotor(model.per2, poz)
            return bottle.template('izberi_pb.tpl', rot3 = rotor3)
        elif izbira_per == '3':
            rotor2 = model.Rotor(model.per3, poz)
            return bottle.template('izberi_pb.tpl', rot3 = rotor3)
        elif izbira_per == '4':
            rotor2 = model.Rotor(model.per4, poz)
            return bottle.template('izberi_pb.tpl', rot3 = rotor3)
        elif izbira_per == '5':
            rotor2 = model.Rotor(model.per5, poz)
            return bottle.template('izberi_pb.tpl', rot3 = rotor3)
        

    elif izbira == 'b_rot3':
        rotor3 = model.Rotor(model.ustvari_rotor(), poz)
        return bottle.template('izberi_pb.tpl', rot3 = rotor3)

    elif izbira == 'c_rot3':
        vnos_rot = bottle.request.query['doloci_rot3']
        vnos_rot_2 = vnos_rot.lstrip('[').rstrip(']').replace(' ', '').split(',')
        if all(i.isnumeric() for i in vnos_rot_2) and vnos_rot_2 != []:
            vnos_rot_3 = list(map(int, vnos_rot_2))
            if model.preveri_rotor(vnos_rot_3):
                rotor3 = model.Rotor(vnos_rot_3, poz)
                return bottle.template('izberi_pb.tpl', rot3 = rotor3)
            else:
                return bottle.template('izberi_rot_3.tpl', rot2 = rotor2)
        else:
            return bottle.template('izberi_rot_3.tpl', rot2 = rotor2)

#========================================================================================================
@bottle.get('/izberi_pb/')
def izberi_zrc():
    try:
        izbira = bottle.request.query['izberi_pb']
    except KeyError:
        return bottle.template('izberi_pb.tpl', rot3 = rotor3)

    global plugboard

    if izbira == 'a_pb':
        plugboard = model.plugboard
        return bottle.template('vnos_besedila.tpl', pb= plugboard)
        
    elif izbira == 'b_pb':
        plugboard = model.ustvari_plugboard()
        return bottle.template('vnos_besedila.tpl', pb= plugboard)

    elif izbira == 'c_pb':
        vnos_pb = bottle.request.query['doloci_pb']
        vnos_pb_2 = vnos_pb.lstrip('[').rstrip(']').replace(' ', '').split(',')
        if all(i.isnumeric() for i in vnos_pb_2) and vnos_pb_2 != []:
            vnos_pb_3 = list(map(int, vnos_pb_2))
            if model.preveri_plugboard(vnos_pb_3):
                plugboard = vnos_pb_3
                return bottle.template('vnos_besedila.tpl', pb= plugboard)
            else:
                return bottle.template('izberi_pb.tpl', rot3= rotor3)
        else:
            return bottle.template('izberi_pb.tpl', rot3= rotor3)

#========================================================================================================
@bottle.get('/izbira_besedila/')
def izbira_besedila():
    besedilo = bottle.request.query['vnos_besedila']
    besedilo2 = besedilo.replace('Ä', 'c').replace('Å¡', 's').replace('Å¾', 'z').replace('Å½', 'z').replace('Å', 's')

    urejeno_besedilo = model.uredi_besedilo(besedilo2)

    global rotor1, rotor2, rotor3, plugboard, zrcalo, izbrana_koda, kodirano_besedilo
    izbrana_koda = model.Koda(rotor1, rotor2, rotor3, plugboard, zrcalo)
    kodirano_besedilo = model.kodiraj_besedilo(besedilo, izbrana_koda)

    if urejeno_besedilo == '':
        return bottle.template('vnos_besedila.tpl', pb= plugboard)
    else:
        return bottle.template('kodiraj.tpl', rot1= rotor1, rot2= rotor2, rot3= rotor3,
                                zrc= zrcalo, pb= plugboard, tekst= urejeno_besedilo)

#========================================================================================================
@bottle.get('/kodiraj/')
def kodiraj():
    global kodirano_besedilo
    return bottle.template('koda.tpl', tekst = kodirano_besedilo)

#========================================================================================================
@bottle.get('/nazaj/')
def nazaj():
    return bottle.template('osnovni_zaslon.tpl', sporocilo = tekstovni_vmesnik.sporocilo_skrajsano)

bottle.run(debug=True, reloader=True)