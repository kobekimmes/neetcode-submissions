class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # create directed adj. list, mapping courses to prereqs 
        # representing the courses (prereqs) that must be taken 
        # before course is able to be taken
        g = {course: [] for course in range(numCourses)}
        for course, prereq in prerequisites:
            g[course].append(prereq)
        
        # attempt 1. (i think i have solved this before but regardless attempt 1.) dfs

        def attempt1():

            seen = set()

            def dfs(course):
                if course in seen:
                    return False

                if not g[course]:
                    return True

                seen.add(course)
                for prereq in g[course]:
                    if not dfs(prereq):
                        return False
                seen.remove(course)

                return True

            for i in range(numCourses):
                if not dfs(i):
                    return False
            return True

        # struggled with cylce detection -- TLE (38/78)
        # return attempt1()

        # attempt 2. memoize

        def attempt2():

            seen = set()
            cache = {}

            def dfs(course):
                if course in cache:
                    return cache[course]

                if course in seen:
                    return False

                if not g[course]:
                    return True

                can_take = True
                seen.add(course)

                for prereq in g[course]:
                    if not dfs(prereq):
                        can_take = False
                        break

                seen.remove(course)
                cache[course] = can_take

                return can_take

            for i in range(numCourses):
                if not dfs(i):
                    return False
            return True

        return attempt2()

            





            
            