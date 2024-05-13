#A pangram is a sentence where every letter of the English alphabet appears at least once.
#
#Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

def checkIfPangram(self, sentence: str) -> bool:
    coll = set()
    for c in sentence:
        coll.add(c)
        
    return len(coll) == 26
