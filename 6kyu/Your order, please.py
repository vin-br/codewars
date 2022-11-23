# Description:

# Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.

# Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

# If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.
# Examples

# "is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
# "4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
# ""  -->  ""

# Solution 1
def order(sentence):
    new_sentence = []
    for digit in range (1,len(sentence.split()) + 1):
        for word in sentence.split():
            if str(digit) in word:
                new_sentence.append(word)
                break
                
    return " ".join(new_sentence)

# Solution 2
def order(sentence):
    sentence = sentence.split()
    res = []
    i = 1
    while len(sentence) > 0:
        for j in range(len(sentence)):
            if str(i) in sentence[j]:
                res.append(sentence.pop(j))
                i += 1
                break

    return ' '.join(res)