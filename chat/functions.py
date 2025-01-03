import re


def remove_html_tags(text):
    """
    Remove HTML tags from the given text.
    """
    if not isinstance(text, str):
        return text  # If text is not a string, return it as-is
    clean_text = re.sub(r"<[^>]*>", "", text)  # Remove HTML tags
    return clean_text.strip()

def format_context(documents):
    """
    Format the context string from retrieved documents for GPT-4 or other processing.
    """
    context = ""
    for doc in documents:
        title = doc.get("metadata", {}).get("title", "Unknown Title")
        url = doc.get("metadata", {}).get("url", "Unknown URL")
        text = doc.get("text", "No content available")
        context += f"Title: {title}\nURL: {url}\nSummary: {text}\n\n"
    return context

def categorize_query(query):
    """
    Categorize the query based on predefined keywords.
    """
    categories = {
    "treatments": ["treat", "cure", "remedy", "therapy", "medication", "heal", "manage"],
    "symptoms": ["symptom", "sign", "indicator"],
    "causes": ["cause", "reason", "why"],
    "definition": ["what is", "define", "meaning"],
    "prevention": ["prevent", "avoid", "reduce", "stop"],
}

    for category, keywords in categories.items():
        if any(keyword in query.lower() for keyword in keywords):
            return category
    return 'general'

def filter_by_category(data, category_keywords):
    print(f"Filtering data with keywords: {category_keywords}")
    filtered_data = []

    for item in data:
        title = remove_html_tags(item.get("title", ""))
        summary = remove_html_tags(item.get("summary", ""))

        # Check if any keywords match the title or summary
        if any(keyword.lower() in title.lower() for keyword in category_keywords) or \
           any(keyword.lower() in summary.lower() for keyword in category_keywords):
            filtered_data.append(item)

    print(f"Filtered Data: {filtered_data}")
    return filtered_data

def prepare_response(query, documents):
    """
    Prepare a response based on the query and retrieved documents.
    """
    print(f"Preparing response for query: {query}")
    print(f"Documents passed to response preparation: {documents}")

    if not documents or not isinstance(documents, list):
        return "Sorry, I couldn't find any relevant information."

    context = f"Based on the information retrieved, here is what I found about '{query}':\n\n"
    for doc in documents:
        title = doc.get("metadata", {}).get("title", "Unknown Title")
        url = doc.get("metadata", {}).get("url", "Unknown URL")
        text = doc.get("text", "No content available")
        context += f"Title: {title}\nURL: {url}\nSummary: {text}\n\n"

    print(f"Prepared Context for GPT-4: {context}")
    return context




