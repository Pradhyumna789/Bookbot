def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        
    print("--- Begin report of books/frankenstein.txt ---\n")
    no_words = word_count(file_contents)
    print(f"{no_words} words found in the document\n")
    
    char_freq(file_contents)

    print("--- End Report ---\n")

    return "Report Completed"

def word_count(file_contents):
    file_string = file_contents.split()
    words = len(file_string)
    return words

def sort_on(char_list):
    return char_list["num"]

def char_freq(file_contents):
    file_string = file_contents
    char_freq = {}
    for string in file_string:
        lowered_string = string.lower()
        for char in lowered_string:
            if(char.isalpha()):
                if(char not in char_freq):
                    char_freq[char] = 1
                else:
                    char_freq[char] += 1

    char_list = []
    for char, count in char_freq.items():
        char_list.append({"name": char, "num": count})

    char_list.sort(reverse=True, key=sort_on) 

    for dict in char_list:
        print(f"The {dict['name']} character was found {dict['num']} times\n")

main()
