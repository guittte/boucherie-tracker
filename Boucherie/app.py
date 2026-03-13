from flask import Flask, jsonify
from services.users_service import users_bp
from services.butcheries_service import butcheries_bp

app = Flask(__name__)

# Register blueprints
app.register_blueprint(users_bp, url_prefix='/api/v1/users')
app.register_blueprint(butcheries_bp, url_prefix='/api/v1/butcheries')

@app.route('/')
def health_check():
    return jsonify({"status": "API Gateway / Core Service is running"})

@app.route('/api/v1/health')
def api_health():
    return jsonify({"status": "OK", "version": "1.0"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
