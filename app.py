from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')


def hello():
    response = {
        'name': 'Behnam',
        'message': 'Hello, World!'
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run()


