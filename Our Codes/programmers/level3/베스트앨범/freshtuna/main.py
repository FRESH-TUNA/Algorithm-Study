from functools import cmp_to_key
def solution(genres, plays):
    def comparator(x, y):
        if x[0] < y[0]: return 1
        elif x[0] > y[0]: return -1
        elif x[1] < y[1]: return -1
        else: return 1

    answer, datas = [], {}
    for index, genre in enumerate(genres):
        if not genre in datas: datas[genre] = {
            "amount": 0, "songs": []}
        datas[genre]["songs"].append((plays[index], index))
        datas[genre]["amount"] += plays[index]
    datas = sorted(datas.items(), key=lambda x: x[1]["amount"], reverse=True)
    for data in datas:
        count = 0
        for _data in sorted(data[1]["songs"], key=cmp_to_key(comparator)):
            if count == 2: break 
            else: count += 1
            answer.append(_data[1])
    return answer
