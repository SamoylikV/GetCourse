import requests
from bs4 import BeautifulSoup as bs
import re
from nltk.stem import PorterStemmer


def fetch_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = bs(response.text, 'html.parser')
        return soup
    else:
        return None


def index_words(soup):
    index = {}
    words = re.findall(r'\w+', soup.get_text())
    for word in words:
        word = word.lower()
        if word in index:
            index[word] += 1
        else:
            index[word] = 1
    return index


def remove_stop_words(index):
    stop_words = {'a', 'an', 'the', 'and', 'or', 'in', 'on', 'at'}
    for stop_word in stop_words:
        if stop_word in index:
            del index[stop_word]
    return index


def apply_stemming(index):
    stemmer = PorterStemmer()
    stemmed_index = {}
    for word, count in index.items():
        stemmed_word = stemmer.stem(word)
        if stemmed_word in stemmed_index:
            stemmed_index[stemmed_word] += count
        else:
            stemmed_index[stemmed_word] = count
    return stemmed_index


def search(query, index):
    query_words = re.findall(r'\w+', query.lower())
    result = {}
    for word in query_words:
        if word in index:
            result[word] = index[word]
    return result


def engine(url, query):
    soup = fetch_page(url)
    if soup is None:
        return None
    index = index_words(soup)
    index = remove_stop_words(index)
    index = apply_stemming(index)
    result = search(query, index)
    return result
