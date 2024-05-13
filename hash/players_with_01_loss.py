#You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.
#
#Return a list answer of size 2 where:
#
#answer[0] is a list of all players that have not lost any matches.
#answer[1] is a list of all players that have lost exactly one match.
#The values in the two lists should be returned in increasing order.

def findWinners(matches: List[List[int]]) -> List[List[int]]:
    score = {}

    for match in matches:
        winner, loser = match[0], match[1]
        if loser not in score:
            score[loser] = 0
        if winner not in score:
            score[winner] = 0
        score[loser] += 1

    ans = [[], []]
    players = sorted(score.keys())
    for player in players:
        if score[player] == 0:
            ans[0].append(player)
        elif score[player] == 1:
            ans[1].append(player)

    return ans
