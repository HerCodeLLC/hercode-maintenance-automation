import json
from flask import Flask, request, jsonify

from maintenance_logic import process_maintenance_request

app = Flask(__name__)

def handle_request(request_data):
    """
    Receive maintenance request data, process it,
    and return the finished result as JSON.
    """

    processed_request = process_maintenance_request(request_data)

    return json.dumps(processed_request, indent=4)

@app.route("/maintenance", methods=["POST"])
def maintenance():
    """
    Receive a maintenance request through the API
    and return the processed maintenance decision.
    """
    request_data = request.get_json()

    processed_request = process_maintenance_request(request_data)

    return jsonify(processed_request)

if __name__ == "__main__":
    app.run(debug=True, port=5001)