# هذه هي الدالة الرئيسة للتطبيق 
from flask import Flask, request, jsonify, send_file
from image_loader import load_image_from_folder
from langchain_chroma import Chroma
from langchain_community.embeddings.ollama import OllamaEmbeddings

import os

# Initialize Flask app
app = Flask(__name__)

# Initialize vector database
vectordb = None

def initialize_vectordb():
    global vectordb
    embedding = OllamaEmbeddings(model="nomic-embed-text")
    persist_directory = "/home/abdulmalek-alsalmi/Desktop/SA/the_project/chroma"
    vectordb=Chroma(persist_directory=persist_directory, embedding_function=embedding)

# Define the route for image search
@app.route('/find_image', methods=['POST'])
def find_image():
    # Parse request data
    data = request.get_json()
    text = data.get("text")
    print("Received text:", text)

    if not text:
        return jsonify({"error": "No text provided in request"}), 400

    # Use vectordb to perform similarity search and get the image name
    search_results = vectordb.max_marginal_relevance_search(text, k=1,fetch_k=5)
    if not search_results:
        return jsonify({"error": "No matching image found"}), 404

    # Extract the image name from the first result's page_content
    image_name = search_results[0].page_content
    print("Found image name:", image_name)

    # Load the image from the folder
    image_path = load_image_from_folder(image_name)
    if not image_path:
        return jsonify({"error": "Image not found"}), 404

    # Return the image file to the client
    return send_file(image_path, mimetype='image/png')



if __name__ == '__main__':
    # Initialize the vector database once at server startup
    initialize_vectordb()
    app.run(debug=True, host='0.0.0.0', port=5000)
