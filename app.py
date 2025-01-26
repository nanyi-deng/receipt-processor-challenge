from flask import Flask, request, jsonify
from db import store_receipt, get_receipt
from calculator import calculate_points

app = Flask(__name__)

@app.route('/receipts/process', methods=['POST'])
def process_receipt():
    # check if JSON data is provided
    data = request.get_json()
    if not data:
        return jsonify({
            "message": "It looks like you're missing valid JSON data."
        }), 400

    # store the receipt (assuming it's valid)
    receipt_id = store_receipt(data)

    # return the generated receipt ID
    return jsonify({
        "receipt_id": receipt_id,
        "note": "Your receipt has been successfully stored!"
    }), 201


@app.route('/receipts/<receipt_id>/points', methods=['GET'])
def fetch_points(receipt_id):
    # fetch the receipt by its ID
    receipt = get_receipt(receipt_id)
    if not receipt:
        return jsonify({
            "error": "We couldn’t find a receipt with that ID."
        }), 404

    # calculate the points (assuming it's valid)
    points = calculate_points(receipt)

    return jsonify({
        "points": points,
        "message": "Points calculation completed successfully!"
    }), 200


if __name__ == '__main__':
    app.run(debug=True)
