#Write a function that reverses a string. The input string is given as an array of characters s.
#
#You must do this by modifying the input array in-place with O(1) extra memory.

def reverse(s: str) -> str:
    i = 0
    j = len(s) - 1

    while i < j:
        tmp = s[i]
        s[i] = s[j]
        s[j] = tmp
        i += 1
        j -= 1

    return s
