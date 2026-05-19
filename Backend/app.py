from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
# O CORS é essencial para o Nginx (porta 80) falar com o Flask (porta 5000)
CORS(app)

# Usuário e senha fixos para teste
USER_TEST = "alexandre"
PASS_TEST = "devops2026"

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    
    # Verifica se os campos existem no JSON enviado
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"erro": "Dados incompletos"}), 400

    username = data.get('username')
    password = data.get('password')

    # Lógica de validação
    if username == USER_TEST and password == PASS_TEST:
        return jsonify({
            "status": "sucesso",
            "mensagem": f"Bem-vindo, {username}!",
            "token": "fake-jwt-token-123"
        }), 200
    else:
        return jsonify({"status": "erro", "mensagem": "Credenciais inválidas"}), 401

if __name__ == '__main__':
    # host 0.0.0.0 é obrigatório para rodar dentro do Docker
    app.run(host='0.0.0.0', port=5000)