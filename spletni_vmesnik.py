import bottle
import model

@bottle.get('/')
def osnovni_zaslon():
    return bottle.template('osnovni_zaslon.tpl')

bottle.run(debug=True, reloader=True)