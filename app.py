import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({
        'message': 'Hello from AWS App Runner!',
        'environment': os.environ.get('ENVIRONMENT', 'development'),
        'port': os.environ.get('PORT', '8080')
    })

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    # App Runner proporciona el puerto a través de la variable de entorno PORT
    port = int(os.environ.get('PORT', 8080))
    
    # IMPORTANTE: Siempre usar host='0.0.0.0' para App Runner
    app.run(host='0.0.0.0', port=port, debug=False) 