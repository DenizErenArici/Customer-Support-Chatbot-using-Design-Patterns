from flask import Flask, request, jsonify, render_template
from chatbot import Chatbot
import uuid

app = Flask(__name__)
chatbot = Chatbot()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/faq')
def faq():
    return render_template('faqscreen.html')

@app.route('/connect')
def connect():
    return render_template('connecttoagent.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    session_id = request.json.get('session_id', str(uuid.uuid4()))
    response = chatbot.handle_message(user_message, session_id)
    return jsonify({'response': response, 'session_id': session_id})

if __name__ == '__main__':
    app.run(debug=True)