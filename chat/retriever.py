import chromadb
import uuid
from chat.model import model  # Use the model loaded in model.py
from config import CHROMADB_COLLECTION_NAME

# Initialize ChromaDB client and collection
client = chromadb.Client()
collection = client.get_or_create_collection(name=CHROMADB_COLLECTION_NAME)

def generate_embeddings(texts):
    """
    Generate embeddings for a list of texts using the SentenceTransformer model.
    """
    return model.encode(texts, convert_to_numpy=True)

def retrieve_from_chromadb(query):
    """
    Retrieve documents from ChromaDB based on a query.
    """
    print(f"Querying ChromaDB with: {query}")
    query_embedding = model.encode([query])[0]
    results = collection.query(query_embeddings=[query_embedding], n_results=3)

    # Flatten the structure and handle empty results
    documents = results.get("documents", [])
    metadata = results.get("metadatas", [])
    
    # Check if documents and metadata are nested lists
    if isinstance(documents, list) and len(documents) > 0 and isinstance(documents[0], list):
        documents = documents[0]  # Extract the first list
    if isinstance(metadata, list) and len(metadata) > 0 and isinstance(metadata[0], list):
        metadata = metadata[0]  # Extract the first list

    print(f"ChromaDB Results - Documents: {documents}, Metadata: {metadata}")
    return documents, metadata



def store_in_chromadb(data):
    """
    Store the filtered data into the local ChromaDB collection.
    """
    try:
        for item in data:
            if not isinstance(item, dict):
                print(f"Invalid data format: {item}")
                continue

            # Extract required fields
            summary = item.get("summary", "")
            title = item.get("title", "Untitled")
            url = item.get("url", "")

            # Generate embeddings
            embeddings = generate_embeddings([summary])[0]

            # Add to ChromaDB
            doc_id = str(uuid.uuid4())
            collection.add(
                ids=[doc_id],
                documents=[summary],
                metadatas=[{"title": title, "url": url}],
                embeddings=[embeddings]
            )
            print(f"Stored in ChromaDB: {doc_id} - {title}")
    except Exception as e:
        print(f"Error storing data in ChromaDB: {e}")
        raise
