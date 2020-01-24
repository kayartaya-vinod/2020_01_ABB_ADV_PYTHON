from bottle import Bottle, run, template
from sqlite3 import connect
import requests

app = Bottle()

def get_joke():
    resp = requests.get('https://api.chucknorris.io/jokes/random')
    return resp.json()['value']

@app.get('/')
def index():
    content = f'''
    <h3>Joke of the moment: </h3>
    <p>{get_joke()}</p>
    '''
    return template('index', content = content)

@app.get('/people-list')
def people_list():
    with connect('mydb.sqlite3') as conn:
        cur = conn.cursor()
        cur.execute('select * from people')
        content = template('people-list', data = cur.fetchall())
        return template('index', content=content)

run(app, port=80, reloader=True, debug=True)