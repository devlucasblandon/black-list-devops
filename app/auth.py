from functools import wraps
from flask import request, jsonify

# Token estático predefinido
API_TOKEN = "blacklist-secret-token-2024"

def require_token(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        
        if not token:
            return jsonify({
                'success': False,
                'message': 'Token de autorización no proporcionado'
            }), 401
            
        # Removemos el prefijo 'Bearer ' si existe
        if token.startswith('Bearer '):
            token = token.split(' ')[1]
            
        if token != API_TOKEN:
            return jsonify({
                'success': False,
                'message': 'Token de autorización inválido'
            }), 401
            
        return f(*args, **kwargs)
    return decorated 