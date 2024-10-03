from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro/eleitor', methods=['GET', 'POST'])
def cadastro_eleitor():
    if request.method == 'POST':
        nome = request.form['nome']
        data_nascimento = request.form['data_nascimento']
        endereco = request.form['endereco']
        cpf = request.form['cpf']
        zona = request.form['zona']
        
        return render_template('confirmacao.html', tipo='eleitor', dados={
            'Nome': nome,
            'Data de Nascimento': data_nascimento,
            'Endereço': endereco,
            'CPF': cpf,
            'Zona': zona
        })

    return render_template('cadastro_eleitor.html')

@app.route('/cadastro/candidato', methods=['GET', 'POST'])
def cadastro_candidato():
    if request.method == 'POST':
        partido = request.form['partido']
        nome = request.form['nome']
        idade = request.form['idade']
        endereco = request.form['endereco']
        rg = request.form['rg']
        
        return render_template('confirmacao.html', tipo='candidato', dados={
            'Partido': partido,
            'Nome': nome,
            'Idade': idade,
            'Endereço': endereco,
            'RG': rg
        })

    return render_template('cadastro_candidato.html')

@app.route('/cadastro/partido', methods=['GET', 'POST'])
def cadastro_partido():
    if request.method == 'POST':
        numero_partido = request.form['numero_partido']
        sigla = request.form['sigla']
        nome = request.form['nome']
        cidade = request.form['cidade']
        uf = request.form['uf']
        
        return render_template('confirmacao.html', tipo='partido', dados={
            'Número do Partido': numero_partido,
            'Sigla': sigla,
            'Nome': nome,
            'Cidade': cidade,
            'UF': uf
        })

    return render_template('cadastro_partido.html')

@app.route('/cadastro/local_votacao', methods=['GET', 'POST'])
def cadastro_local_votacao():
    if request.method == 'POST':

        zona = request.form['zona']
        endereco = request.form['endereco']
        bairro = request.form['bairro']
        cidade = request.form['cidade']
        uf = request.form['uf']
        
        return render_template('confirmacao.html', tipo='local_votacao', dados={
            'Zona': zona,
            'Endereço': endereco,
            'Bairro': bairro,
            'Cidade': cidade,
            'UF': uf
        })

    return render_template('cadastro_local_votacao.html')

@app.route('/cadastro/mesario', methods=['GET', 'POST'])
def cadastro_mesario():
    if request.method == 'POST':
        nome = request.form['nome']
        data_nascimento = request.form['data_nascimento']
        endereco = request.form['endereco']
        escolaridade = request.form['escolaridade']
        
        return render_template('confirmacao.html', tipo='mesario', dados={
            'Nome': nome,
            'Data de Nascimento': data_nascimento,
            'Endereço': endereco,
            'Escolaridade': escolaridade
        })

    return render_template('cadastro_mesario.html')

@app.route('/confirmar', methods=['POST'])
def confirmar():
    tipo = request.form['tipo']
    dados = request.form.to_dict(flat=False)


    return render_template('sucesso.html', tipo=tipo)

@app.route('/voltar', methods=['POST'])
def voltar():
    return redirect(request.form['url'])

if __name__ == '__main__':
    app.run(debug=True)
