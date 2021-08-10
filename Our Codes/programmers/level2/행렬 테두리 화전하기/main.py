def teduri_index(query):
    x1, y1, x2, y2 = query
    a = [[x1, y1 + i] for i in range(y2 - y1)]
    b = [[x1 + i, y2] for i in range(x2 - x1)]
    c = [[x2, y2 - i] for i in range(y2 - y1)]
    d = [[x2 - i, y1] for i in range(x2 - x1)]
    return a + b + c + d

def new_teduri_values(array, teduri_index):
    _teduri_values = [
         array[x][y] for x, y in teduri_index]
    return [_teduri_values[-1]] + _teduri_values[0:len(_teduri_values) - 1]

def array(rows, columns):
    row = [i + 1 for i in range(columns)]
    
    return [[0 for _ in range(columns + 1)]] + [
       [0] + list(map(lambda x: x + i * columns, row)) for i in range(rows)
    ]

         
def solution(rows, columns, queries):
    _array = array(rows, columns)
    answer = []
    for query in queries:
        _teduri_index = teduri_index(query)
        _new_teduri_values = new_teduri_values(
            _array, _teduri_index)
        for index, value in enumerate(_teduri_index):
            x, y = value
            _array[x][y] = _new_teduri_values[index]
        answer.append(min(_new_teduri_values))
    
    return answer

if __name__ == "__main__":
  rows, columns = 6, 6
  queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
  print(solution(6, 6, queries))
