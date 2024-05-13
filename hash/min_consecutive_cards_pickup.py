#Given an integer array cards, find the length of the shortest subarray that contains at least one duplicate. If the array has no duplicates, return -1.

def solution(cards: List[str]) -> int:
    count = {}
    ans = len(cards) + 1

    for i in range(len(cards)):
        val = cards[i]
        if val in count:
            ans = min(ans, i - count[val] + 1)
        count[val] = i

    if ans == len(cards) + 1:
        return -1


