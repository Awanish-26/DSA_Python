"""      Recursion       """
"""print first n natural namunbers"""

# def f1(n):
#     if n == 1:
#         return 1
#     s = n+f1(n-1)
#     return s


# r = f1(999)
# print(r)

# def f2(n):
#     if n>0:
#         f2(n-1)
#         print(n,end= " " )


# f2(20)

# def f3(n):
#     if n>0:
#         print(n,end= " " )
#         f3(n-1)


# f3(20)

# def f4(n):
#     if n>0:
#         f4(n-1)
#         print(2*n-1,end= " " )

# f4(20)

# print()

# def f5(n):
#     if n>0:
#         f5(n-1)
#         print(2*n,end= " " )

# f5(20)

def f6(n):
    if n>0:
        print(2*n-1,end= " " )
        f6(n-1)

f6(20)

print()

def f7(n):
    if n>0:
        print(2*n,end= " " )
        f7(n-1)

f7(20)