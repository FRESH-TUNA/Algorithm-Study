def solution(record):
    user_pool = dict()
    logs = []
    
    for i in range(len(record)):
        log = record[i].split()
        action, uid = log[0], log[1]    
        
        if action == "Enter":
            logs.append([uid, "님이 들어왔습니다."])
            user_pool.update({uid: log[2]})
        elif action == "Leave":
            logs.append([uid, "님이 나갔습니다."])
        elif action == "Change":
            user_pool.update({uid: log[2]})
    
    for i in range(len(logs)):
        logs[i] = user_pool[logs[i][0]] + logs[i][1]
    
    return logs

if __name__== "__main__" :
    record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
    print(solution(record))