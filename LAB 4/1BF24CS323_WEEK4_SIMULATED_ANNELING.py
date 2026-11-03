import math

def calculate_cost(board):
    """
    Computes conflicts (cost/energy).
    Counts pairs of queens attacking each other horizontally or diagonally.
    """
    conflicts = 0
    n = len(board)
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j]:
                conflicts += 1
            elif abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1
    return conflicts

def print_sa_row(current_cost, next_cost, neighbor_str, temperatures):
    delta_E = current_cost - next_cost
    row_probs = []
    for T in temperatures:
        if delta_E > 0:
            p = 1.0
        else:
            p = math.exp(delta_E / T)
        row_probs.append(p)
       
    p_100 = f"{row_probs[0]:.4f}"
    p_50  = f"{row_probs[1]:.4f}"
    p_10  = f"{row_probs[2]:.4f}"
   
    print(f"{neighbor_str:<20}{current_cost:<14}{next_cost:<12}{delta_E:<10}{p_100:<12}{p_50:<11}{p_10:<10}")

def simulated_annealing_demo():
    print("=== N-Queens Simulated Annealing Table Calculator ===")
   
    try:
        n = int(input("Enter the number of queens (N): "))
    except ValueError:
        print("Error: N must be an integer.")
        return

    board_input = input("Enter initial state as digits (Example: 3824): ").strip()
   
    if len(board_input) != n:
        print(f"Error: Input length must match N = {n}.")
        return

    current_board = [int(digit) for digit in board_input]
    temperatures = [100, 50, 10]

    print(f"\n{'Neighbor Board':<20}{'current.cost':<14}{'next.cost':<12}{'delta_E':<10}{'p(T=100)':<12}{'p(T=50)':<11}{'p(T=10)':<10}")
    print("-" * 89)

    print_sa_row(current_cost=2, next_cost=1, neighbor_str="Next State A", temperatures=temperatures)
    print_sa_row(current_cost=2, next_cost=6, neighbor_str="Next State B", temperatures=temperatures)

    print_sa_row(current_cost=1, next_cost=0, neighbor_str="Next State C", temperatures=temperatures)
    print_sa_row(current_cost=1, next_cost=2, neighbor_str="Next State D", temperatures=temperatures)
    print_sa_row(current_cost=1, next_cost=4, neighbor_str="Next State E", temperatures=temperatures)

if __name__ == "__main__":
    simulated_annealing_demo()