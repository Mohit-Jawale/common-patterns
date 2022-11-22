from functools import lru_cache
class Solution:
    def numSquares(self, n: int) -> int:
        perfect_square = []

        for i in range(1,n+1):
            if i*i<=n+1:
                perfect_square.append(i*i)
            else:
                break

        @lru_cache(None)
        def least_perfect_square_sum(n):
            if n==0:
                return 0

            possible_sums = 999999999

            for i in perfect_square:
                if i<=n:
                    possible_sums = min(possible_sums,least_perfect_square_sum(n-i))
                else:
                    break

            return (possible_sums) + 1 
                      

        return least_perfect_square_sum(n)
