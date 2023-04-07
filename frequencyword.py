'''write a program that accepts a string and displays a string which contains the word with the largest frequency in the text and the frequency itself separated by space.
rules:
The word would have the largest frequency.
In case multiple word have the same frequency, then choose the word that has maximum length.
Assumptions:
The text has no special characters other than space.
The text would begin with a word and there will be a only space between the word.
perform case insensitive string comparision'''

def find_most_frequent_word(text):
    # Convert the text to lowercase and split into words
    words = text.lower().split()

    # Count the frequency of each word
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    # Find the word with the maximum frequency
    max_frequency = 0
    max_word = ''
    for word, freq in frequency.items():
        if freq > max_frequency:
            max_frequency = freq
            max_word = word
        elif freq == max_frequency:
            if len(word) > len(max_word):
                max_word = word

    # Return the word with its frequency
    return max_word + ' ' + str(max_frequency)

text = ('Betty bought a bit of butter but the bit of butter was a little bitter so Betty bought a bit of better butter to make the bitter butter better.')
print(find_most_frequent_word(text))

 

