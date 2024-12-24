# compute the diagonal difference between a left to right diagonal and right to left diagonal in a square matrix
# 1 2 3
# 4 5 6
# 9 8 9 
# abs diff = | (1+5+9) - (3+5+9) | = 2

# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.

def diagonalDifference(arr):
    n = len(arr)
    # calculate first diagonal (Left to Right)
    first_diag = 0
    second_diag = 0
    for r in range(n):
        first_diag += arr[r][r]
        # calculate second diagonal (right to left)
        second_diag += arr[r][(n-1)-r]

    difference = abs(first_diag - second_diag)
    return difference
# Time complexity: O(n)
# Space complexity: O(1)