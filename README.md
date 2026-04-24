NLP Comparative Analysis Project
Overview

This project performs a comparative Natural Language Processing (NLP) analysis on four text files using Python and the NLTK library. The main objective is to process unstructured text data, extract meaningful insights, and compare writing patterns across documents.

The first three text files are analyzed to determine their subject matter and stylistic similarities, while the fourth text is evaluated using trigram analysis to investigate whether it may have been written by the same author.

This project demonstrates practical applications of NLP concepts such as tokenization, stop word removal, stemming, lemmatization, named entity recognition, and n-gram analysis.

Objectives
Apply NLP pre-processing techniques to raw text
Compare the first three documents by subject and writing style
Use trigram patterns to evaluate authorship of the fourth text
Identify the most common words and entities in each file
Demonstrate the role of NLP in analyzing unstructured data
Features
Tokenization of sentences and words
Stop word removal for cleaner analysis
Stemming using Porter Stemmer
Lemmatization using WordNet Lemmatizer
Named Entity Recognition (NER) for identifying people, places, and organizations
Trigram generation for stylistic comparison
Frequency analysis of the top 20 most common tokens
Project Structure
nlp-comparative-analysis/
│
├── main.py               # Main script to run analysis
├── analyzer.py           # TextAnalyzer class implementation
├── Text_1.txt            # Input file 1
├── Text_2.txt            # Input file 2
├── Text_3.txt            # Input file 3
├── Text_4.txt            # Input file 4
├── requirements.txt      # Required Python packages
└── README.md             # Project documentation
Installation

Clone the repository and install dependencies:

git clone <your-repository-url>
cd nlp-comparative-analysis
pip install -r requirements.txt
Required NLTK Downloads

Before running the project, make sure the following NLTK resources are installed:

import nltk

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
How to Run

Run the main script:

python main.py

The program will automatically analyze all four text files located in the project folder.

How It Works
1. Text Loading

Each text file is read and stored for analysis.

2. Pre-processing

The text is cleaned through:

Lowercasing
Tokenization
Removing punctuation
Removing stop words
3. Word Normalization

Two approaches are applied:

Stemming → reduces words to root forms
Lemmatization → converts words to dictionary-valid forms
4. Frequency Analysis

The top 20 most frequent words are extracted.

5. Named Entity Recognition

Entities such as names, locations, and organizations are identified.

6. Trigram Analysis

Three-word combinations are generated to detect writing style patterns.

Example Findings
Text_1, Text_2, and Text_3 showed strong overlap in vocabulary and themes, indicating they revolve around the same literary subject.
Frequent words such as Romeo, Juliet, love, and Verona suggested a connection to Romeo and Juliet.
Text_4 differed in trigram structure and entity distribution, suggesting a distinct narrative style.
Key NLP Concepts Demonstrated
Concept	Purpose
Tokenization	Splits text into words/sentences
Stop Words	Removes common filler words
Stemming	Reduces words to root form
Lemmatization	Produces dictionary base forms
NER	Detects meaningful entities
N-grams	Captures word sequence patterns
Limitations
NER may not always correctly classify fictional names.
Trigram similarity suggests style but does not guarantee authorship.
Results depend on text quality and formatting.
Conclusion

This project highlights how NLP can be used to process and analyze unstructured text data. By combining pre-processing, linguistic normalization, entity recognition, and trigram modeling, meaningful insights about subject matter and writing style can be extracted efficiently.

AI Usage Disclosure

AI tools were used for assistance with debugging, documentation drafting, and improving code clarity. All implementation decisions, testing, and final submissions were reviewed and validated independently.