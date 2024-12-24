def getSecond(index):
    return index[1]

intervals = [[7,10],[10,12],[2,4],[2,3]]
print(sorted(intervals, key=getSecond))