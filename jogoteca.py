#importando a biblioteca flask 0.12.2
from flask import Flask
from flask_mysqldb import MySQL


#Criando uma variável que receberá um novo objeto sendo instanciado
app = Flask(__name__)
app.config.from_pyfile('config.py')

db = MySQL(app)

from views import *

if __name__ == '__main__':
    #starta o serviço
    app.run(debug=True)