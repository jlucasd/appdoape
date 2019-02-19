from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pagamentos')
def pagamentos():
    return render_template('pagamentos.html', payers=getPayers())

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

def getCurrentPayer():
	months = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho","Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
	currentMonth = months[(datetime.now().month - 1)]
	payers = getPayers()
	return payers[currentMonth]

def getResidents():
    return ['Julio', 'Marcos', 'João']

if __name__ == '__main__':
    print("server is runing!!")
    app.run(debug=True)
