import nltk

def download_nltk_data():
    try:
        nltk.download('punkt')
        nltk.download('stopwords')
    except:
        print("Error al descargar los paquetes de NLTK. Asegúrate de tener conexión a internet.")
