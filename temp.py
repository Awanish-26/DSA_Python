# Count the most frequently element in the list
# x = [1, 1, 1, 1, 2, 1, 3, 5, 6, 1, 7, 4, 5, 3, 2, 6, 4, 5, 7, 5, 3, 4, 2]

# most = max(set(x), key=x.count)

# print(most)


# Decorators in python
# def my_decorator(func):
#     def wrapper():
#         print(f"Running {func.__name__}")
#         func()
#         print("Completed")
#     return wrapper


# @my_decorator
# def do_this():
#     print("Doing this")


# @my_decorator
# def do_that():
#     print('Doing that')


# do_this()
# do_that()


# using removeprefix instead of lstrip
links = [
    "www.blog.com",
    "www.youtube.com",
    "www.google.com",
    "www.wikipedia.com"
]

for link in links:
    print(link.removeprefix("www."))
    print(link.lstrip("www."))
