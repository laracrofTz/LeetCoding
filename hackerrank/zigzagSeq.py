# this is a debugging question

def findZigZagSequence(a, n):
    a.sort()
    mid = (n - 1)//2 # initial: mid = int((n+1)/2) --> NOT the middle value in the arr
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1
    ed = n - 2 # initial: ed = n - 1 --> we already swapped the mid value with the last value in the arr, 
    # so ed must be at the 2nd last element 
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1 # we are increasing start since we want to sort the values from k to n-1 in descending order
        # the elements from 0 to k are already increasing and hence need not be modified
        ed = ed - 1 # initial: ed = ed + 1 --> error: list index out of range,
        # ed must reduce since our condition checks if st is lesser than equal to ed

    for i in a:
        print(i, end = ' ')
    # for i in range (n): # can change this to the one above too
        # if i == n-1:
        #     print(a[i])
        # else:
        #     print(a[i], end = ' ')
    return

test_cases = int(input())
for cs in range (test_cases):
    n = int(input())
    a = list(map(int, input().split()))
    findZigZagSequence(a, n)



