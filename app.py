import os
from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    content = {
        'ape': 'Edifício Donalane - 1102',
        'titulo' : 'App do Apê',
        'secao' : 'Moradores'
    }
    
    return render_template('index.html', content=content, users=getUsers())

@app.route('/pagamentos')
def pagamentos():
    return render_template('pagamentos.html', payers=getPayers(), columns=getColumns(), year=getYear())

@app.route('/contas',methods = ['POST', 'GET'])
def contas():
    return render_template('contas.html', residents=getResidents(), currentPayer=getCurrentPayer())

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

def getYear():
    now = datetime.now()
    return now.year

def getCurrentPayer():
	months = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho","Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
	currentMonth = months[(datetime.now().month - 1)]
	payers = getPayers()
	return payers[currentMonth]

def getResidents():
    return ['Julio', 'Marcos', 'João']

def getUsers():
    users = {
        'joaolucas.damiani': 'joao',
        'julio.h.bitencourt': 'julio',
        'marcos.rc10': 'marcos'
    }
    return users

if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)
    # print("server is runing!!")
    # app.run(debug=True)
