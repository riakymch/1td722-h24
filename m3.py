"""
Tasks for module 3
"""


class LinkedList:

    class Node:
        def __init__(self, data, succ=None):
            self.data = data
            self.succ = succ

    def __init__(self):
        self.first = None

    def __iter__(self):
        current = self.first
        while current:
            yield current.data
            current = current.succ

    def __str__(self):
        return '(' + ', '.join([str(x) for x in self]) + ')'

    def append(self, x):
        if self.first is None:
            self.first = self.Node(x)
        else:
            f = self.first
            while f.succ:
                f = f.succ
            f.succ = self.Node(x)

    ### A6 BEGIN ###
    def __getitem__(self, index):
        pass
    ### A6 END ###

    ### B2 BEGIN ###
    def insert(self, x, index):
        pass
    # B2 END ###

# End of class LinkedList


class BST:

    class Node:
        def __init__(self, key, left=None, right=None):
            self.key = key
            self.left = left
            self.right = right
            self.count = 1  # For use in task B3 and B4

        def __str__(self):
            return f'({self.key}, {self.count})'

        def __iter__(self):
            if self.left:
                yield from self.left
            yield self
            if self.right:
                yield from self.right

    def __init__(self, init=None):
        self.root = None
        if init:
            for x in init:
                self.insert(x)

    def __iter__(self):
        if self.root:
            yield from self.root

    def __str__(self):
        return '<' + ', '.join([str(x.key) for x in self]) + '>'

    def __repr__(self):
        return '<' + ', '.join([str(x) for x in self]) + '>'

    def insert(self, key):
        """ Standard binary search tree insertion
        """
        def insert(key, r):
            if r is None:
                return BST.Node(key)
            elif key < r.key:
                r.left = insert(key, r.left)
            elif key > r.key:
                r.right = insert(key, r.right)
            else:
                pass  # Already there. Do nothing.
            return r

        self.root = insert(key, self.root)

    ### A7 BEGIN ###
    def sum_level(self, level):
        pass
    # A7 END ###

    ### B3 BEGIN ###
    # Write the new insert here. It will overide the
    # given insert.
    # def insert(self, key):
    #    pass
    ### B3 END ###

### Demo functions ###

def A6():
    print('\nA5: Index operator at linked list')
    llst = LinkedList()
    for x in (1, 3, 5, 7, 2, 4, 6):
        llst.append(x)
    print('llst: ', llst)
    for i in range(-1, 8):
        try:
            print(f'llst[{i}] : {llst[i]}')
        except IndexError as ie:
            print(ie)


def A7():
    print(f'\nA6: Sum of node keys on level in a binary tree')
    inserts = (5, 8, 1, 3, 7, 2, 6, 9)
    print(f'Inserted keys: {inserts}')
    tree = BST(inserts)
    print('Level   Sum of keys')
    for level in (0, 1, 2, 3, 4):
        result = tree.sum_level(level)
        print(f'{level:3d} {result}')


def B2():
    print(f'\nB2: Insert list nodes at specified positions')
    tests = ((2, 0), (3, 1), (9, 3), (1, -1), (1, 0), (4, 1),
             (9, 0), (5, 5))  # (data, position)
    llst = LinkedList()
    for e in tests:
        try:
            print(f'Insert {e[0]} in {llst} at index {e[1]} gives',
                  end=' ')
            llst.insert(e[0], e[1])
            print(llst)
        except IndexError as ie:
            print(f'IndexError:\n\t {ie}')


def B3():
    print(f'\nB3: Using insert that maintains the count fields.')
    inserts = (10, 10, 5, 1, 7, 20, 30, 15, 17, 12, 2, 2, 2)
    print(f'Inserted keys: {inserts}')
    tree = BST()
    for x in inserts:
        tree.insert(x)
        print(f'After inserting {x}: {repr(tree)}')


### Demo functions stop ###


if __name__ == '__main__':
    A6()
    B2()
    A7()
    B3()
    print()
