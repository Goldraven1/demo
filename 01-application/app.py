from flask import Flask, render_template, jsonify
import socket
import os
import signal
import sys

app = Flask(__name__)

@app.route('/')
def index():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    author = os.environ.get('AUTHOR', 'Не указан')
    
    return render_template('index.html', hostname=hostname, ip_address=ip_address, author=author)

@app.route('/health')
def health():
    return jsonify({"status": "ok"}), 200

def signal_handler(sig, frame):
    print('Получен сигнал завершения, закрываем приложение...')
    sys.exit(0)

if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
    app.run(host='0.0.0.0', port=8000)
