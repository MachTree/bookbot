def get_word_count(book_text):
    words = book_text.split()
    return len(words)

def get_character_count(book_text):
    chars = {}
    for char in book_text:
        char = char.lower()
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

def sort_characters(character_count):
    sorted = []
    for key, value in character_count.items():
        sorted.append({"char": key, "num": value})
    
    def sort_on(items):
        return items["num"]
    
    sorted.sort(reverse=True, key=sort_on)
    return sorted