"""
Source: https://www.geeksforgeeks.org/python-program-for-tower-of-hanoi/
Contributed by Dilip Jain to geeksforgeeks
Time Complexity: O(2^n)
Auxiliary Space: O(n)
"""


# Recursive Python function to solve the tower of hanoi
def TowerOfHanoi(n, source, destination, auxiliary):
    """Disc being transfered from source -> auxiliary"""
    if n == 1:
        print("Move disk 1 from source", source, "to destination", destination)
        return
    TowerOfHanoi(n - 1, source, auxiliary, destination)
    print("Move disk", n, "from source", source, "to destination", destination)
    TowerOfHanoi(n - 1, auxiliary, destination, source)


number_of_discs = 4

TowerOfHanoi(number_of_discs, "A", "B", "C")
# A, B, C are the name of rods
