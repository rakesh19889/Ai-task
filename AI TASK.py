# app.py
from flask import Flask, request, jsonify
from langchain.vectorstores import FAISS

app = Flask(__name__)

# Load the vector store
vector_store = FAISS.load('vector_store.faiss')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    
    # Generate a response using the vector store
    response = vector_store.query(user_input)
    
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
