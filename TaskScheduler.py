import heapq
from collections import Counter
from typing import List

class Task:
    def __init__(self, name: str, earliest_time: int, ranking: int):
        self.name = name
        self.earliest_time = earliest_time
        self.ranking = ranking

    def __lt__(self, other):
        if self.earliest_time == other.earliest_time:
            return self.ranking < other.ranking
        return self.earliest_time < other.earliest_time


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # because of cooldown period between two same tasks,
        # we'll take the greedy approach and just do the more
        # frequently occuring tasks first
        task_freq = Counter(tasks)

        order_of_tasks = sorted(
            task_freq.keys(), key=lambda x: task_freq[x], reverse=True
        )
        urgency = {
            c: {"rank": i, "earliest_time": i} for i, c in enumerate(order_of_tasks)
        }
        to_do = []
        available_tasks = []
        for task in tasks:
            to_do.append(
                Task(
                    task,
                    earliest_time=urgency[task]["earliest_time"],
                    ranking=urgency[task]["rank"],
                )
            )
            urgency[task]["earliest_time"] += n + 1
        del urgency
        heapq.heapify(to_do)
        time = 0
        while to_do or available_tasks:
            while to_do and time >= to_do[0].earliest_time:
                task = heapq.heappop(to_do)
                task.earliest_time = 0
                heapq.heappush(available_tasks, task)
            if available_tasks:
                task = heapq.heappop(available_tasks)
                # print(f"Did task {task.name} at time {time}")
            # else:
            #     print("Idling")
            time += 1
        return time

tasks = ["A","A","A","B","B","B"]
n = 2
print(Solution().leastInterval(tasks, n))

tasks = ["A","A","A","B","B","B"]
n = 0
print(Solution().leastInterval(tasks, n))

tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
n = 2
print(Solution().leastInterval(tasks, n))