 

start = [1, 2, 3,
         4, 0, 6,
         7, 5, 8]

goal = [1, 2, 3,
        4, 5, 6,
        7, 8, 0]

max_depth = 30   # safety stop for unsolvable puzzles

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

# depth limited DFS
def dls(state, path, depth, limit):
    if state == goal:
        return path
    if depth == limit:
        return None
    for nxt in get_neighbors(state):
        if nxt not in path:     # avoid going in circles
            answer = dls(nxt, path + [nxt], depth + 1, limit)
            if answer is not None:
                return answer
    return None

# IDDFS: try limit = 0, 1, 2, ... until goal is found
solution = None
for limit in range(max_depth + 1):
    print("Trying depth limit", limit)
    solution = dls(start, [start], 0, limit)
    if solution is not None:
        break

print()
if solution is None:
    print("No solution found up to depth", max_depth)
else:
    print("Solved in", len(solution) - 1, "moves\n")
    for step, state in enumerate(solution):
        print("Step", step)
        show(state)