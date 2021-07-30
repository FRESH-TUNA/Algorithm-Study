def solution(s):
    s = list(s)
    is_truncated = True
    
    while is_truncated and len(s) > 0:
        count = -1
        prev_index = 0
        is_truncated = False

        for i in range(len(s)):
            if s[prev_index] == s[i]: count += 1
            else:
                if count > 0: 
                    s = s[0:prev_index] + s[prev_index + count + 1:]
                    is_truncated, count = True, 0
                    break
                prev_index = i
        
        if count > 0: 
            s = s[0:prev_index] + s[prev_index + count + 1:]
            is_truncated = True

    if len(s) == 0: return 1
    else: return 0

if __name__== "__main__" :
    print(solution("baabaa"))
