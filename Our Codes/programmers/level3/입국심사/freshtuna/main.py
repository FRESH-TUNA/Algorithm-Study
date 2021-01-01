def solution(n, times):
    left, right, answer = 1, max(times) * n, 0
    while left <= right:
        mid = (left + right)
        people = 0
        for i in times:
            people += mid
            if people >= n: break
        if people >= n:
            answer = mid
            right = mid - 1
        elif people < n:
            left = mid + 1
    return answer
