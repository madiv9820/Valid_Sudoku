# 🧩 This file stores the actual Sudoku-validation strategies.
# Each method here implements a different way to check whether the
# board follows the row, column, and 3x3-box rules.

from typing import List, Set

class Approaches:
    def approach_01_bruteForce(self, board: List[List[str]]) -> bool:
        # 🔍 Scan the current row and make sure this value does not
        # appear anywhere else in the same horizontal line.
        def checkRow(row: int, col: int, val: str) -> bool:
            for i in range(9):
                if i == col:
                    continue
                if board[row][i] == val:
                    return False
            return True

        # 📏 Do the same check for the vertical column.
        def checkCol(row: int, col: int, val: str) -> bool:
            for i in range(9):
                if i == row:
                    continue
                if board[i][col] == val:
                    return False
            return True

        # 🧩 Every cell also belongs to a 3x3 box, so we locate that box
        # and confirm the value is unique inside it too.
        def checkBox(row: int, col: int, val: str) -> bool:
            startRow: int = row // 3
            startCol: int = col // 3

            for i in range(startRow * 3, startRow * 3 + 3):
                for j in range(startCol * 3, startCol * 3 + 3):
                    if i == row and j == col:
                        continue
                    if board[i][j] == val:
                        return False
            return True

        # 🚦 Walk through the full board.
        # Empty cells `.` are ignored, but every filled cell must pass
        # the row, column, and box checks to keep the Sudoku valid.
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if (
                        not checkRow(i, j, board[i][j])
                    or  not checkCol(i, j, board[i][j])
                    or  not checkBox(i, j, board[i][j])
                ):
                    return False

        # ✅ If no rule was broken, the board is valid.
        return True
    
    def approach_02_hashSet(self, board: List[List[str]]) -> bool:
        # 📦 Each row will have its own set to track seen digits
        rows: List[Set[str]] = [set() for _ in range(9)]

        # 📦 Each column will have its own set to track seen digits
        columns: List[Set[str]] = [set() for _ in range(9)]

        # 📦 Each 3x3 box will have its own set to track seen digits
        boxes: List[Set[str]] = [set() for _ in range(9)]

        # 🚦 Traverse every cell in the 9x9 Sudoku board
        for row in range(9):
            for col in range(9):

                current_Value: str = board[row][col]

                # ⏭️ Empty cells are ignored
                if current_Value == ".":
                    continue

                # 🧩 Calculate which 3x3 box this cell belongs to
                # Formula maps each box into an index from 0 to 8
                box_Index: int = (row // 3) * 3 + (col // 3)

                # ❌ If digit already exists in the same row, board is invalid
                if current_Value in rows[row]:
                    return False

                # ❌ If digit already exists in the same column, board is invalid
                if current_Value in columns[col]:
                    return False

                # ❌ If digit already exists in the same 3x3 box, board is invalid
                if current_Value in boxes[box_Index]:
                    return False

                # ✅ Mark this digit as seen in its row, column, and box
                rows[row].add(current_Value)
                columns[col].add(current_Value)
                boxes[box_Index].add(current_Value)

        # ✅ If no duplicate was found, the Sudoku board is valid
        return True
