# Solution 1
def order_1(sentence: str) -> str:
    """
    Sort the words in a given string based on the single digit (1-9)
    present in each word, which indicates its position in the result.
    Return an empty string if the input is empty.
    """
    new_sentence = []
    for digit in range(1, len(sentence.split()) + 1):
        for word in sentence.split():
            if str(digit) in word:
                new_sentence.append(word)
                break

    return " ".join(new_sentence)


# Solution 2
def order_2(sentence: str) -> str:
    """
    Sort the words in a given string based on the single digit (1-9)
    present in each word, which indicates its position in the result.
    Return an empty string if the input is empty.
    """
    sentence = sentence.split()
    res = []
    i = 1
    while len(sentence) > 0:
        for j in range(len(sentence)):
            if str(i) in sentence[j]:
                res.append(sentence.pop(j))
                i += 1
                break

    return " ".join(res)
