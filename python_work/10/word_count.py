def count_words(filename):
    """Count the approximate number of words in a file."""
    try: with open(filename, encoding='utf-8') as f:
        contents = f.read()