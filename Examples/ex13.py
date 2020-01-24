from bottle import Bottle, run, template

# create an instance of class Bottle
app = Bottle()

@app.route('/welcome')
def welcome():
    # looks for ./views/welcome.tpl or .html
    return template('welcome', msg='Welcome to BottlePy')

# this function will be invoked when a client makes a URL requests like:
# http://localhost:1234/
# http://localhost:1234/home
@app.route('/')
def index():
    return '''<h1>Hello, World!</h1>
    <hr>
    <p>Demo by Vinod</p>
    '''

# on unix platforms, run with 'sudo'
run(app, port=80, debug=True, reloader=True)