from flask import Flask, request, jsonify, render_template
from flask_cors import CORS 
from chat.api_handler import handle_query
from chat.functions import prepare_response
from chat.model import model  # Ensure the SentenceTransformer model is loaded
import openai
from config import CATEGORY_KEYWORDS

# Initialize Flask app
app = Flask(__name__, static_folder="static", template_folder="templates")
CORS(app)  # Allow CORS for cross-origin requests

# Set OpenAI API key (ensure it's stored in your environment variables or .env file)
openai.api_key = "your_openai_api_key"

def generate_gpt4_response(question, context):
    print(f"Generating GPT-4 response with context:\n{context}")
    prompt = f"Answer the following question based on the provided context:\n\nContext:\n{context}\n\nQuestion: {question}\nAnswer:"

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500,
            temperature=0.7,
        )
        gpt_answer = response['choices'][0]['message']['content'].strip()
        print(f"GPT-4 Response: {gpt_answer}")
        return gpt_answer

    except Exception as e:
        print(f"Error generating GPT-4 response: {e}")
        return "Sorry, I couldn't generate a response at the moment."

"""
@app.route("/query", methods=["POST"])
def query_handler():
    data = request.get_json()  # Extract JSON data
    print("Received data:", data)  # Debugging: Print received JSON

    if not data or "query" not in data:
        return jsonify({"error": "Missing 'query' parameter in request body"}), 400

    query = data["query"]  # Extract 'query'
    print("Extracted query:", query)  # Debugging: Print extracted query


    try:
        # Step 1: Retrieve documents from ChromaDB
        documents, metadata = retrieve_from_chromadb(query)

        # Debug: Print the retrieved documents and metadata
        print("Retrieved Documents from ChromaDB:", documents)
        print("Retrieved Metadata from ChromaDB:", metadata)

        # Step 2: If no documents, fetch from MedlinePlus
        if not documents:
            category, medlineplus_data = get_medical_info_from_medlineplus(query)
            print("Retrieved Data from MedlinePlus:", medlineplus_data)

            if medlineplus_data:
                # Store MedlinePlus data in ChromaDB
                store_in_chromadb(medlineplus_data)
                documents = [{"text": item["summary"], "metadata": {"title": item["title"], "url": item["url"]}} for item in medlineplus_data]
                print("Formatted Documents from MedlinePlus:", documents)
            else:
                return jsonify({"message": "No relevant information found in ChromaDB or MedlinePlus."}), 404

        # Debug: Print documents before preparing context
        print("Documents before Context Preparation:", documents)

        # Step 3: Prepare context
        context = prepare_response(query, documents)
        print("Prepared Context for GPT-4:", context)

        # Step 4: Generate GPT-4 response
        answer = generate_gpt4_response(query, context)
        return jsonify({"answer": answer}), 200

    except Exception as e:
        print("Error:", e)  # Print the exact error for debugging
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500
"""
@app.route("/query", methods=["POST"])
def query_handler():
    """
    Flask route for handling user queries.
    """
    try:
        # Extract the query from the request body
        data = request.get_json()
        if not data or "query" not in data:
            return jsonify({"error": "Missing 'query' parameter in request body"}), 400

        query = data["query"]
        print(f"Received query: {query}")

        # Retrieve documents and prepare context
        documents = handle_query(query)
        print("Documents retrieved for query:", documents)

        # Prepare context
        context = prepare_response(query, documents)
        print("Prepared Context:", context)

        # Generate GPT-4 response
        answer = generate_gpt4_response(query, context)
        print("GPT-4 Answer:", answer)

        return jsonify({"answer": answer}), 200

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

@app.route("/")
def home():
    """
    Serve the chatbot interface.
    """
    return render_template("chatbot.html")  

if __name__ == "__main__":
    app.run(debug=True, port=5001)
