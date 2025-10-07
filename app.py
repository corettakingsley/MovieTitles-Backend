from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
# Enable CORS for all origins (for testing)
CORS(app)

@app.route('/api/titles')
def get_titles():
    return jsonify([
        {"id": 1, "title": "The Shawshank Redemption", "year": 1994},
        {"id": 2, "title": "The Godfather", "year": 1972},
        {"id": 3, "title": "The Dark Knight", "year": 2008}
    ])

@app.route('/api/health')
def health_check():
    return jsonify({"status": "healthy", "message": "Backend is working!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)