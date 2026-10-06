import heapq

def calculate_misplaced_tiles(state, goal_state=(1, 2, 3, 4, 5, 6, 7, 8, 0)):
    """
    Counts how many tiles are not in their correct goal position.
    The blank space (0) is not counted as a misplaced tile.
    """
    count = 0
    for i in range(9):
        if state[i] != 0: # Ignore the blank space
            if state[i] != goal_state[i]:
                count += 1
    return count

def get_neighbors(state):
    neighbors = []
    zero_idx = state.index(0)
    r, c = divmod(zero_idx, 3)
    
    # Grid movements for the empty slot (0): Up, Down, Left, Right
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nr < 3:
            n_idx = nr * 3 + nc
            new_state = list(state)
            new_state[zero_idx], new_state[n_idx] = new_state[n_idx], new_state[zero_idx]
            neighbors.append(tuple(new_state))
            
    return neighbors

def solve_8_puzzle_misplaced(start_state, goal_state= (1,2,3,8,0,4,7,6,5)):
    # open_list stores: (f_score, g_score, current_state, path_history)
    open_list = []
    h_init = calculate_misplaced_tiles(start_state, goal_state)
    heapq.heappush(open_list, (h_init, 0, start_state, [start_state]))
    
    g_scores = {start_state: 0}
    closed_set = set()
    
    print(f"--- Initial State Evaluation ---")
    print(f"Board: {start_state}")
    print(f"Initial Misplaced Tiles Count (h): {h_init}\n")
    
    debug_counter = 0

    while open_list:
        f, g, current, path = heapq.heappop(open_list)
        
        if current == goal_state:
            return path
            
        if current in closed_set:
            continue
        closed_set.add(current)
        
        # Log the first 3 nodes pulled from the priority queue to visualize the heuristic
        if debug_counter < 3:
            print(f"[Queue Pop] Evaluating state with lowest f={f} (g={g}, h={f-g})")
            print(f"  Layout: {current[0:3]} | {current[3:6]} | {current[6:9]}")
            debug_counter += 1
        
        for neighbor in get_neighbors(current):
            if neighbor in closed_set:
                continue
                
            tentative_g = g + 1
            if tentative_g < g_scores.get(neighbor, float('inf')):
                g_scores[neighbor] = tentative_g
                h_score = calculate_misplaced_tiles(neighbor, goal_state)
                f_score = tentative_g + h_score
                heapq.heappush(open_list, (f_score, tentative_g, neighbor, path + [neighbor]))
                
    return None

# --- YOUR HARDCODED TARGET STATE ---
initial_board = (2, 8, 3, 
                 1, 6, 4, 
                 0, 7, 5)

solution_path = solve_8_puzzle_misplaced(initial_board)

print("\n--- Final Status ---")
if solution_path:
    print(f"Solved in {len(solution_path) - 1} steps!")
else:
    print("No solution found. This layout is mathematically unsolvable.")