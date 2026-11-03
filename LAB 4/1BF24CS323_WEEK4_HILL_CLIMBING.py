
import random

def calculate_cost(state):
    cost = 0
    n = len(state)

    for i in range(n):
        for j in range(i + 1, n):
            # Queens attack diagonally if row difference
            # equals column difference
            if abs(state[i] - state[j]) == abs(i - j):
                cost += 1

    return cost

def get_neighbors(state):
    neighbors = []
    n = len(state)

    for i in range(n):
        for j in range(i + 1, n):
            new_state = state.copy()
            new_state[i], new_state[j] = (
                new_state[j], new_state[i]
            )
            neighbors.append(new_state)

    return neighbors

def hill_climbing():
    state = random.sample(range(4), 4)

    while True:
        current_cost = calculate_cost(state)

        print("State:", state, "Cost:", current_cost)

        if current_cost == 0:
            print("Solution found:", state)
            return

        neighbors = get_neighbors(state)

        best_neighbor = min(neighbors, key=calculate_cost)
        best_cost = calculate_cost(best_neighbor)

        if best_cost >= current_cost:
            print("Local minimum reached. Restarting...")
            state = random.sample(range(4), 4)
        else:
            state = best_neighbor

hill_climbing()
