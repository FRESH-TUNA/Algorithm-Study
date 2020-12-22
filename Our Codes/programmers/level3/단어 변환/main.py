def solution(begin, target, words):
    class Solution:
        def __init__(self, begin, target, words):
            self.begin = begin
            self.target = target
            self.words = [begin] + words
            self.answer = 100
            self.depth = 0
            self.is_traced = [False for _ in range(len(words))]
    
        def check(self, i, j):
            count = 0
            for z in range(len(i)):
                if i[z] != j[z]: count += 1
                if count > 1: return False
            return True

        def dfs(self, i):
            if self.words[i] == self.target:
                self.answer = min(self.depth, self.answer)
            else:    
                for y, word in enumerate(self.words):
                    if not self.is_traced[y] and self.check(self.words[i], word):
                        self.is_traced[i] = True
                        self.depth += 1
                        self.dfs(y)
         
        def service(self):
            if target not in self.words: return 0
            self.dfs(0)
            return self.answer if self.answer != 100 else 0
        
    return Solution(begin, target, words).service()
        
    
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
