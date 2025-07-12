import random

def identify_random_elements(max, num_random_elements):
    if num_random_elements > max:
        return []

    ids = []
    x = 0
    while x < num_random_elements:
        rand_int = random.randint(0, max - 1)

        if rand_int not in ids:
            ids.append(rand_int)
            x += 1

    return ids

def identify_random_elements_inc_49(max, num_random_elements):
    if num_random_elements > max:
        return []

    ids = []
    x = 0
    while x < num_random_elements-1:
        rand_int = random.randint(0, max - 1)

        if rand_int not in ids:
            ids.append(rand_int)
            x += 1

    ids.append(49)
    return ids