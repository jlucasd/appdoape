from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pagamentos')
def pagamentos():
    return render_template('pagamentos.html', payers=getPayers())

@app.route('/contas',methods = ['POST', 'GET'])
def contas():
    return render_template('contas.html', residents=getResidents())

def getPayers():

    residents = getResidents()

    return {'Janeiro': residents[1],
            'Fevereiro': residents[2],
            'Março': residents[0],
            'Abril': residents[1],
            'Maio': residents[2],
            'Junho': residents[0],
            'Julho': residents[1],
            'Agosto': residents[2],
            'Setembro': residents[0],
            'Outubro': residents[1],
            'Novembro': residents[2],
            'Dezembro': residents[0]
           }

def getResidents():
    return ['João' , 'Julio', 'Marcos']

if __name__ == '__main__':
    print("server is runing!!")
    app.run(debug=True)
