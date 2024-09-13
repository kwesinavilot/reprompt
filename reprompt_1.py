import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re

class PromptEngineer:
    def __init__(self):
        nltk.download('punkt')
        nltk.download('stopwords')
        nltk.download('wordnet')
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()

    def preprocess(self, text):
        # Lowercase and remove punctuation
        text = re.sub(r'[^\w\s]', '', text.lower())
        
        # Tokenize
        tokens = word_tokenize(text)
        
        # Remove stop words and lemmatize
        tokens = [self.lemmatizer.lemmatize(token) for token in tokens if token not in self.stop_words]
        
        return tokens

    def identify_key_concepts(self, tokens):
        # This is where you'd implement logic to identify important concepts
        # For now, we'll just return the most frequent words
        from collections import Counter
        return [word for word, count in Counter(tokens).most_common(5)]

    def determine_intent(self, tokens):
        # Implement logic to determine the user's intent
        # This could involve looking for specific keywords or patterns
        intent = "unknown"
        if "how" in tokens:
            intent = "instruction"
        elif "what" in tokens:
            intent = "definition"
        elif "why" in tokens:
            intent = "explanation"
        return intent

    def generate_improved_prompt(self, original_prompt):
        tokens = self.preprocess(original_prompt)
        key_concepts = self.identify_key_concepts(tokens)
        intent = self.determine_intent(tokens)
        
        # Construct improved prompt based on intent and key concepts
        if intent == "instruction":
            improved_prompt = f"Provide step-by-step instructions on how to {' '.join(key_concepts)}"
        elif intent == "definition":
            improved_prompt = f"Define and explain the concept of {' '.join(key_concepts)}"
        elif intent == "explanation":
            improved_prompt = f"Explain in detail why {' '.join(key_concepts)} occurs or is important"
        else:
            improved_prompt = f"Provide comprehensive information about {' '.join(key_concepts)}"
        
        return improved_prompt