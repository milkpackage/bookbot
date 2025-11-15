def find_num_of_words(text):
    splited_text = text.split()
    #print(splited_text)
    return len(splited_text)
    
def character_count(text):
    dict_of_chars = {}
    text = text.lower()
    for symbols in text:
        dict_of_chars[symbols]=dict_of_chars.setdefault(symbols, 0)+1
    return dict_of_chars


def sort_helper(items):
    return items["num"]
    
    
def sorting_data(dict_of_chars):
    dict_of_chars = character_count(dict_of_chars)
    listed = []
    for char, num in dict_of_chars.items():
        listed = [{"char": ch, "num": n} for ch, n in dict_of_chars.items() if ch.isalpha()]
        listed.sort(reverse=True, key=sort_helper)
        return listed