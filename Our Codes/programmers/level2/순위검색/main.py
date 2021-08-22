def solution(info, query):
    def _filter(info, query, score):
        answer = info
        for index, value in enumerate(query):
            if value != "-":
                answer = list(filter(lambda x: x[index] == value, answer))
        return len(list(filter(lambda x: int(x[-1]) >= int(score), answer)))

    answer = []
    info = [_info.split() for _info in info]
    for _query in query:
        _query = _query.split(" ")
        answer.append(_filter(info, filter(lambda x: x != "and", _query[:-1]), _query[-1]))
    return answer

if __name__ == "__main__":
    info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
    query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
    query = ["- and - and - and - 150"]
    print(solution(info, query))
