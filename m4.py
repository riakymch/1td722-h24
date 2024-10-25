# Imports
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import time

# A9: write a one-line list comprehension to return all even elements in a list
def even_elements(list):
    pass

# factorial helper
def factorial(x):
    fact = 1
    for i in range(1, x+1):
        fact *= i
    #print(f'Factorial of {x}: {fact}')
    return fact

# A10: multi-processing
def fact_multiprocessing(x):
    pass

# B4: multi-threading
def fact_multithreading(x):
    pass

# B4: serial
def fact_serial(x):
    pass

# B4: Analysis
def my_analysis():
    my_answer = "Enter your answer and analysis of comparisons between multi-processing/threading and serial"
    return(my_answer)

# Main
if __name__ == '__main__':
    # A9
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    print(f"Even numbers: {even_elements(numbers)}\n")

    # calculate factorial up to 50
    values = 50

    # Multiprocessing
    # Call the corresponding function here, measure running time 
    
    # Multithreading
    # Call the corresponding function here, measure running time

    # Serial
    # Call the corresponding function here, measure running time

    my_analysis()
