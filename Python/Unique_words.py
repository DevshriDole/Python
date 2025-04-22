def extract_unique_words(paragraph):
    words = paragraph.split()
    cleaned_words = [word.strip('.,!?;:"\'').lower() for word in words]
    unique_words = set(cleaned_words)
    sorted_words = sorted(unique_words)
    print("\nUnique words in alphabetical order: ")

    for word in sorted_words:
        print(word)

paragraph = """ Python is a powerful. Python is easy to learn.
It is used in web development, data analysis, AI and more."""

extract_unique_words(paragraph)


