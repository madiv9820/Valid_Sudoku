# 🧠 This file exposes the LeetCode-facing `Solution` class.
# It delegates the Sudoku validation work to the reusable methods
# defined in `approaches.py`.

from typing import List
from .approaches import Approaches

class Solution(Approaches):
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.approach_01_bruteForce(board) and self.approach_02_hashSet(board)
