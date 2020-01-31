import time

""" 
***!Important!*** If you are running this using PowerShell by clicking on the green play button, you will get an error that `names1.txt` is not found.  To resolve this, run it, get the error, then `cd` into the `names` directory in the `python` terminal that opens in VSCode.

Navigate into the `names` directory. Here you will find two text files containing 10,000 names each, along with a program `names.py` that compares the two files and prints out duplicate name entries. Try running the code with `python3 names.py`. Be patient because it might take a while: approximately six seconds on my laptop. What is the runtime complexity of this code?

Six seconds is an eternity so you've been tasked with speeding up the code. Can you get the runtime to under a second? Under one hundredth of a second?

*You may not use the built in Python list, set, or dictionary for this problem*

(Hint: You might try importing a data structure you built during the week)
"""


class BinarySearchTree:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # If inserting we must already have a tree/root
        # if value is less than self.value go left, make a new tree/node if empty, otherwise
        # keep going (recursion)
        if self.value == None:
            self.value = value
        if value < self.value:
            if self.left == None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)

        # if greater than or equal to then go right, make a new tree/node if empty, otherwise
        # keep going.
        elif value >= self.value:
            if self.right == None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if target = self.value return it
        # go left or right based on smaller or bigger
        if target == self.value:
            return True
        elif target < self.value:
            if self.left == None:
                return False
            else:
                return self.left.contains(target)
        elif target > self.value:
            if self.right == None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # start here, easy
        # if right exists, go right
        # otherwise return self.value
        if self.right != None:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        if node == None:
            return

        if node.left != None:
            self.in_order_print(node.left)

        print(node.value)

        if node.right != None:
            self.in_order_print(node.right)


start_time = time.time()

bst_names = BinarySearchTree()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

# building a tree to the list
for name in names_1:
    bst_names.insert(name)

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()


duplicates = []
# this takes 7.46 seconds
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# run search to check if it's equal to the value, this will run another search and compare the other list
# this takes 0.17 seconds
for name in names_2:
    if bst_names.contains(name):
        duplicates.append(name)


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?
