# Configuration settings for the application
CHROMADB_COLLECTION_NAME = "medical_info"
SENTENCE_TRANSFORMER_MODEL = "pritamdeka/S-BioBert-snli-multinli-stsb"
MEDLINEPLUS_URL = "https://wsearch.nlm.nih.gov/ws/query"
CATEGORY_KEYWORDS = {
    "treatments": ["treat", "cure", "remedy", "therapy", "medication", "heal", "manage"],
    "symptoms": ["symptom", "sign", "indicator"],
    "causes": ["cause", "reason", "why"],
    "definition": ["what is", "define", "meaning"],
    "prevention": ["prevent", "avoid", "reduce", "stop"],
}
