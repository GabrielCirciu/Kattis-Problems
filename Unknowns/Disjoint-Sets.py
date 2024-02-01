# n - number of singletons, m - number of lines of input
n, m = map(int, input().split())
sets = dict()

# Create disjoint sets {0}{1}{2}...{n-1}
for i in range(n):
    sets[i] = i

# Process each row of input
for _ in range(m):
    operation, x, y = map(int, input().split())

    # Query if two elements are part of the same set
    if operation == 0:
        print("1") if sets[x] == sets[y] else print("0")

    # MERGE SETS NOT ELEMENTS
    # Union
    elif operation == 1:
        pass

    # Move element from one set to another
    else:
        if sets[x] != sets[y]:
            sets[y] = sets[x]
