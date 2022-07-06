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
        
    if izbira == 'a_zrc':
        return bottle.template('izberi_rot_1.tpl', zrc= zrcalo)
        
    elif izbira == 'b_zrc':
        global zrcalo
        zrcalo = model.ustvari_zrcalo()
        return bottle.template('izberi_rot_1.tpl', zrc= zrcalo)

    elif izbira == 'c_zrc':
        vnos_zrc = bottle.request.query['doloci_zrc']
        vnos_zrc_2 = vnos_zrc.lstrip('[').rstrip(']').replace(' ', '').split(',')
        if all(i.isnumeric() for i in vnos_zrc_2) and vnos_zrc_2 != []:
            vnos_zrc_3 = list(map(int, vnos_zrc_2))
            if model.preveri_zrcalo(vnos_zrc_3):
                global zrcalo
                zrcalo = vnos_zrc_3
                return bottle.template('izberi_rot_1.tpl', zrc= zrcalo)
        else:
            return bottle.template('izberi_zrc.tpl')

#========================================================================================================
@bottle.get('/izberi_rot_1/')
def izberi_rot_1():
    try:
        izbira = bottle.request.query['izberi_zrcalo']
    except KeyError:
        return bottle.template('izberi_rot_1.tpl')
    
    izbira_poz = int(bottle.request.query('rot1_poz'))

    if izbira == 'a_zrc':
        izbira_per = bottle.request.query('a_rot1_per')
        if izbira_per == '1':
            global rotor1
            rotor1 = model.Rotor(model.per1, izbira_poz)
            return bottle.template('izberi_rot_2.tpl', rot1 = rotor1)
        elif izbira_per == '2':
            global rotor1
            rotor1 = model.Rotor(model.per2, izbira_poz)
            return bottle.template('izberi_rot_2.tpl', rot1 = rotor1)
        elif izbira_per == '3':
            global rotor1
            rotor1 = model.Rotor(model.per3, izbira_poz)
            return bottle.template('izberi_rot_2.tpl', rot1 = rotor1)
        elif izbira_per == '4':
            global rotor1
            rotor1 = model.Rotor(model.per4, izbira_poz)
            return bottle.template('izberi_rot_2.tpl', rot1 = rotor1)
        elif izbira_per == '5':
            global rotor1
            rotor1 = model.Rotor(model.per5, izbira_poz)
            return bottle.template('izberi_rot_2.tpl', rot1 = rotor1)
        

    elif izbira == 'b_zrc':
        global rotor1
        rotor1 = model.Rotor(model.ustvari_rotor(), izbira_poz)
        return bottle.template('izberi_rot_2.tpl', rot1 = rotor1)

    elif izbira == 'c_zrc':
        vnos_rot = bottle.request.query['doloci_zrc']
        vnos_rot_2 = vnos_rot.lstrip('[').rstrip(']').replace(' ', '').split(',')
        if all(i.isnumeric() for i in vnos_rot_2) and vnos_rot_2 != []:
            vnos_rot_3 = list(map(int, vnos_rot_2))
            if model.preveri_zrcalo(vnos_rot_3):
                global rotor1
                rotor1 = vnos_rot_3
                return bottle.template('izberi_rot_2.tpl', rot1 = rotor1)
        else:
            return bottle.template('izberi_rot_1.tpl', zrc= zrcalo)
            
#========================================================================================================
        



bottle.run(debug=True, reloader=True)