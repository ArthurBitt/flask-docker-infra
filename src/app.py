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

@app.route('/health')
def health():
    return 'ok', 200
