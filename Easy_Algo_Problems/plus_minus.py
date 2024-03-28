# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.

# Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.

# Example arr = [1,1,0,-1,-1]

# There are n=5 elements, two positive, two negative and one zero. Their ratios are , 2/5, 2/5 and 1/5. Results are printed as:

# 0.400000 in 6 dp
# 0.400000
# 0.200000

def plusMinus(arr):
    # Write your code here
    plus_count = 0
    minus_count = 0
    zero_count = 0
    
    n = len(arr)
    
    for i in arr:
        if i < 0:
            minus_count += 1
        elif i > 0:
            plus_count += 1
        else:
            zero_count += 1
    
    plus_ratio = plus_count/n
    minus_ratio = minus_count/n
    zero_ratio = zero_count/n
    
    print(f"{plus_ratio:.6f}\n{minus_ratio:.6f}\n{zero_ratio:.6f}")

    # if there are more ratios to print, better to store in a list
    # ratio_output = [minus_count, plus_count, zero_count]
    # for r in ratio_output:
    #     ratio = r/n
    #     print(f"{ratio:.6f}")