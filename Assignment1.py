from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/hello', methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        return jsonify({"message": "world"}), 200
    elif request.method == 'POST':
        return jsonify({"error": "Method Not Allowed"}), 405


@app.route('/hello/<name>', methods=['GET'])
def hello_name_get(name):
    return jsonify({"error": "Method Not Allowed"}), 405


@app.route('/hello/<name>', methods=['POST'])
def hello_name_post(name):
    return jsonify({"message": f"Hi, {name}."}), 200


@app.route('/test', methods=['GET'])
def test():
    if request.method == 'GET':
        return jsonify({"message": "test is successful"}), 200
    elif request.method == 'POST':
        return jsonify({"error": "Bad Request"}), 400


@app.route('/test', methods=['POST'])
def test_with_params():
    message = request.args.get('msg')
    if message:
        return jsonify({"message": message}), 200
    else:
        return jsonify({"error": "Bad Request"}), 400


if __name__ == '__main__':
    app.run(debug=True, port=8090, host='0.0.0.0')
