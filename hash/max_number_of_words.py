#Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
#
#You can use each character in text at most once. Return the maximum number of instances that can be formed.

def maxNumberOfBalloons(text: str) -> int:
    count = {
        "b": 0,
        "a": 0,
        "l": 0, # 2
        "o": 0, # 2
        "n": 0
    }

    for x in text:
        if x in count:
            count[x] += 1

    count['l'] //= 2
    count['o'] //= 2

    return min(count.values())
