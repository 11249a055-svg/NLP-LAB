from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')
nltk.download('stopwords')
example_text = "Hello Mr.Smith, How are you doing today?"
stop_words = set(stopwords.words("english"))
words = word_tokenize(example_text)
filtered_sentence = []
for w in words:
    if w.lower() not in stop_words:
        filtered_sentence.append(w)
print(filtered_sentence)
