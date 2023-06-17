from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/process-url", methods=["POST"])
def process_url():
    data = request.get_json()
    url = data["url"]
    
    # Process the URL here using your own logic
    processed_url = "https://example.com/processed"
    
    custom_messages = [
        "This is the first custom message.",
        "Here's another custom message.",
        "And a third custom message.",
    ]
    
    return jsonify({
        "processedURL": processed_url,
        "customMessages": custom_messages
    })

if __name__ == "__main__":
    app.run()


if __name__ == "__main__":
    app.run()
