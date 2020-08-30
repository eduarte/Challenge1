def read_from_file():

    filename = input("Please Enter File Name: ")
    with open(filename, 'r') as f:
        try:
            return [line.strip() for line in f]
        except IOError:
            print("Something went wrong when reading to the file")


def find_largest_word(words):
    try:
        return max(words, key=len)
    except (ValueError, TypeError):
        return "Ops! Something went wrong, please try again with a valid file!"


def reverse_string(word):
    try:
        return word[::-1]
    except (ValueError, TypeError):
        return "Ops! Something went wrong, please try again with a valid word!"


if __name__ == '__main__':
    list_of_words = read_from_file()
    largest_word = find_largest_word(list_of_words)
    print(largest_word)
    print(reverse_string(largest_word))
