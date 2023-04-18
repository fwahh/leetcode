from collections import defaultdict
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses_reqs = {i: 0 for i in range(numCourses)}
        neighbors = defaultdict(list)
        for a, b in prerequisites:
            neighbors[b].append(a)
            courses_reqs[a] += 1
        to_remove = [i for i,v in courses_reqs.items() if v == 0]
        order = []
        
        while to_remove:
            cur = to_remove.pop()
            order.append(cur)
            
            for neighbor in neighbors[cur]:
                courses_reqs[neighbor] -= 1
                if courses_reqs[neighbor] == 0:
                    to_remove.append(neighbor)
        return order if all(i == 0 for i in courses_reqs.values()) else []
    
numCourses = 2
prerequisites = [[1,0]]
print(Solution().findOrder(numCourses, prerequisites))