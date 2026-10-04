class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # create directed adj. list, mapping courses to prereqs 
        # representing the courses (prereqs) that must be taken 
        # before course is able to be taken
        g = {course: [] for course in range(numCourses)}
        for course, prereq in prerequisites:
            g[course].append(prereq)

        print(g)
        
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

        # attempt 2. memoize -- accepted

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

        # return attempt2()

        # attempt 3. topological sort/kahns algorithm -- TLE BUT 78/78 test cases passed ????

        def attempt3():

            reqs = {course: set(g[course]) for course in g}
            q = [course for course in g if not g[course]]

            print(q)

            can_take = [False for _ in range(numCourses)]

            while q:

                curr = q[0]
                q = q[1:]

                can_take[curr] = True

                for course in reqs:
                    prereqs = reqs[course]
                    if curr in prereqs:
                        prereqs.remove(curr)

                        if not prereqs:
                            q.append(course)

            return all(can_take)

        # return attempt3()

        # attempt 4. fix deps logic

        def attempt4():
            deps = [0 for _ in range(numCourses)]
            reqs = {i: [] for i in range(numCourses)}
            for prereq, course in prerequisites:
                reqs[prereq].append(course)
                deps[course] += 1

            q = [i for i in range(numCourses) if deps[i] == 0]

            can_take = 0

            while q:

                curr = q[0]
                q = q[1:]

                can_take += 1
                for prereq in reqs[curr]:
                    deps[prereq] -= 1
                    if deps[prereq] == 0:
                        q.append(prereq)
                    
            return can_take == numCourses

        return attempt4()



            





            
            