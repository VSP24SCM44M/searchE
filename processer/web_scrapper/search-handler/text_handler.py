import json
import string
import nltk
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

documents = []

def tokenize_document(document):
    translator = str.maketrans('', '', string.punctuation)
    tokens = []
    for token in document.split():
        tokens.append(token)
    return tokens

# Read the crawled pages
for a in range(1, 150):
    with open(f"../bootstrap-{a}.json", 'r') as f:
        data = json.load(f)
        tokens = tokenize_document(data['content'])
        documents.append(" ".join(tokens))

# scikit
vectorizer = TfidfVectorizer(stop_words='english')
index = vectorizer.fit_transform(documents)
with open('scikit.pkl', 'w') as f:
    pickle.dump(index, f)
