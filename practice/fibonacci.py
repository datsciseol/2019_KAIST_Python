def FibonacciDP(n):
    dicFibonacci = {}
    dicFibonacci[0] = 1
    dicFibonacci[1] = 1
    for iter in range(2, n + 1):
        dicFibonacci[iter] = dicFibonacci[iter - 1] + dicFibonacci[iter - 2]
    return dicFibonacci[n]





print(FibonacciDP(1))