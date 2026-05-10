from typing import List
from .approaches import Approaches

class Solution(Approaches):
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.approach_01_bruteForce(board) and self.approach_02_hashSet(board)