class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m = len(matrix)
        n = len(matrix[0])

        l, r = 0, (m * n)

        while l < r:

            mid = (l + r)//2

            i, j = (mid//n), (mid%n)
            # i = how many full n's can I fit
            # j = how many past the last n I can fully fit

            print(mid, i, j, matrix[i][j])

            if matrix[i][j] < target:
                l = mid+1

            elif matrix[i][j] > target:
                r = mid

            else:
                return True

        return False
        