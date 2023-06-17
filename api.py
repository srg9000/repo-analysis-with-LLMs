from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/process-url", methods=["POST"])
def process_url():
    data = request.get_json()
    url = data["url"]
    
    # Process the URL here using your own logic
    processed_url = "https://example.com/processed"
    
    return jsonify({"processedURL": processed_url})

if __name__ == "__main__":
    app.run()
