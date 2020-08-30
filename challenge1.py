def read_from_file():
    filename = input("Please Enter File Name: ")
    with open(filename, 'r') as f:
        return [line.strip() for line in f]


def find_largest_word(words):
    return max(words, key=len)


def reverse_string(word):
    return word[::-1]

if __name__ == '__main__':
    list_of_words = read_from_file()
    largest_word = find_largest_word(list_of_words)
    print(largest_word)
    print(reverse_string(largest_word))
