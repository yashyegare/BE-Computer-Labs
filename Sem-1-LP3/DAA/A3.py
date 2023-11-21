# Fractional Knapsack problem using a greedy method

# Define a class for an item
class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.value_per_weight = value / weight


# Function to solve the fractional knapsack problem
def fractional_knapsack(items, capacity):
    # Sort items by value per weight in descending order
    items.sort(key=lambda x: x.value_per_weight, reverse=True)

    total_value = 0.0
    knapsack = []

    for item in items:
        if item.weight <= capacity:
            # Take the whole item
            knapsack.append((item, 1.0))
            total_value += item.value
            capacity -= item.weight
        else:
            # Take a fraction of the item to fill the remaining capacity
            fraction = capacity / item.weight
            knapsack.append((item, fraction))
            total_value += item.value * fraction
            break  # Knapsack is full

    return total_value, knapsack


# Take user input for items and knapsack capacity
def get_user_input():
    items = []
    n = int(input("Enter the number of items: "))
    for i in range(n):
        weight, value = input(
            f"Enter the weight, value of item {i + 1}: ").split()
        weight = float(weight)  # Convert to float
        value = float(value)    # Convert to float
        items.append(Item(weight, value))

    capacity = float(input("Enter the capacity of the knapsack: "))

    return items, capacity


# Main
if __name__ == "__main__":
    items, capacity = get_user_input()

    max_value, knapsack_contents = fractional_knapsack(items, capacity)

    print("Maximum value:", max_value)
    print("Knapsack contents:")
    for item, fraction in knapsack_contents:
        print(
            f"Item with weight {item.weight} and value {item.value}, Fraction taken: {fraction}")
        
# ----------------------------------------------------------------------

# OUTPUT-

# Enter the number of items: 3
# Enter the weight, value of item 1: 10 60
# Enter the weight, value of item 2: 20 100
# Enter the weight, value of item 3: 30 120

# Enter the capacity of the knapsack: 50

# Maximum value: 240.0

# Knapsack contents:
# Item with weight 10.0 and value 60.0, Fraction taken: 1.0
# Item with weight 20.0 and value 100.0, Fraction taken: 1.0
# Item with weight 30.0 and value 120.0, Fraction taken: 0.6
