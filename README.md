# Medical Chatbot

A Flask-based Medical Chatbot that retrieves medical information from local and external sources (MedlinePlus) and provides meaningful responses using GPT-4. The chatbot is designed to categorize, retrieve, and format responses for user queries about medical conditions, treatments, symptoms, and more.

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Setup and Installation](#setup-and-installation)
5. [Usage](#usage)
6. [API Endpoints](#api-endpoints)
7. [Debugging](#debugging)


---

## Project Overview
This chatbot uses a combination of:
1. **ChromaDB**: For storing and retrieving local medical information using embeddings.
2. **MedlinePlus API**: To fetch medical data if no relevant local data is found.
3. **GPT-4**: To generate responses for the user's queries based on retrieved documents.

---

## Features
- Categorizes queries into medical contexts such as symptoms, treatments, causes, etc.
- Fetches data from local storage (ChromaDB) and external sources (MedlinePlus API).
- Prepares a concise and readable context for GPT-4 to generate responses.
- User-friendly web interface for interacting with the chatbot.
- Robust error handling and debugging support.

---

## Technologies Used
- **Backend**: Flask, Flask-CORS
- **Frontend**: HTML, CSS, JavaScript
- **Model**: SentenceTransformers (BioBERT)
- **Database**: ChromaDB
- **External API**: MedlinePlus
- **OpenAI GPT-4**: For generating responses
- **Python Libraries**: `requests`, `uuid`, `xml.etree.ElementTree`

---

## Setup and Installation

### Prerequisites
1. Python 3.9 or higher
2. Node.js (for frontend development, optional)
3. Virtual environment (optional but recommended)

### Steps
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/medical-chatbot.git
    cd medical-chatbot
    ```

2. Create a virtual environment:
    ```bash
    python -m venv medical
    source medical/bin/activate  # On Windows: medical\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up environment variables:
    Create a `.env` file in the root directory and add the following:
    ```
    FLASK_APP=app.py
    FLASK_ENV=development
    OPENAI_API_KEY=your-openai-api-key
    CHROMADB_COLLECTION_NAME=medical_info
    ```

5. Run the Flask app:
    ```bash
    flask run --port=5001
    ```

6. Open the application:
    Access the chatbot at `http://127.0.0.1:5001` in your web browser.

---

## Usage

1. **Web Interface**:
    - Type a medical question in the input field and click "Send".
    - Example: "What are the symptoms of diabetes?"

2. **API Endpoint**:
    - Use the `/query` endpoint to interact programmatically:
      ```bash
      curl -X POST http://127.0.0.1:5001/query \
      -H "Content-Type: application/json" \
      -d '{"query": "What is diabetes?"}'
      ```

## API Endpoints

### `/query` (POST)

- **Description**: Handles user queries and returns answers.
- **Request**:
    ```json
    {
        "query": "What is diabetes?"
    }
    ```
- **Response**:
    ```json
    {
        "answer": "Diabetes is a condition in which your blood glucose levels are too high..."
    }
    ```

---

## Debugging and Troubleshooting

### Common Issues

1. **CORS Errors**:
   - Ensure `Flask-CORS` is installed and initialized in `app.py`.

2. **API Key Errors**:
   - Verify your OpenAI API key in the `.env` file.

3. **Database Issues**:
   - Ensure ChromaDB is initialized and the collection exists.

### Debugging Steps

- Add print statements in key functions (e.g., `handle_query`, `query_handler`) to log intermediate results.
- Use Flask logs for troubleshooting issues.

# Medical Chatbot

A Flask-based Medical Chatbot that retrieves medical information from local and external sources (MedlinePlus) and provides meaningful responses using GPT-4. The chatbot is designed to categorize, retrieve, and format responses for user queries about medical conditions, treatments, symptoms, and more.

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Setup and Installation](#setup-and-installation)
5. [Usage](#usage)
6. [API Endpoints](#api-endpoints)
7. [Debugging and Troubleshooting](#debugging-and-troubleshooting)
8. [Enhancements](#enhancements)

---

## Project Overview
This chatbot uses a combination of:
1. **ChromaDB**: For storing and retrieving local medical information using embeddings.
2. **MedlinePlus API**: To fetch medical data if no relevant local data is found.
3. **GPT-4**: To generate responses for the user's queries based on retrieved documents.

---

## Features
- Categorizes queries into medical contexts such as symptoms, treatments, causes, etc.
- Fetches data from local storage (ChromaDB) and external sources (MedlinePlus API).
- Prepares a concise and readable context for GPT-4 to generate responses.
- Displays references (URLs) for the information provided in the response.
- User-friendly web interface for interacting with the chatbot.
- Robust error handling and debugging support.

---

## Technologies Used
- **Backend**: Flask, Flask-CORS
- **Frontend**: HTML, CSS, JavaScript
- **Model**: SentenceTransformers (BioBERT)
- **Database**: ChromaDB
- **External API**: MedlinePlus
- **OpenAI GPT-4**: For generating responses
- **Python Libraries**: `requests`, `uuid`, `xml.etree.ElementTree`, `dotenv`

---

## Setup and Installation

### Prerequisites
1. Python 3.9 or higher
2. Node.js (for frontend development, optional)
3. Virtual environment (optional but recommended)

### Steps
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/medical-chatbot.git
    cd medical-chatbot
    ```

2. Create a virtual environment:
    ```bash
    python -m venv medical
    source medical/bin/activate  # On Windows: medical\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up environment variables:
    Create a `.env` file in the root directory and add the following:
    ```
    FLASK_APP=app.py
    FLASK_ENV=development
    OPENAI_API_KEY=your-openai-api-key
    CHROMADB_COLLECTION_NAME=medical_info
    ```

5. Run the Flask app:
    ```bash
    flask run --port=5001
    ```

6. Open the application:
    Access the chatbot at `http://127.0.0.1:5001` in your web browser.

---

## Usage

### Web Interface:
1. Type a medical question in the input field and click "Send".
2. Example: "What are the symptoms of diabetes?"
3. The chatbot will display an answer with references (URLs).

### API Endpoint:
- Use the `/query` endpoint to interact programmatically:
    ```bash
    curl -X POST http://127.0.0.1:5001/query \
    -H "Content-Type: application/json" \
    -d '{"query": "What is diabetes?"}'
    ```

---

## API Endpoints

### `/query` (POST)

- **Description**: Handles user queries and returns answers along with references.
- **Request**:
    ```json
    {
        "query": "What is diabetes?"
    }
    ```
- **Response**:
    ```json
    {
        "answer": "Diabetes is a condition in which your blood glucose levels are too high...",
        "references": [
            "https://medlineplus.gov/diabetes.html",
            "https://medlineplus.gov/diabetesmanagement.html"
        ]
    }
    ```

---

## Debugging and Troubleshooting

### Common Issues

1. **CORS Errors**:
   - Ensure `Flask-CORS` is installed and initialized in `app.py`.

2. **API Key Errors**:
   - Verify your OpenAI API key in the `.env` file.

3. **Database Issues**:
   - Ensure ChromaDB is initialized and the collection exists.

4. **Token Limit Errors**:
   - Ensure the number of documents used to generate the response is limited to 3 for GPT-4.

---
# Medical Chatbot

A Flask-based Medical Chatbot that retrieves medical information from local and external sources (MedlinePlus) and provides meaningful responses using GPT-4. The chatbot is designed to categorize, retrieve, and format responses for user queries about medical conditions, treatments, symptoms, and more.

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Setup and Installation](#setup-and-installation)
5. [Usage](#usage)
6. [API Endpoints](#api-endpoints)
7. [Debugging and Troubleshooting](#debugging-and-troubleshooting)
8. [Enhancements](#enhancements)

---

## Project Overview
This chatbot uses a combination of:
1. **ChromaDB**: For storing and retrieving local medical information using embeddings.
2. **MedlinePlus API**: To fetch medical data if no relevant local data is found.
3. **GPT-4**: To generate responses for the user's queries based on retrieved documents.

---

## Features
- Categorizes queries into medical contexts such as symptoms, treatments, causes, etc.
- Fetches data from local storage (ChromaDB) and external sources (MedlinePlus API).
- Prepares a concise and readable context for GPT-4 to generate responses.
- Displays references (URLs) for the information provided in the response.
- User-friendly web interface for interacting with the chatbot.
- Robust error handling and debugging support.

---

## Technologies Used
- **Backend**: Flask, Flask-CORS
- **Frontend**: HTML, CSS, JavaScript
- **Model**: SentenceTransformers (BioBERT)
- **Database**: ChromaDB
- **External API**: MedlinePlus
- **OpenAI GPT-4**: For generating responses
- **Python Libraries**: `requests`, `uuid`, `xml.etree.ElementTree`, `dotenv`

---

## Setup and Installation

### Prerequisites
1. Python 3.9 or higher
2. Node.js (for frontend development, optional)
3. Virtual environment (optional but recommended)

### Steps
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/medical-chatbot.git
    cd medical-chatbot
    ```

2. Create a virtual environment:
    ```bash
    python -m venv medical
    source medical/bin/activate  # On Windows: medical\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up environment variables:
    Create a `.env` file in the root directory and add the following:
    ```
    FLASK_APP=app.py
    FLASK_ENV=development
    OPENAI_API_KEY=your-openai-api-key
    CHROMADB_COLLECTION_NAME=medical_info
    ```

5. Run the Flask app:
    ```bash
    flask run --port=5001
    ```

6. Open the application:
    Access the chatbot at `http://127.0.0.1:5001` in your web browser.

---

## Usage

### Web Interface:
1. Type a medical question in the input field and click "Send".
2. Example: "What are the symptoms of diabetes?"
3. The chatbot will display an answer with references (URLs).

### API Endpoint:
- Use the `/query` endpoint to interact programmatically:
    ```bash
    curl -X POST http://127.0.0.1:5001/query \
    -H "Content-Type: application/json" \
    -d '{"query": "What is diabetes?"}'
    ```

---

## API Endpoints

### `/query` (POST)

- **Description**: Handles user queries and returns answers along with references.
- **Request**:
    ```json
    {
        "query": "What is diabetes?"
    }
    ```
- **Response**:
    ```json
    {
        "answer": "Diabetes is a condition in which your blood glucose levels are too high...",
        "references": [
            "https://medlineplus.gov/diabetes.html",
            "https://medlineplus.gov/diabetesmanagement.html"
        ]
    }
    ```

---

## Debugging and Troubleshooting

### Common Issues

1. **CORS Errors**:
   - Ensure `Flask-CORS` is installed and initialized in `app.py`.

2. **API Key Errors**:
   - Verify your OpenAI API key in the `.env` file.

3. **Database Issues**:
   - Ensure ChromaDB is initialized and the collection exists.

4. **Token Limit Errors**:
   - Ensure the number of documents used to generate the response is limited to 3 for GPT-4.

---

## Enhancements
### Current
- Add chat memory .

