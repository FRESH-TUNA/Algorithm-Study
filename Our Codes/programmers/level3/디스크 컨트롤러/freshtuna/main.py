import heapq
from collections import deque

def solution(jobs):
    jobs = deque(sorted(jobs))
    processed, current_time, waiting_time, queue = 0, 0, 0, []

    while queue or jobs:
        if not queue:
            requested_time, expected_time = jobs.popleft()
            current_time = requested_time + expected_time
            waiting_time += expected_time
        else:
            expected_time, requested_time = heapq.heappop(queue)
            current_time += expected_time
            waiting_time += current_time - requested_time
        processed += 1

        while jobs and jobs[0][0] <= current_time:
            heapq.heappush(queue, jobs.popleft()[::-1])
        
    return waiting_time // processed
