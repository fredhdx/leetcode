#Given an array of strings strs, group the anagrams together.
#
#For example, given strs = ["eat","tea","tan","ate","nat","bat"], return [["bat"],["nat","tan"],["ate","eat","tea"]].

def solution(strs: List[str])->List[List[str]]:
    ans = {}
    for s in strs:
        key = "".join(sorted(s))
        ans[key].append(s)

    return list(ans.values())
