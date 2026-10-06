

start = [1, 2, 3,
         4, 0, 6,
         7, 5, 8]

goal = [1, 2, 3,
        4, 5, 6,
        7, 8, 0]

limit = 10   # max depth allowed

def show(state):
    for i in range(0, 9, 3):
        print(state[i], state[i+1], state[i+2])
    print()

def get_neighbors(state):
    result = []
    i = state.index(0)          # position of blank
    row = i // 3
    col = i % 3

    if row > 0:                 # move blank up
        new = state[:]
        new[i], new[i-3] = new[i-3], new[i]
        result.append(new)
    if row < 2:                 # move blank down
        new = state[:]
        new[i], new[i+3] = new[i+3], new[i]
        result.append(new)
    if col > 0:                 # move blank left
        new = state[:]
        new[i], new[i-1] = new[i-1], new[i]
        result.append(new)
    if col < 2:                 # move blank right
        new = state[:]
        new[i], new[i+1] = new[i+1], new[i]
        result.append(new)
    return result

def dfs(state, path, depth):
    if state == goal:
        return path
    if depth == limit:
        return None
    for nxt in get_neighbors(state):
        if nxt not in path:     # avoid going in circles
            answer = dfs(nxt, path + [nxt], depth + 1)
            if answer is not None:
                return answer
    return None

solution = dfs(start, [start], 0)

if solution is None:
    print("No solution found within depth limit", limit)
else:
    print("Solved in", len(solution) - 1, "moves\n")
    for step, state in enumerate(solution):
        print("Step", step)
        show(state)