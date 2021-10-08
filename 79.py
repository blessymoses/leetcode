"""
Word Search
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
"""


# class Solution:
#     dx = [0, 0, -1, 1]
#     dy = [1, -1, 0, 0]

#     def solution(self, board, word, x, y, cur):
#         if (
#             x < 0
#             or x >= len(board)
#             or y < 0
#             or y >= len(board[x])
#             or board[x][y] == " "
#         ):
#             return False
#         cur += board[x][y]
#         if len(cur) > len(word):
#             return False
#         if cur[len(cur) - 1] != word[len(cur) - 1]:
#             return False
#         if cur == word:
#             return True

#         temp = board[x][y]
#         board[x][y] = " "

#         for i in range(4):
#             if self.solution(board, word, self.dx[i], self.dy[i], cur):
#                 return True

#         board[x][y] = temp
#         return False

#     def exist(self, board: List[List[str]], word: str) -> bool:
#         if not word:
#             return True
#         for i in range(len(board)):
#             for j in range(board[i]):
#                 if word[0] == board[i][j] and self.solution(board, word, i, j, ""):
#                     return True
#         return False
