import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re
from collections import Counter
import xml.etree.ElementTree as ET

class Reprompt:
    def __init__(self):
        nltk.download('punkt')
        nltk.download('stopwords')
        nltk.download('wordnet')
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()

    def preprocess(self, text):
        # Capitalize and fix basic grammar
        text = '. '.join(sent.capitalize() for sent in sent_tokenize(text))
        
        # Tokenize
        tokens = word_tokenize(text)
        
        # Remove stop words and lemmatize
        tokens = [self.lemmatizer.lemmatize(token.lower()) for token in tokens if token.lower() not in self.stop_words]
        
        return tokens

    def identify_key_concepts(self, tokens):
        return [word for word, count in Counter(tokens).most_common(5)]

    def determine_intent(self, tokens):
        intent_keywords = {
            "instruction": ["how", "steps", "guide"],
            "definition": ["what", "define", "explain"],
            "explanation": ["why", "reason", "cause"],
            "comparison": ["compare", "contrast", "versus"],
            "analysis": ["analyze", "examine", "investigate"],
            "summary": ["summarize", "brief", "overview"]
        }
        
        for intent, keywords in intent_keywords.items():
            if any(keyword in tokens for keyword in keywords):
                return intent
        return "general"

    def improve(self, original_prompt):
        tokens = self.preprocess(original_prompt)
        key_concepts = self.identify_key_concepts(tokens)
        intent = self.determine_intent(tokens)
        
        # Construct XML structure
        root = ET.Element("prompt")
        
        # Add context
        context = ET.SubElement(root, "context")
        context.text = f"The user is seeking information about {', '.join(key_concepts)}."
        
        # Add instruction
        instruction = ET.SubElement(root, "instruction")
        if intent == "instruction":
            instruction.text = f"Provide step-by-step instructions on how to {' '.join(key_concepts)}. Limit the response to 5 steps."
        elif intent == "definition":
            instruction.text = f"Define and explain the concept of {' '.join(key_concepts)} in 2-3 sentences."
        elif intent == "explanation":
            instruction.text = f"Explain in detail why {' '.join(key_concepts)} occurs or is important. Use a 'lightweight chain of thought' approach by first stating your reasoning process, then providing the explanation."
        elif intent == "comparison":
            instruction.text = f"Compare and contrast {' and '.join(key_concepts[:2])} in a brief paragraph."
        elif intent == "analysis":
            instruction.text = f"Analyze {' '.join(key_concepts)} by considering its causes, effects, and implications. Structure your response with clear subheadings."
        elif intent == "summary":
            instruction.text = f"Provide a concise summary of {' '.join(key_concepts)} in 3-4 bullet points."
        else:
            instruction.text = f"Provide comprehensive information about {' '.join(key_concepts)}. Structure your response with an introduction, main points, and a conclusion."
        
        # Add output format
        output_format = ET.SubElement(root, "output_format")
        output_format.text = "Please structure your response using appropriate headings and subheadings. Use bullet points where applicable for clarity."
        
        # Convert to string
        improved_prompt = ET.tostring(root, encoding="unicode")
        
        return improved_prompt