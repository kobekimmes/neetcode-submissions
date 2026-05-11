class Solution:
    def hammingWeight(self, n: int) -> int:
        


        # def d_and_c(n, chunk):
        #     print(n, chunk)

        #     if n == 0:
        #         return 0
        #     if chunk >= 32:
        #         return n == 1

        #     l = r = 0xFFFFFFFF >> chunk

        #     l &= (n >> chunk)
        #     r &= n

        #     return d_and_c(l, chunk + chunk // 2) + d_and_c(r, chunk + chunk // 2)

        # return d_and_c(n, 16)
        iters = 0
        while n > 0:

            iters += 1
            n &= (n-1)
            n >> 1

        return iters
