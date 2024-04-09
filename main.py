def count_letters(file_contents):
    lower_case_text = file_contents.lower()
    letter_counts = {}
    for letter in lower_case_text:
        if letter.isalpha():
            current_count = letter_counts.get(letter, 0)
            letter_counts[letter] = current_count + 1
    return letter_counts
            


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        word_count = len(words)
        print(f"Word count: {word_count}")

        letter_counts = count_letters(file_contents)
        print ("Letter counts:", letter_counts)

        letter_counts_list = convert_count_to_list(letter_counts)
        letter_counts_list.sort(key=get_count, reverse=True)

        print("--- Begin report ---")
        for item in letter_counts_list:
            print(f"The '{item['letter']}' character was found {item['count']} times")
        print("--- End report ---")



def convert_count_to_list(letter_counts):
    counts_list = []
    for letter, count in letter_counts.items():
        counts_list.append({'letter': letter, 'count': count})
    return counts_list


def get_count(letter_dict):
    return letter_dict['count']
    letter_counts_list = convert_count_to_list(letter_counts)
    letter_counts_list




main()