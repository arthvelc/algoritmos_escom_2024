import random
import time
import pandas as pd

def search_one_array(A, t):
    for i in range(len(A)):
        if A[i] == t:
            return True
    return False

def search_two_arrays(A, B, t):
    for i in range(len(A)):
        if A[i] == t:
            return True
    for i in range(len(B)):
        if B[i] == t:
            return True
    return False

def check_common_element(A, B):
    for i in range(len(A)):
        for j in range(len(B)):
            if A[i] == B[j]:
                return True
    return False

def check_duplicates(A):
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[i] == A[j]:
                return True
    return False

# Generate random arrays
n_values = [10, 100, 1000, 10000, 1000000]
arrays = []
for n in n_values:
    array = [random.randint(1, 100) for _ in range(n)]
    arrays.append(array)

# Measure execution time for each algorithm and input size
results = []
for i in range(len(n_values)):
    n = n_values[i]
    array = arrays[i]

    start_time = time.time()
    search_one_array(array, 42)
    end_time = time.time()
    search_one_array_time = end_time - start_time

    start_time = time.time()
    search_two_arrays(array, array, 42)
    end_time = time.time()
    search_two_arrays_time = end_time - start_time

    start_time = time.time()
    check_common_element(array, array)
    end_time = time.time()
    check_common_element_time = end_time - start_time

    start_time = time.time()
    check_duplicates(array)
    end_time = time.time()
    check_duplicates_time = end_time - start_time

    results.append([search_one_array_time, search_two_arrays_time, check_common_element_time, check_duplicates_time])

# Create pandas DataFrame to present the results
df = pd.DataFrame(results, columns=['search_one_array', 'search_two_arrays', 'check_common_element', 'check_duplicates'])
df.insert(0, 'n', n_values)
# Save the results to a CSV file
df.to_csv('/home/artur/ESCOM/ADA/Practica_lab_1/results.csv', index=False)

print(df)