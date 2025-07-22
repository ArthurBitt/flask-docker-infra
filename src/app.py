from flask import Flask, request
import redis
from datetime import datetime

app = Flask(__name__)

# Conexão com o Redis (padrão: localhost, porta 6379)
r = redis.Redis(host='redis', port=6379, db=0)

def log_to_redis(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    full_message = f"[{timestamp}] {message}"
    r.lpush("flask_logs", full_message)        # adiciona no início da lista
    r.ltrim("flask_logs", 0, 99)               # mantém apenas os 100 mais recentes (cache leve)

@app.route('/health_check')
def health_check():
    log_to_redis("health_check endpoint foi chamado")
    return {'status':'ok'}, 200

if __name__ == '__main__':
    log_to_redis("Servidor Flask iniciando...")
    app.run(debug=True, host='0.0.0.0', port=5000)
