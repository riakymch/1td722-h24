# Imports
# Nothing to import

"""
A1:
"""
# my_efficient_sort
# A1
def my_efficient_sort(array):
    pass

"""
B1:
"""
# optimized my_efficient_sort
# B1
def my_efficient_sort_opt(array):
    pass

# Print the array
def print_list(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()

# A2
"""
Time and Space Complexity of your sorting algorithm
"""
def sort_analysis():
    my_answer = "Enter your answer and analysis in Theta, BigOh notation here"
    return(my_answer)

# A3
"""
GCD of two given numbers
"""
def gcd(a,b):
    pass

# Module main
if __name__ == '__main__':
    array = [8, 3, 5, 0, 12, 1, 33]

    # A1
    my_efficient_sort(array)
    print(f"A1: Sorted array: {array}\n")

    # A2
    print(f"A2: Analysis: \n {sort_analysis()}\n")

    # A3
    print(f"GCD of 15 and 5 is: {gcd(15, 5)}\n")

    # B1
    array = [8, 3, 5, 0, 12, 1, 33]
    my_efficient_sort_opt(array)
    print(f"B1 - Θ(nlog(n)): Sorted array: {array}\n")
    