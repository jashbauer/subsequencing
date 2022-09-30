#--------------- SUBSEQUENCE FILTER CHALLENGE ---------------------------------
# Selects the longest word in an array that is also a subsequence of a
# supplied string.

# --------------- HELPER FUNCTIONS --------------------------------------------
def longer_subseq_filter(array):
    longest_word = array[0]
    for word in array:
        if len(longest_word) < len(word):
            longest_word = word
    return longest_word


def sequence_to_dict(sequence):
    sequence_dict = {}
    for letter in sequence:
        sequence_dict[letter] = []

    i = 0
    for letter in sequence:
        if letter == sequence[i]:
            sequence_dict[letter].append(i)
            i += 1

    return sequence_dict


def order_checker(array, min_index):
    for index in array:
        if index >= min_index:
            return index + 1
    else:
        return False


def char_checker(word, dict):
    min_index = 0
    for letter in word:
        if letter in dict:
            min_index = order_checker(dict[letter], min_index)
            if not min_index:
                return False
        else:
            return False
    return True


# -------------------- THE CODE IN ACTION ---------------------------------

sequence = "helplove"

words = ["hllove", "hello", "hell", "lplo", "helovpe", "banana", "car", "hpv", "evolpleh",
         "heuhauhalove", "plohelp", "epove"]

words2 = ["evolpleh"]


def subsequencer(seq, array):

    sequence_as_dict = sequence_to_dict(seq)

    subs = []
    for word in array:
        if char_checker(word=word, dict=sequence_as_dict):
            subs.append(word)

    print(subs)
    return longer_subseq_filter(subs)


print(subsequencer(seq=sequence, array=words))
