def solution(places: List[List]):

    def a_place(place):
        '하나의 대기실 체크'
        # 문제 생기면 바로 return 0
        ans = 1
        def build_visited():
            nonlocal place
            visited_map = [[False for i in range(5)] for j in range(5)]
            for i in range(5):
                for j in range(5):
                    if place[i][j] == 'X':
                        visited_map[i][j] = True
            return visited_map
            

        def dfs_helper(root, distance, first_check):
            nonlocal place, visited_map, ans
            i, j = root[0], root[1]
            visited_map[i][j] = True
            if place[i][j] == 'P' and first_check != 0:
                if distance <= 2:
                    ans = 0
                return
            
            togo = [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]
            def check_loc(loc):
                nonlocal visited_map
                i, j = loc[0], loc[1]
                if i < 0 or i > 4: return False
                if j < 0 or j > 4: return False
                if visited_map[i][j]:
                    return False
                return loc
            togo = list(map(check_loc, togo))

            for loc in togo:
                if loc:
                    dfs_helper(loc, distance+1, 1)
        
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    visited_map = build_visited()
                    dfs_helper((i,j), 0, 0)
                    if ans == 0:
                        return 0
        return 1
    
    return [a_place(place) for place in places]
