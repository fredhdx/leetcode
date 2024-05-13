#Given a string s, return the first character to appear twice. It is guaranteed that the input will have a duplicate character.

def solution(s: str) -> str:
    tmp = {}
    for c in s:
        if c in tmp:
            return c
        else:
            tmp[c] = 1
