
from flask import Flask, request, jsonify
from banco_dados import iniciar_banco, adicionar_transacao, obter_transacoes, obter_transacoes_por_mes, obter_despesas_por_categoria

app = Flask(__name__)

iniciar_banco()

@app.route('/transacoes', methods=['POST'])
def criar_transacao():
    dados = request.json
    adicionar_transacao(
        dados['tipo'],
        dados['valor'],
        dados['categoria'],
        dados['data']
    )
    return jsonify({'mensagem': 'Transação adicionada com sucesso'}), 201

@app.route('/transacoes', methods=['GET'])
def listar_transacoes():
    transacoes = obter_transacoes()
    return jsonify([{
        'id': t[0],
        'tipo': t[1],
        'valor': t[2],
        'categoria': t[3],
        'data': t[4]
    } for t in transacoes])

@app.route('/mensal', methods=['GET'])
def resumo_mensal():
    dados = obter_transacoes_por_mes()
    return jsonify([{
        'mes': linha[0],
        'tipo': linha[1],
        'total': linha[2]
    } for linha in dados])

@app.route('/categorias', methods=['GET'])
def resumo_categorias():
    dados = obter_despesas_por_categoria()
    return jsonify([{
        'categoria': linha[0],
        'total': linha[1]
    } for linha in dados])

if __name__ == '__main__':
    app.run(debug=True, port=5000)
