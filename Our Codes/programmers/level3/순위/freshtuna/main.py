def solution(n, results):
    wins, loses = {}, {}
    
    for i in range(1, n + 1):
        wins[i], loses[i] = set(), set()       
    
    for i in range(1, n + 1):                    
        for case in results:                      
            if case[0] == i: wins[i].add(case[1])
            if case[1] == i: loses[i].add(case[0])
    
        for winner in loses[i]:                
            wins[winner].update(wins[i])
        for loser in wins[i]:
            loses[loser].update(loses[i]) 
    count = 0
    for i in range(1, n + 1):                   
        if len(wins[i]) + len(loses[i]) == n - 1:
            count += 1
            
    return count
