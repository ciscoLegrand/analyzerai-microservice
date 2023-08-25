import stopwordsiso as stopwords

def stop_words_loader():
    stop_words_es = set(stopwords.stopwords("es"))
    stop_words_ca = set(stopwords.stopwords("ca"))
    stop_words_en = set(stopwords.stopwords("en"))
    stop_words_eu = set(stopwords.stopwords("eu"))
    stop_words_fr = set(stopwords.stopwords("fr"))
    stop_words_pt = set(stopwords.stopwords("pt"))

    stop_words = set.union(*(stop_words_es, stop_words_ca, stop_words_en, stop_words_eu, stop_words_fr, stop_words_pt))
    
    stop_words.discard("trabajo")
    stop_words.update(['q', 'si', 'none'])
    
    return stop_words
