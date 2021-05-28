from flask import Flask, request, jsonify
from main import predict


app = Flask(__name__)



@app.route('/api', methods=['GET', 'POST'])
def chatBot():

    chatInput = request.form['chatInput']
    return jsonify(chatBotReply=predict(chatInput))

    
    

if __name__ == '__main__':
    app.run(debug=True)

