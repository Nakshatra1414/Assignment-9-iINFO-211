import os
from analyzer import TextAnalyzer


def analyze_text(file_name):
    print(f"\n--- Analysis for {file_name} ---")

    analyzer = TextAnalyzer(file_name)

    analyzer.preprocess_text()
    analyzer.stem_tokens()
    analyzer.lemmatize_tokens()

    print("\nTop 20 Filtered Tokens:")
    print(analyzer.most_common_tokens("filtered"))

    print("\nTop 20 Stemmed Tokens:")
    print(analyzer.most_common_tokens("stemmed"))

    print("\nTop 20 Lemmatized Tokens:")
    print(analyzer.most_common_tokens("lemmatized"))

    print("\nNamed Entities Count:")
    print(analyzer.named_entities_count())

    print("\nTop 20 Trigrams:")
    print(analyzer.trigram_analysis())


if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))

    files = [
        os.path.join(base_dir, "Text_1.txt"),
        os.path.join(base_dir, "Text_2.txt"),
        os.path.join(base_dir, "Text_3.txt"),
        os.path.join(base_dir, "Text_4.txt"),
    ]

    for file in files:
        analyze_text(file)