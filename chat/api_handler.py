from chat.retriever import retrieve_from_chromadb, store_in_chromadb
from chat.functions import categorize_query, filter_by_category, prepare_response
from chat.medlineplus import get_medical_info_from_medlineplus
from config import CATEGORY_KEYWORDS

def handle_query(query):
    """
    Handles the user query by retrieving information from the database or an external source.
    """
    try:
        print(f"Processing query: {query}")

        # Categorize the query
        category = categorize_query(query)
        print(f"Query categorized as: {category}")

        # Retrieve documents from the local database
        documents = retrieve_from_chromadb(query)
        print(f"Retrieved documents from ChromaDB: {documents}")

        # Validate documents and metadata structure
        if not documents or not isinstance(documents, list) or not all(isinstance(doc, str) for doc in documents):
            print("Invalid documents structure from ChromaDB. Fetching from MedlinePlus...")
            documents = []

            print("No local documents found. Fetching from MedlinePlus...")
            category, medlineplus_data = get_medical_info_from_medlineplus(query)
            print(f"Retrieved data from MedlinePlus: {medlineplus_data}")
            # Add the debugging statement here
            print("Parsed MedlinePlus Data:", medlineplus_data)

            # Filter the data based on the query category
            filtered_data = filter_by_category(medlineplus_data, CATEGORY_KEYWORDS.get(category, []))
            print(f"Filtered data: {filtered_data}")

            # Store the filtered data into the local database
            if filtered_data:
                store_in_chromadb(filtered_data)
                print("Filtered data stored in ChromaDB.")

            # Use the filtered data as documents
            documents = [
                {
                    "text": doc.get("summary", ""),
                    "metadata": {
                        "title": doc.get("title", ""),
                        "url": doc.get("url", ""),
                    },
                }
                for doc in filtered_data
            ]
            print(f"Documents prepared for response: {documents}")

        # Prepare the response
        response = prepare_response(query, documents)
        print(f"Prepared response: {response}")
        return response

    except Exception as e:
        print(f"Error handling query: {e}")
        raise
