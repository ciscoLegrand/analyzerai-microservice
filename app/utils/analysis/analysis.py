import re
from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer
from app.utils.analysis.stop_words import stop_words_loader

def process_answers(answers):
    texts = [answer['custom_field'] for answer in answers if 'custom_field' in answer]
    vectorizer = CountVectorizer(stop_words=stop_words_loader(), max_features=100)
    X = vectorizer.fit_transform(texts)
    terms = vectorizer.get_feature_names_out()
    frequencies = X.toarray().sum(axis=0)
    most_common = Counter(dict(zip(terms, frequencies))).most_common(10)
    return {'most_repeated_words': most_common}