with open('/Users/shiranavni/workspace/github.com/shiranavni/bookbot/books/Frankenstein.txt', 'r') as book_file:
    text = book_file.read()


def count_words (text):
    words = text.split()
    return len(words)



def count_letters (text): 
    letter_count = {}
    lowered_string = text.lower()
    for i in lowered_string: 
        if i.isalpha():
            letter_count[i] = letter_count.get(i, 0) + 1
    return letter_count 


def sort_on (letter_count):
    return letter_count["count"]

def generate_result(letter_count):
    character_list = []
    character_list = [{"letter": letter, "count": count} for letter, count in letter_count.items()]
    character_list.sort(reverse = True, key=sort_on)
    print("--- Begin report ---")
    for character in character_list:
        print(f"The '{character['letter']}' character was found {character['count']} times")
    print("--- End report ---")
    
word_count = count_words(text)
print("This book contains", word_count, "words" )

letter_count = count_letters(text)
generate_result(letter_count)




