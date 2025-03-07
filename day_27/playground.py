# positional arguments
def add(*args):
    sum = 0
    print(args)
    for arg in args:
        sum += arg
    print(sum)

add(1, 2, 3, 4, 5, 6)

# keyword arguments
