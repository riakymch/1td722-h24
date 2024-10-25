
"""
Tasks for modul 1 (A1, A2 and B1)
"""


def mysort(lst):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]


def A1():
    print('\nTask A1: Complexity of mysort')
    lst = [4, 2, 6, 6, 7, 2, 1, 9]
    mysort(lst)
    print('Sorted:', lst)
### A1 BEGIN ###
    my_answer = """ 
My answer to A1:
    The complexity is: Theta(?)
    Motivation: 


    Estimated time to sort a list of length 10^6 is:
    Motivation:



        """
### A1 END ###
    print(my_answer)
    print('End task A1\n')


### A2 BEGIN ###
def digit_sum(x, d=10):
    pass
### A2 END ###


def A2():
    print('\n\nTask A2: digit_sum')
    tests = ((0, 11), (1, 10), (3, 2), (9, 3), (10, 3), (11, 3),
             (3, 7), (15, 2), (2048, 16), (41, 20))
    for x in tests:
        print(f'Digit sum of {x[0]:5d} in base {x[1]:2d} is',
              f'{digit_sum(x[0], x[1])}')
    print('End A2 demonstration\n')


### B1 BEGIN ###
def split(l):
    '''B1: Split a list'''
    pass
### B1 END ###


def B1():
    print('\nTask B1: Demonstrate the split function')
    lists = ([],
             [0],
             [0, 1],
             [0, 1, 2],
             [0, 1, 2, 3],
             [0, 1, 2, 3, 4]
             )
    print('Argument                 Result')
    for lst in lists:
        print(f'{str(lst):15s} \t {split(lst)}')
    print('End B1 demonstration\n')


if __name__ == "__main__":
    A1()
    A2()
    # B1()

