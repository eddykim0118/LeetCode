class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {course: [] for course in range(numCourses)}
        indegree = [0]*numCourses
        for prereq in prerequisites:
            graph[prereq[1]].append(prereq[0])
            indegree[prereq[0]] += 1
        queue = []
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)
        ans = []
        while queue != []:
            course = queue.pop(0)
            ans.append(course)
            for node in graph[course]:
                indegree[node] -= 1
                if indegree[node] == 0:
                    queue.append(node)
        if len(ans) == numCourses:
            return ans
        else:
            return []