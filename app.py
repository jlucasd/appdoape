import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_user, logout_user, login_required, LoginManager
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from forms import FormLogin
from config import Config
from database.base import Base
from models import User
import sqlite3

app = Flask(__name__)
app.config.from_object(Config)
login_manager = LoginManager(app)

base = Base()
database = SQLAlchemy(app)

@app.route('/')
def index():
    if not current_user.is_authenticated:
        return login()
    else:
        content = {
            'ape': 'Edifício Donalane - 1102',
            'titulo' : 'App do Apê',
            'secao' : 'Moradores'
        }
        return render_template('index.html', content=content, users=getUsers())

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
            return redirect(url_for('index'))
    form = FormLogin()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.user.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Usuário ou senha inválidos!', 'danger')
            return redirect(url_for('login'))
        login_user(user, remember=True)
        flash('Bem vindo {}!'.format(current_user.username), 'success')
        return redirect(url_for('index'))
    return render_template('login.html', form=form)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.errorhandler(401)
def not_authenticated(error):
    flash("Faça o login primeiro!", 'danger')
    return redirect(url_for('index'))

@app.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/pagamentos')
@login_required
def pagamentos():
    return render_template('pagamentos.html', payers=getPayers(), columns=getColumns(), year=getCurrentYear())

@app.route('/contas',methods = ['POST', 'GET'])
@login_required
def contas():
    return render_template('contas.html', residents=getResidents(), currentPayer=getCurrentPayer())

@app.route('/caixa',methods = ['POST', 'GET'])
@login_required
def caixa():
    deposito = 20 * len(getResidents())
    meses = diff_month(datetime.now(), datetime(2020,2,1)) + 1
    valor = meses * deposito
    return render_template('caixa.html', valor=valor)

def getMonths():
    return ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho","Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

def getPayers():
    return base.get_payers()

def getColumns():
    return ["Nº", "Mês", "Pagador"]

def getCurrentYear():
    return datetime.now().year

def getCurrentPayer():
	currentMonth = getMonths()[(datetime.now().month - 1)]
	return {'payer' : getPayers()[currentMonth], 'month' : currentMonth}

def getResidents():
    residents = [user for user in base.get_residents()]
    return residents

def getUsers():
    return {
        'joao': 'joaolucas.damiani',
        'julio': 'julio.h.bitencourt',
        'marcos': 'profile.php?id=100002460771942' 
    }

def diff_month(d1, d2):
    return (d1.year - d2.year) * 12 + d1.month - d2.month

if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    # print("server is runing!!")
    #app.run(debug=True)
