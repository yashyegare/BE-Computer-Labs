def recursive(n):
    if (n < 2):
        return 1

    return recursive(n-1) + recursive(n-2)


n = int(input("Enter a positive number: "))
print(f"First {n} Fibonacci numbers are")
for i in range(n):
    print(recursive(i), end=" ")
