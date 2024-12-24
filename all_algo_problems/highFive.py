from collections import defaultdict
class Solution(object):
    def highFive(self, items):
        """
        :type items: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        scores = defaultdict(list)
        for p in items:
            scores[p[0]].append(p[1])
        for id in scores.keys():
            scores[id].sort(reverse=True)
            avg = (scores[id][0] + scores[id][1] + scores[id][2] + scores[id][3] + scores[id][4])//5
            res.append([id, avg])
        res.sort()
        return res
    
# Complexity
# Time ->
# Space ->