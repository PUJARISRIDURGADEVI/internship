
import ollama

text = "This is a sentence with multiple entities: John (PERSON), London (LOCATION)"
entities = ollama.extract_entities(text)
print(entities)