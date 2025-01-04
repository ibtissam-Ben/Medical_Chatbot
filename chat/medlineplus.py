import requests
import xml.etree.ElementTree as ET
from chat.functions import categorize_query, remove_html_tags

def get_medical_info_from_medlineplus(query):
    """
    Fetches medical information from the MedlinePlus API based on the given query.

    Args:
        query (str): The user's query.

    Returns:
        tuple: A category string and a list of results containing title, URL, and summary.
    """
    url = "https://wsearch.nlm.nih.gov/ws/query"
    params = {
        "db": "healthTopics",  # Database for health topics
        "term": query,         # Search term
    }

    try:
        # Make a GET request to the MedlinePlus API
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)

        # Parse the XML response
        root = ET.fromstring(response.text)

        # Extract relevant data
        results = []
        for document in root.findall(".//document"):
            try:
            # Extract title
                title_elem = document.find(".//content[@name='title']")
                title = "Unknown Title"  # Default title
                if title_elem is not None:
                    if hasattr(title_elem, 'text') and title_elem.text:  # Check if text exists
                        title = remove_html_tags(title_elem.text)
                    else:
                        print("Invalid Title Element:", title_elem)

                # Extract summary
                summary_elem = document.find(".//content[@name='FullSummary']")
                summary = "No summary available."  # Default summary
                if summary_elem is not None:
                    if hasattr(summary_elem, 'text') and summary_elem.text:  # Check if text exists
                        summary = remove_html_tags(summary_elem.text)
                    else:
                        print("Invalid Summary Element:", summary_elem)


                # Extract URL
                url = document.attrib.get("url", "N/A")

                # Debugging: Print extracted values
                print("Parsed Title:", title)
                print("Parsed Summary:", summary)
                print("Parsed URL:", url)

                results.append({
                    "title": title,
                    "url": url,
                    "summary": summary
                })
                
            except Exception as e:
                print("Error processing document:")
                print(ET.tostring(document, encoding='unicode'))  # Print the raw document
                print(f"Error: {e}")
                
        # Categorize the query
        category = categorize_query(query)
        print(f"Query categorized as: {category}")
        return category, results

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return None, []

    except ET.ParseError as e:
        print(f"Failed to parse XML. Error: {e}")
        return None, []