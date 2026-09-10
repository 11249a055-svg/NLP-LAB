import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

# Download required resources
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('wordnet')
nltk.download('omw-1.4')

# Get input
text = input("Enter a sentence: ")

# Tokenization
words = word_tokenize(text)

# Create stemmer and lemmatizer objects
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

# Display results
print("\nMorphological Analysis")
print("-" * 60)
print("{:<15} {:<15} {:<15}".format(
    "Original", "Stemmed", "Lemmatized"
))
print("-" * 60)

# Perform stemming and lemmatization
for word in words:
    stem = stemmer.stem(word)
    lemma = lemmatizer.lemmatize(word)

    print("{:<15} {:<15} {:<15}".format(
        word, stem, lemma
    ))