from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    user_input = data.get('message', '')

    try:
        # Make request to Ollama's local API
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "mistral",
                "prompt": user_input,
                "stream": False
            }
        )
        result = response.json()
        answer = result.get("response", "Computer: I couldn't think of a reply.")
        return jsonify({'response': f'Computer: {answer}'})
    except Exception as e:
        return jsonify({'response': f'Computer: Something went wrong while processing your request.\n\n{str(e)}'})

if __name__ == '__main__':
    app.run(debug=True)
