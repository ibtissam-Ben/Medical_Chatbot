from flask import Flask, request, jsonify, render_template
from flask_cors import CORS 
from chat.query_handler import handle_query
from dotenv import load_dotenv
import os
import openai
from config import CATEGORY_KEYWORDS

# Initialize Flask app
app = Flask(__name__, static_folder="static", template_folder="templates")
CORS(app)  # Allow CORS for cross-origin requests

# Load environment variables from the .env file
load_dotenv()

# Retrieve the OpenAI API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

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

        # Pass the query to the handle_query function and get the prepared context
        context , urls= handle_query(query)
        print("Prepared Context from handle_query:", context)

        # Generate GPT-4 response
        answer = generate_gpt4_response(query, context)
        return jsonify({"answer": answer, "urls": urls}), 200

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
