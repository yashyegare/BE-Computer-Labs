def knapsack(max_weight, n, values, weights):
    # Populate base cases
    # dp = [[0] * (max_weight + 1) for _ in range(n + 1)]
    dp = [[0 for _ in range(max_weight+1)] for _ in range(n + 1)]

    # Main logic
    for item in range(1, n + 1):
        for capacity in range(1, max_weight + 1):
            max_val_without_current_item = dp[item - 1][capacity]
            max_val_with_current_item = 0
            weight_of_current_item = weights[item - 1]

            if capacity >= weight_of_current_item:
                max_val_with_current_item = values[item - 1]

                remaining_capacity = capacity - weight_of_current_item
                max_val_with_current_item += dp[item - 1][remaining_capacity]

            dp[item][capacity] = max(
                max_val_without_current_item, max_val_with_current_item)

    # Traceback to find selected items
    selected_items = []
    current_item, remaining_capacity = n, max_weight
    while current_item > 0 and remaining_capacity > 0:
        if dp[current_item][remaining_capacity] != dp[current_item - 1][remaining_capacity]:
            selected_items.append(current_item - 1)
            remaining_capacity -= weights[current_item - 1]
        current_item -= 1
    selected_items = [x+1 for x in selected_items]
    return dp[n][max_weight], selected_items[::-1]


# Example usage
max_weight = 50
n = 3
values = [60, 100, 120]
weights = [10, 20, 30]

result_value, selected_items = knapsack(max_weight, n, values, weights)
print("Maximum value:", result_value)
print("Selected items:", selected_items)


# max_weight = 10
# n = 4
# values = [20, 30, 10, 50]
# weights = [1, 3, 4, 6]
