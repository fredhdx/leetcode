#Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.
#
#A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).


def equalPairs(grid: List[List[int]]) -> int:
    
    def convert_to_key(s: List[int]) -> str:
        return ",".join([str(_) for _ in s])
    
    n = len(grid)
   
    dic1 = defaultdict(int)
    for row in grid:
        dic1[convert_to_key(row)] += 1
    
    dic2 = defaultdict(int)
    for j in range(n):
        col = []
        for i in range(n):
            col.append(grid[i][j])
        dic2[convert_to_key(col)] += 1
        
    ans = 0
    for k in dic1:
        if k in dic2:
            ans += dic1[k] * dic2[k]
    
    return ans
        
