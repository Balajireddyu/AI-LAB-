import heapq

def calculate_misplaced_tiles(state, goal_state):
    """
    Counts how many tiles are not in their correct goal position.
    Blank space (0) is not counted.
    """
    count = 0

    for i in range(9):
        if state[i] != 0:
            if state[i] != goal_state[i]:
                count += 1

    return count


def get_neighbors(state):
    neighbors = []

    zero_idx = state.index(0)
    r, c = divmod(zero_idx, 3)

    # Up, Down, Left, Right
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:

        nr, nc = r + dr, c + dc

        # Correct condition
        if 0 <= nr < 3 and 0 <= nc < 3:

            n_idx = nr * 3 + nc

            new_state = list(state)

            new_state[zero_idx], new_state[n_idx] = \
                new_state[n_idx], new_state[zero_idx]

            neighbors.append(tuple(new_state))

    return neighbors


def solve_8_puzzle_misplaced(start_state, goal_state):

    # open_list stores:
    # (f_score, g_score, current_state, path_history)

    open_list = []

    h_init = calculate_misplaced_tiles(
        start_state,
        goal_state
    )

    heapq.heappush(
        open_list,
        (h_init, 0, start_state, [start_state])
    )

    g_scores = {start_state: 0}
    closed_set = set()

    print("\n--- Initial State Evaluation ---")
    print(f"Board: {start_state}")
    print(f"Goal : {goal_state}")
    print(f"Initial Misplaced Tiles Count (h): {h_init}\n")

    debug_counter = 0

    while open_list:

        f, g, current, path = heapq.heappop(open_list)

        if current == goal_state:
            return path

        if current in closed_set:
            continue

        closed_set.add(current)

        # Display first 3 queue pops
        if debug_counter < 3:

            print(
                f"[Queue Pop] Evaluating state with "
                f"lowest f={f} (g={g}, h={f-g})"
            )

            print(
                f"  Layout: {current[0:3]} | "
                f"{current[3:6]} | "
                f"{current[6:9]}"
            )

            debug_counter += 1

        for neighbor in get_neighbors(current):

            if neighbor in closed_set:
                continue

            tentative_g = g + 1

            if tentative_g < g_scores.get(
                    neighbor, float('inf')):

                g_scores[neighbor] = tentative_g

                h_score = calculate_misplaced_tiles(
                    neighbor,
                    goal_state
                )

                f_score = tentative_g + h_score

                heapq.heappush(
                    open_list,
                    (
                        f_score,
                        tentative_g,
                        neighbor,
                        path + [neighbor]
                    )
                )

    return None


# ==================================================
# USER INPUT
# ==================================================

print("Enter Initial State")
print("Example: 283104765")

initial_input = input("Initial state: ")


print("\nEnter Goal State")
print("Example: 123804765")

goal_input = input("Goal state: ")


# Convert 9-digit input into tuple
initial_board = tuple(
    int(x) for x in initial_input
)

goal_board = tuple(
    int(x) for x in goal_input
)


# Check input
if len(initial_board) != 9 or len(goal_board) != 9:

    print("Invalid input!")
    print("Please enter exactly 9 digits.")

else:

    # ==================================================
    # SOLVE
    # ==================================================

    solution_path = solve_8_puzzle_misplaced(
        initial_board,
        goal_board
    )


    # ==================================================
    # FINAL OUTPUT
    # ==================================================

    print("\n--- Final Status ---")

    if solution_path:

        print(
            f"Solved in {len(solution_path) - 1} steps!"
        )

        print("\n--- Solution Path ---")

        for step, state in enumerate(solution_path):

            g = step

            h = calculate_misplaced_tiles(
                state,
                goal_board
            )

            f = g + h

            print(f"\nStep {step}")

            print(
                f"{state[0:3]}\n"
                f"{state[3:6]}\n"
                f"{state[6:9]}"
            )

            print(
                f"g = {g}, h = {h}, f = {f}"
            )

    else:

        print(
            "No solution found. "
            "This layout is mathematically unsolvable."
        )
