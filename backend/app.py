from flask import Flask, jsonify, request # Added 'request' to handle uploads
from flask_cors import CORS
from ml_pipeline import run_analysis

app = Flask(__name__)
CORS(app) 

# 1. Changed method to POST so it can securely receive file payloads
@app.route('/analyze', methods=['POST'])
def analyze():
    print("\n[Server] 🌐 Incoming file upload from frontend...")
    
    # 2. Check if a file was actually sent in the request
    if 'dataset' not in request.files:
        return jsonify({"status": "error", "message": "No file uploaded."}), 400
        
    file = request.files['dataset']
    
    if file.filename == '':
        return jsonify({"status": "error", "message": "Empty file."}), 400

    try:
        # 3. Pass the raw file directly into your machine learning logic!
        results = run_analysis(file)
        
        return jsonify({
            "status": "success",
            "data": results
        }), 200
        
    except Exception as e:
        print(f"[Server] ❌ Error: {e}")
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

if __name__ == '__main__':
    print("[Server] 🚀 Flask backend is running on http://127.0.0.1:5000")
    app.run(debug=True, port=5000)