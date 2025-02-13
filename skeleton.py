import sys
import math
from collections import defaultdict, deque, Counter
from itertools import permutations, combinations
from heapq import heappush, heappop

# Fast I/O for competitive programming
def input():
    return sys.stdin.readline().rstrip()

def main():
    # Read input
    n = int(input())  # Example: Read an integer
    arr = list(map(int, input().split()))  # Example: Read a list of integers

    # Logic to solve the problem
    result = solve(n, arr)  # Replace with your logic

    # Output the result
    print(result)

# Example solve function (replace with your logic)
def solve(n, arr):
    # Your problem-solving logic here
    return 0  # Replace with actual result

# Call the main function
if __name__ == "__main__":
    main()