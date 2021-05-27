from flask import Flask, request, jsonify

from main import get_response

app = Flask(__name__)


@app.route('/chat', methods=['GET', 'POST'])
def chatBot():
    chatInput = request.form['chatInput']
    return jsonify(chatBotReply=get_response(chatInput))


if __name__ == '__main__':
    app.run(debug=True)
    
