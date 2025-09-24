from collections import deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # numCourses = number of courses you have to take (labeled from 0 to numCourses - 1)
        # prerequisites = (array)
        #   prerequisites[i] = [a, b] <- b must be taken before a
        # return: the ordering of courses you should take to finish all courses (all numCourses)
        #         if there are many valid answers, return any of them (in other words, return just one)
        #         if it is not possible to finish, return an empty arrya (in other words, return [])

        # From example inputs,
        # if numCourses = 4, then the course number is going to be from 0 to 3 ([0..3])
        # Since courses are put as numbers, I think we can simply use that as a marker/keys => let's use list instead of dictionary

        # What algorithms should we use?
        #   This sounds like a DAG + ordering problem. Why? b/c "b must be taken before a"
        #   We want an ordering that respects all edges => Topological Sort
        #   Kahn's Algorithm? (BFS with indegree tracking)
        #       then I would need graph, indegree, queue of "ready" nodes, and an array for output

        course_graph = [[] for _ in range(numCourses)]
        prereq_count = [0] * numCourses

        for a, b in prerequisites:
            # prerequisites example: [[1,0], [2,0], [3,1], [3,2]]
            course_graph[b].append(a)
            # prereq_count: [0, 0, 0, 0]
            prereq_count[a] += 1

        pre_q = []
        for i in range(numCourses):
            if prereq_count[i] == 0:
                pre_q.append(i)

        q_ready = deque(pre_q)
        course_order = []

        while q_ready:
            course = q_ready.popleft()
            course_order.append(course)

            for next_course in course_graph[course]:
                prereq_count[next_course] -= 1
                if prereq_count[next_course] == 0:
                    q_ready.append(next_course)

        return course_order if len(course_order) == numCourses else []
