import bottle
import model
import tekstovni_vmesnik

@bottle.get('/')
def osnovni_zaslon():
    return bottle.template('osnovni_zaslon.tpl', sporocilo = tekstovni_vmesnik.sporocilo_skrajsano)

@bottle.get('/izberi_zrc/')
def izbira_zrcala():
    return bottle.template('izberi_zrc.tpl')

@bottle.get('/izberi_rot/')
def izberi_zrc():
    izbira = bottle.request.query['izberi_zrcalo']
    if izbira == 'a_zrc':
        return bottle.template('izberi_rot.tpl', zrc=model.zrcalo)
    elif izbira == 'b_zrc':
        return bottle.template('izberi_rot.tpl', zrc=model.ustvari_zrcalo())
    elif izbira == 'c_zrc':
        vnos_zrc = bottle.request.query['doloci_zrc']
        print(vnos_zrc)
        return bottle.template('izberi_zrc.tpl')
    else:
        return bottle.template('izberi_zrc.tpl')
        
        



bottle.run(debug=True, reloader=True)