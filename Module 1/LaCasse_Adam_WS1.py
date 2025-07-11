import random

# TASK 1 ========================================================
def MCSS_1(a):
    largest, acc, i = 0, 0, 0

    for j in range(len(a)):
        acc += a[j]

        if (acc > largest):
            largest = acc
        elif (acc < 0):
            i = j + 1
            acc = 0

    return largest

def generate_random_vector(size=1000, min_val=-100, max_val=100):
    """
    Generate a vector of random positive and negative integers.
    
    Arguments:
        size: Number of elements in the vector
        min_val: Minimum value for random integers
        max_val: Maximum value for random integers
    
    Returns:
        list: Vector of random integers
    """
    return [random.randint(min_val, max_val) for _ in range(size)]

vector = generate_random_vector()
print(MCSS_1(vector))

# TASK 2 ========================================================
def MCSS_2(a):
    largest, acc, i = 0, 0, 0
    start_idx, end_idx = 0, 0

    for j in range(len(a)):
        acc += a[j]

        if (acc > largest):
            largest = acc
            start_idx = i
            end_idx = j
        elif (acc < 0):
            i = j + 1
            acc = 0

    return largest, start_idx, end_idx

# Test MCSS_2 function
vector = generate_random_vector()
max_sum, start, end = MCSS_2(vector)
print(f"MCSS_2 result: Maximum sum = {max_sum}, Start index = {start}, End index = {end}")
print(f"Subarray: {vector[start:end+1]}")
