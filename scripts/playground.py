# -*- coding: utf-8 -*-
# @File    : playground.py
# @Author  : Hua Guo
# @Time    : 2020/4/25 下午4:15
# @Disc    :
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        # for idx in range(matrix[0]):
        #     if matrix[0][idx] == 1:
        #         dp[0][idx] = 1
        #     else:
        #         dp[0][idx] = 0
        # for idx in range(len(matrix)):
        #     if matrix[idx][0] == 1:
        #         dp[idx][0] = 1
        #     else:
        #         dp[idx][0] = 0
        max_value = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                dp[row][col] = int(matrix[row][col])
                if matrix[row][col] and row and col:
                    dp[row][col] = min([dp[row - 1][col - 1], dp[row - 1][col], dp[row][col - 1]]) + 1
                max_value = max(max_value, dp[row][col])
        print(dp)
        print(max_value)
        return max_value ** 2


a = "ezupkr"
b = "ubmrapg"

result = Solution().longestCommonSubsequence(a, b)
print(result)
