
from typing import List
from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Find a valid course ordering using BFS (Kahn's Algorithm).
        
        Args:
            numCourses: Total number of courses (0 to numCourses-1)
            prerequisites: List of [course, prerequisite] pairs
            
        Returns:
            List representing a valid course order, or empty list if impossible
        """
        # Build adjacency list and calculate in-degrees
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        
        for course, prereq in prerequisites:
            graph[prereq].append(course)  # prereq -> course
            in_degree[course] += 1
        
        # Start with courses that have no prerequisites
        queue = deque([course for course in range(numCourses) if in_degree[course] == 0])
        result = []
        
        while queue:
            # Take a course with no remaining prerequisites
            current_course = queue.popleft()
            result.append(current_course)
            
            # Remove this course as a prerequisite for dependent courses
            for next_course in graph[current_course]:
                in_degree[next_course] -= 1
                # If next_course now has no prerequisites, it can be taken
                if in_degree[next_course] == 0:
                    queue.append(next_course)
        
        # If we've ordered all courses, return the result
        # Otherwise, there was a cycle and it's impossible
        return result if len(result) == numCourses else []


class SolutionDFS:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Find a valid course ordering using DFS with post-order traversal.
        
        The key insight: In DFS post-order, we add courses to result AFTER
        processing all their dependencies, which gives us reverse topological order.
        """
        # Build adjacency list
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[prereq].append(course)
        
        # Track visit states: 0=unvisited, 1=visiting, 2=visited
        state = [0] * numCourses
        result = []
        
        def dfs(course):
            """Returns False if cycle detected, True otherwise"""
            if state[course] == 1:  # Cycle detected
                return False
            if state[course] == 2:  # Already processed
                return True
            
            # Mark as visiting
            state[course] = 1
            
            # Process all dependent courses first
            for next_course in graph[course]:
                if not dfs(next_course):
                    return False
            
            # Mark as visited and add to result
            state[course] = 2
            result.append(course)  # Post-order: add after processing dependencies
            return True
        
        # Try DFS from each unvisited course
        for course in range(numCourses):
            if state[course] == 0:
                if not dfs(course):
                    return []  # Cycle detected
        
        # Result is in reverse topological order, so reverse it
        return result[::-1]