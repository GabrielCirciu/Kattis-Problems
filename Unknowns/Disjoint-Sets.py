n, m = map(int, input().split())
elements_to_representatives, sets_to_elements = dict(), dict()

# Create disjoint sets {0}{1}{2}...{n-1}
for i in range(n):
    elements_to_representatives[i] = i
    sets_to_elements[i] = [i]

for _ in range(m):
    # Perform operations m times
    operation, s, t = map(int, input().split())

    # Query, if two elements are part of the same set
    if operation == 0:
        print("1") if elements_to_representatives[s] == elements_to_representatives[t] else print("0")

    # Union, merge two sets based on which set x and y is in
    elif operation == 1:
        if elements_to_representatives[s] != elements_to_representatives[t]:
            for element in sets_to_elements[elements_to_representatives[t]]:
                elements_to_representatives[element] = elements_to_representatives[s]
                sets_to_elements[elements_to_representatives[s]].append(element)
            #del sets_to_elements[t] - Not needed and gives runtime error anyways

    # Move element s from its set to set containing t
    else:
        if elements_to_representatives[s] != elements_to_representatives[t]:
            sets_to_elements[elements_to_representatives[t]].append(s)
            sets_to_elements[elements_to_representatives[s]].remove(s)
            elements_to_representatives[s] = elements_to_representatives[t]
            pass
