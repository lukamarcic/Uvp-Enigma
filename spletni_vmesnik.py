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

#========================================================================================================
@bottle.get('/izberi_rot_1/')
def izberi_rot_1():
    try:
        izbira = bottle.request.query['izberi_rotor1']
    except KeyError:
        return bottle.template('izberi_rot_1.tpl', zrc= zrcalo)
    
    global rotor1
    izbira_poz = bottle.request('rot1_poz')

    if izbira == 'a_rot1':
        return bottle.template('izberi_rot_1.tpl', zrc= zrcalo)
#        izbira_per = bottle.request.query('a_rot1_per')
#        
#        if izbira_per == '1':
#            rotor1 = model.Rotor(model.per1, 0)
#            return bottle.template('izberi_rot_2.tpl', rot1 = rotor1)
#        elif izbira_per == '2':
#            rotor1 = model.Rotor(model.per2, 0)
#            return bottle.template('izberi_rot_2.tpl', rot1 = rotor1)
#        elif izbira_per == '3':
#            rotor1 = model.Rotor(model.per3, 0)
#            return bottle.template('izberi_rot_2.tpl', rot1 = rotor1)
#        elif izbira_per == '4':
#            rotor1 = model.Rotor(model.per4, 0)
#            return bottle.template('izberi_rot_2.tpl', rot1 = rotor1)
#        elif izbira_per == '5':
#            rotor1 = model.Rotor(model.per5, 0)
#            return bottle.template('izberi_rot_2.tpl', rot1 = rotor1)
        

    elif izbira == 'b_rot1':
        rotor1 = model.Rotor(model.ustvari_rotor(), 0)
        return bottle.template('izberi_rot_2.tpl', rot1 = rotor1)

    elif izbira == 'c_rot1':
        vnos_rot = bottle.request.query['doloci_rot1']
        vnos_rot_2 = vnos_rot.lstrip('[').rstrip(']').replace(' ', '').split(',')
        if all(i.isnumeric() for i in vnos_rot_2) and vnos_rot_2 != []:
            vnos_rot_3 = list(map(int, vnos_rot_2))
            if model.preveri_rotor(vnos_rot_3):
                rotor1 = model.Rotor(vnos_rot_3, 0)
                return bottle.template('izberi_rot_2.tpl', rot1 = rotor1)
        else:
            return bottle.template('izberi_rot_1.tpl', zrc= zrcalo)

#========================================================================================================
        



bottle.run(debug=True, reloader=True)