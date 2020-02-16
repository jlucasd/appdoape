import os
from flask import Flask, render_template, request, redirect, url_for, session
from datetime import datetime
from forms import FormLogin
from config import Config
from database.base import Base
import sqlite3
from dotenv import load_dotenv 

app = Flask(__name__)
app.config.from_object(Config)

base = Base()

@app.route('/')
def index():
    if not session.get('logged_in'):
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
    form = FormLogin()
    if form.validate_on_submit():
        if((form.user.data == 'apesenai') and (form.password.data == 'apesenai')):
            session['logged_in'] = True
            return redirect(url_for('index'))
    return render_template('login.html', form=form)

@app.route('/logout', methods=['GET'])
def logout():
    session['logged_in'] = False
    return index()

@app.route('/pagamentos')
#@login_required
def pagamentos():
    return render_template('pagamentos.html', payers=getPayers(), columns=getColumns(), year=getCurrentYear())

@app.route('/contas',methods = ['POST', 'GET'])
#@login_required
def contas():
    return render_template('contas.html', residents=getResidents(), currentPayer=getCurrentPayer())

@app.route('/caixa',methods = ['POST', 'GET'])
#@login_required
def caixa():
    meses = diff_month(datetime(2020,2,1), datetime.now()) + 1
    valor = meses * 20
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
    usuarios = [user for user in base.get_users()]
    return usuarios

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
