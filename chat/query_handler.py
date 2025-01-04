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

        # Validate documents and metadata structure
        if not documents or not isinstance(documents, list) or not all(isinstance(doc, str) for doc in documents):
            print("Invalid documents structure from ChromaDB. Fetching from MedlinePlus...")
            documents = []

            print("No local documents found. Fetching from MedlinePlus...")
            category, medlineplus_data = get_medical_info_from_medlineplus(query)
            print(f"Retrieved data from MedlinePlus: {medlineplus_data}")
            # Retrieve keywords for the category
            print(category)
            if category in CATEGORY_KEYWORDS:
                category_keywords = CATEGORY_KEYWORDS[category]
            else:
                category_keywords = []
                print(f"Warning: No keywords found for category '{category}'. Using empty keyword list.")


            # Filter the data based on the query category
            filtered_data = filter_by_category(medlineplus_data,category_keywords)
            
            # Store the filtered data into the local database
            if filtered_data:
            # Validate filtered_data structure
                for entry in filtered_data:
                    if not isinstance(entry, dict):
                        print(f"Invalid entry in filtered_data: {entry}")
                    elif "summary" not in entry or "title" not in entry or "url" not in entry:
                        print(f"Missing keys in entry: {entry}")
                    else:
                        print(f"Valid entry: {entry}")
            
            # Store the filtered data into the local database
            if filtered_data:
                store_in_chromadb(filtered_data)
                print("***************************Filtered data stored in ChromaDB.")

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
        # Limit to the top 3 documents
        top_documents = documents[:3]
        print(f"Top documents: {top_documents}")

        # Prepare context
        context = prepare_response(query, top_documents)
        print(f"Prepared Context: {context}")

        # Extract URLs separately
        urls = [doc["metadata"]["url"] for doc in top_documents if "metadata" in doc and "url" in doc["metadata"]]
        print(f"Extracted URLs: {urls}")

        return context, urls

    except Exception as e:
        print(f"Error handling query: {e}")
        raise
