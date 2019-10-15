import os
from flask import Flask, render_template, request, redirect, url_for, session
from datetime import datetime
from forms import FormLogin
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

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
        if((form.user.data == 'apsenai') and (form.password.data == 'apsenai')):
            session['logged_in'] = True
            return redirect(url_for('index'))
    return render_template('login.html', form=form)

@app.route('/logout', methods=['GET'])
def logout():
    session['logged_in'] = False
    return index()

@app.route('/pagamentos')
def pagamentos():
    return render_template('pagamentos.html', payers=getPayers(), columns=getColumns(), year=getCurrentYear())

@app.route('/contas',methods = ['POST', 'GET'])
def contas():
    return render_template('contas.html', residents=getResidents(), currentPayer=getCurrentPayer())

def getMonths():
    return ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho","Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

def getPayers():

    residents = getResidents()

    return {'Janeiro': residents[0],
            'Fevereiro': residents[1],
            'Março': residents[2],
            'Abril': residents[0],
            'Maio': residents[1],
            'Junho': residents[2],
            'Julho': residents[0],
            'Agosto': residents[1],
            'Setembro': residents[2],
            'Outubro': residents[0],
            'Novembro': residents[1],
            'Dezembro': residents[2]
           }

def getColumns():
    return ["Nº", "Mês", "Pagador"]

def getCurrentYear():
    return datetime.now().year

def getCurrentPayer():
	currentMonth = getMonths()[(datetime.now().month - 1)]
	return {'payer' : getPayers()[currentMonth], 'month' : currentMonth}

def getResidents():
    return ['Julio', 'Marcos', 'João']

def getUsers():
    return {
        'joao': 'joaolucas.damiani',
        'julio': 'julio.h.bitencourt',
        'marcos': 'profile.php?id=100002460771942' 
    }

if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    # print("server is runing!!")
    # app.run(debug=True)
