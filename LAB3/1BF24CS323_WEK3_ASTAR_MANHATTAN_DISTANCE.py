import heapq


def calculate_misplaced_tiles(state, goal_state):
    count = 0

    for i in range(9):
        if state[i] != 0 and state[i] != goal_state[i]:
            count += 1

    return count


def get_neighbors(state):
    neighbors = []

    zero_idx = state.index(0)
    r, c = divmod(zero_idx, 3)

    # Up, Down, Left, Right
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:

        nr = r + dr
        nc = c + dc

        if 0 <= nr < 3 and 0 <= nc < 3:

            n_idx = nr * 3 + nc

            new_state = list(state)

            new_state[zero_idx], new_state[n_idx] = \
                new_state[n_idx], new_state[zero_idx]

            neighbors.append(tuple(new_state))

    return neighbors


def solve_8_puzzle_misplaced(start_state, goal_state):

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
    print("Initial State:", start_state)
    print("Goal State   :", goal_state)
    print("Initial Misplaced Tiles (h):", h_init)

    while open_list:

        f, g, current, path = heapq.heappop(open_list)

        if current == goal_state:
            return path

        if current in closed_set:
            continue

        closed_set.add(current)

        for neighbor in get_neighbors(current):

            if neighbor in closed_set:
                continue

            tentative_g = g + 1

            if tentative_g < g_scores.get(
                    neighbor, float('inf')):

                g_scores[neighbor] = tentative_g

                h = calculate_misplaced_tiles(
                    neighbor,
                    goal_state
                )

                f_score = tentative_g + h

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


# ------------------------------------------------
# INPUT FUNCTION
# ------------------------------------------------

def get_state(message):

    while True:

        user_input = input(message).strip()

        # Case 1: User enters 283104765
        if user_input.isdigit() and len(user_input) == 9:

            state = tuple(
                int(x) for x in user_input
            )

        # Case 2: User enters 2 8 3 1 0 4 7 6 5
        else:

            values = user_input.split()

            if len(values) == 9:
                try:
                    state = tuple(
                        map(int, values)
                    )
                except ValueError:
                    state = ()
            else:
                state = ()

        # Validate
        if len(state) == 9 and set(state) == set(range(9)):
            return state

        print(
            "Invalid input!"
            "\nEnter exactly 9 digits containing "
            "0 to 8 once each."
        )


# ------------------------------------------------
# MAIN PROGRAM
# ------------------------------------------------

print("Enter Initial State")
print("Example: 283104765")
print("or     : 2 8 3 1 0 4 7 6 5")

initial_board = get_state(
    "Initial state: "
)


print("\nEnter Goal State")
print("Example: 123804765")
print("or     : 1 2 3 8 0 4 7 6 5")

goal_board = get_state(
    "Goal state: "
)


# ------------------------------------------------
# SOLVE
# ------------------------------------------------

solution_path = solve_8_puzzle_misplaced(
    initial_board,
    goal_board
)


# ------------------------------------------------
# OUTPUT
# ------------------------------------------------

print("\n--- Final Status ---")

if solution_path:

    print(
        "Solved in",
        len(solution_path) - 1,
        "steps!"
    )

    print("\n--- Solution Path ---")

    for step, state in enumerate(solution_path):

        g = step

        h = calculate_misplaced_tiles(
            state,
            goal_board
        )

        f = g + h

        print("\nStep", step)

        print(
            state[0:3]
        )

        print(
            state[3:6]
        )

        print(
            state[6:9]
        )

        print(
            "g =", g,
            "h =", h,
            "f =", f
        )

else:

    print("No solution found.")
