import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk import pos_tag, ne_chunk, ngrams
from nltk.probability import FreqDist
from collections import Counter
import string

# Download required resources
nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("averaged_perceptron_tagger")
nltk.download("maxent_ne_chunker")
nltk.download("words")
nltk.download("maxent_ne_chunker_tab")

class TextAnalyzer:
    """
    A class for performing NLP analysis on text files.
    Includes tokenization, stemming, lemmatization,
    named entity recognition, and n-gram analysis.
    """

    def __init__(self, file_path):
        self.file_path = file_path
        self.raw_text = self.load_text()
        self.tokens = []
        self.filtered_tokens = []
        self.stemmed_tokens = []
        self.lemmatized_tokens = []

    def load_text(self):
        """Load text file content."""
        with open(self.file_path, "r", encoding="utf-8") as file:
            return file.read()

    def preprocess_text(self):
        """Tokenize, lowercase, remove punctuation and stopwords."""
        stop_words = set(stopwords.words("english"))

        self.tokens = word_tokenize(self.raw_text.lower())

        self.filtered_tokens = [
            token for token in self.tokens
            if token not in string.punctuation and token not in stop_words
        ]

    def stem_tokens(self):
        """Apply stemming."""
        stemmer = PorterStemmer()
        self.stemmed_tokens = [stemmer.stem(token) for token in self.filtered_tokens]

    def lemmatize_tokens(self):
        """Apply lemmatization."""
        lemmatizer = WordNetLemmatizer()
        self.lemmatized_tokens = [
            lemmatizer.lemmatize(token) for token in self.filtered_tokens
        ]

    def most_common_tokens(self, token_type="filtered", n=20):
        """Return top N most common tokens."""
        token_map = {
            "filtered": self.filtered_tokens,
            "stemmed": self.stemmed_tokens,
            "lemmatized": self.lemmatized_tokens
        }

        fd = FreqDist(token_map[token_type])
        return fd.most_common(n)

    def named_entities_count(self):
        """Count named entities in the text."""
        tagged = pos_tag(word_tokenize(self.raw_text))
        chunked = ne_chunk(tagged)

        count = 0
        for chunk in chunked:
            if hasattr(chunk, "label"):
                count += 1

        return count

    def trigram_analysis(self, n=20):
        """Return most common trigrams."""
        trigrams = list(ngrams(self.filtered_tokens, 3))
        freq = Counter(trigrams)
        return freq.most_common(n)