
from flask import Flask, session, render_template, request
from flask import copy_current_request_context
from converter import convert_unit

from DBcm import UseDatabase, ConnectionError, CredentialsError, SQLError
from checker import checked_logged_in

from threading import Thread
from time import sleep


app = Flask(__name__)

# set secret key
secret_key = "YouWillNeverGuess"

# app.config
app.config['dbconfig'] = {'host': '127.0.0.1',
                          'user': 'converter',
                          'password': 'converterpasswd',
                          'database': 'converterlogDB'


# create decorator
def check_logged_in(func) -> 'func':

    @wraps
    def wrapper(*args,**kwargs):
        # get the user, check the session
        if request.user in session:
            return func
        print('You are NOT logged in.')
    return wrapper



@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    title = 'Welcome to unit conversion web service!'
    return render_template('entry.html',
                           the_title=title)


@app.route('/result')
def result_page() -> 'html':

    # db connection
    with UseDataBase('dbconfig') as cursor:
        # request.form attrs
        _SQL = '''INSERT INTO log
                (entry, ini_unit, result, res_unit, remote_ip, web_browser)
                VALUES
                (%d, %s, %d, %s, %s, %s) 
                '''
        cursor.execute(_SQL, (entry,
                              ini_unit,
                              result,
                              res_unit,
                              request.remote_ip,
                              request.web_browser))

    entry = request.form['entry']
    ini_unit = request.form['ini_unit']
    result, res_unit = convert_unit(entry, ini_unit)
    try:
        # thread
        Thread(target=result_page)
    except Exception as err:
        print('*********Logging error with %s' % err)

    return render_template('result.html',
                           the_entry=entry,
                           ini_unit=ini_unit,
                           the_result=result,
                           res_unit=res_unit)



class UserDataBase:
    def __init__(self,):
        conn = sqlite3.connect('dbconfig')
        cur = conn.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        cur.close()
        conn.close()




app.run(debug=True)
