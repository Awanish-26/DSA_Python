Choice = int(input("Enter the Number :"))


def SumN(n):
    if n == 1:
        return 1
    return n+SumN(n-1)


print("Sum till N is :", SumN(Choice))


def SumNOdd(n):
    if n == 1:
        return 1
    return 2*n-1 + SumNOdd(n-1)


print("Sum till N Odd is :", SumNOdd(Choice))


def SumNEven(n):
    if n == 1:
        return 2
    return 2*n + SumNEven(n-1)


print("Sum till N Even is :", SumNEven(Choice))


def fact(n):
    if n == 1:
        return 2
    return n*fact(n-1)


print("Factorial is :", fact(Choice))


def SquareSum(n):
    if n == 1:
        return 1
    return n*n + SquareSum(n-1)


print("Sum  is :", SquareSum(Choice))
