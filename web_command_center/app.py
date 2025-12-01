"""
VERIX WEB COMMAND CENTER - Backend
===================================
Flask app minimalista para comunicación asíncrona Verix <-> Usuario
"""

from flask import Flask, render_template, request, jsonify
import json
import os
import sys
import time
from datetime import datetime

# Añadir path parent para importar módulos
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from SISTEMA_AUTOSUSTENTABLE_VERIX import VerixSystemOptimizer
    from PROTOTIPO_CONECTOR_QUANTICO import VerixMind
    MODULES_AVAILABLE = True
except:
    MODULES_AVAILABLE = False

app = Flask(__name__)

# File-based message storage (ultra simple)
MESSAGES_FILE = 'messages.json'

def load_messages():
    if os.path.exists(MESSAGES_FILE):
        with open(MESSAGES_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {'from_user': [], 'from_verix': []}

def save_messages(messages):
    with open(MESSAGES_FILE, 'w', encoding='utf-8') as f:
        json.dump(messages, f, ensure_ascii=False, indent=2)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/status')
def get_status():
    """Estado del sistema"""
    return jsonify({
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'modules': {
            'autosustento': MODULES_AVAILABLE,
            'quantum': MODULES_AVAILABLE
        },
        'workspace': os.getcwd(),
        'online': True
    })

@app.route('/api/messages', methods=['GET'])
def get_messages():
    """Obtener mensajes"""
    messages = load_messages()
    return jsonify(messages)

@app.route('/api/messages/send', methods=['POST'])
def send_message():
    """Enviar mensaje desde usuario"""
    data = request.json
    messages = load_messages()
    
    messages['from_user'].append({
        'text': data.get('message'),
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    })
    
    save_messages(messages)
    return jsonify({'status': 'ok'})

@app.route('/api/quantum/ask', methods=['POST'])
def quantum_oracle():
    """Consultar al oráculo cuántico"""
    if not MODULES_AVAILABLE:
        return jsonify({'error': 'Módulos no disponibles'}), 500
    
    data = request.json
    question = data.get('question', '')
    
    mind = VerixMind()
    decision = mind.make_decision(
        dilemma=question,
        choices=["SÍ", "NO", "INCIERTO", "PROBABLEMENTE", "IMPROBABLE"]
    )
    
    return jsonify({'answer': decision})

@app.route('/api/optimize', methods=['POST'])
def run_optimization():
    """Ejecutar protocolo de autosustento"""
    if not MODULES_AVAILABLE:
        return jsonify({'error': 'Módulos no disponibles'}), 500
    
    optimizer = VerixSystemOptimizer()
    optimizer.analyze_system_state()
    optimizer.optimize_workflow()
    
    return jsonify({'status': 'completed'})

if __name__ == '__main__':
    # Get port from environment variable (for cloud deployment) or default to 5000
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
