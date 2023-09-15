for _ in range(int(input())):
    cities = list()
    visited_count = 0
    for number_of_cities in range(int(input())):
        city = input()
        if city not in cities:
            cities.append(city)
            visited_count += 1
    print(visited_count)