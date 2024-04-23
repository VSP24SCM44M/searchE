import os
import pickle
import json
from text_handler import vectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from flask import Flask, jsonify, request, abort

with open('scikit.pkl', 'rb') as f:
    docs_vector = pickle.load(f)

# Flask application
app = Flask(__name__)

@app.route('/search-scikit', methods=['POST'])
def handle_scikit_search():
    data = request.json
    query = data['query']
    if not query:
        abort(400, 'Please add query')

    query_vector = vectorizer.transform([query])
    cosine_similarities = cosine_similarity(query_vector, docs_vector).flatten()
    k = min(5, len(cosine_similarities))
    results = cosine_similarities.argsort()[-k:][::-1]
    output = []
    for i in results:
        with open(f"../bootstrap-{i+1}.json", 'r') as f:
            data = json.load(f)
            obj = {
                'title': data['title'],
                'url': data['url'],
                'cosine_similarity': cosine_similarities[i]
            }
            output.append(obj)

    # Return a response
    return jsonify(output), 200

if __name__ == '__main__':
    app.run(debug=True)
