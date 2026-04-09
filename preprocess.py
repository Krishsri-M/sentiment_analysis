import re
import nltk

nltk.download('stopwords') # Stopwords
nltk.download('wordnet') #lemmatizer dictionary
nltk.download('vader_lexicon') #Vader lexicon dictionary
nltk.download('punkt') #Tokenizer rules
nltk.download('punkt_tab')

from nltk.corpus import stopwords, movie_reviews
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

stop_words = stopwords.words("english")
lemmatizer = WordNetLemmatizer()

def preprocess(text):
    # Convert to lowercase
    text = text.lower()

    # Remove punctuations, numbers
    text = re.sub(r'[^a-z\s]', '', text)

    # Tokenize text
    tokens = word_tokenize(text)

    # Remove stop words 
    tokens = [t for t in tokens if t not in stop_words] # Remove stop words from the tokens

    #Lemmatize_tokens 
    lemmatize_tokens = [lemmatizer.lemmatize(t) for t in tokens] # Lemmatize tokens 

    # Converting back to a string object
    return " ".join(lemmatize_tokens)

print(preprocess("The storytelling was good!!!"))