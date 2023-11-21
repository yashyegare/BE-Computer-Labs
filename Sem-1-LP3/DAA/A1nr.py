def non_recursive(n):
    fibo = []
    fibo.append(1)
    fibo.append(1)
    for i in range(2, n):
        fibo.append(fibo[i-1] + fibo[i-2])

    return fibo


n = int(input("Enter a positive number: "))
print(f"First {n} Fibonacci numbers are")
print(non_recursive(n))
