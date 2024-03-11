def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        filename = f.name
        words = count_words(file_contents)
        letter_dict = count_letters(file_contents)
        create_report(filename, words, letter_dict)

def count_words(txt):
    words = txt.split()
    return len(words)

def count_letters(txt):
    letter_dict = {}
    for i in txt:
        i = i.lower()
        if i not in letter_dict:
            letter_dict[i] = 1
        else:
            letter_dict[i] += 1

    return letter_dict


def sort_on(dict):
    return dict['count']

def create_report(filename,word_count, c_dict):
    print(f'--- Begin report of {filename} ---')
    print(f'{word_count} words found in the document')
    list_characters = []
    for x,y in c_dict.items():
        new_dict = {}
        if x.isalpha():
            new_dict['character'] = x
            new_dict['count'] = y
            list_characters.append(new_dict)
    list_characters.sort(reverse=True, key=sort_on)
    for c in list_characters:
        print(f"The '{c["character"]}' character was found {c["count"]} times")

    print("--- End report ---" )


main()

