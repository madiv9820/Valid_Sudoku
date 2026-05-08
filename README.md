# 🧩 Valid Sudoku
Sudoku is a classic **9 × 9 grid puzzle** where every number must follow strict placement rules.

In this problem, you are given a **partially filled Sudoku board**, and your task is to determine whether the current board is **valid** or **invalid**.

But here’s the important part:
```
✅ You only need to validate the cells that are already filled.
❌ You do not need to solve the Sudoku.
```

### 📌 Problem Statement
Given a 9 × 9 Sudoku board, determine whether the board is valid according to the following rules:

**✅ Rule 1: Rows Must Be Unique**

Each row must contain digits from **1 to 9** without repeating any digit.
```
["5", "3", ".", ".", "7", ".", ".", ".", "."]
```
The `.` represents an empty cell, so it is ignored during validation.

**✅ Rule 2: Columns Must Be Unique**

Each column must also contain digits from **1 to 9** without repetition.
```
Column Example:
5
6
.
8
4
7
.
.
.
```
If a digit appears more than once in the same column, the board is invalid.

**✅ Rule 3: Each 3 × 3 Box Must Be Unique**

The board is divided into **nine smaller 3 × 3 sub-boxes**.

Each sub-box must contain digits from **1 to 9** without repeating any digit.

Top-left 3 × 3 box:

5 3 .
6 . .
. 9 8

This box is valid because no filled digit appears more than once.

#### 🎯 Goal
Check whether the given Sudoku board is currently valid by carefully validating:
```
Rows + Columns + 3 × 3 Boxes
```
If all filled cells follow the rules, return **`true`**; otherwise, return **`false`**.

#### 📝 Important Notes
- Empty cells are represented by **`"."`**
- Empty cells should be ignored
- The board may be valid even if it cannot be solved
- You only need to check whether the current filled values follow Sudoku rules

### ✅ Example 1
#### Input
```
board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
```

#### Output
```
true
```

#### Explanation
Every filled digit follows all Sudoku rules:
- No duplicate digits in any row ✅
- No duplicate digits in any column ✅
- No duplicate digits in any 3 × 3 box ✅

So, the board is valid.

### ❌ Example 2
#### Input
```
board = [
    ["8","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
```

#### Output
```
false
```

#### Explanation
The board becomes invalid because the digit **`"8"`** appears more than once in the **top-left 3 × 3 sub-box**.
```
8 3 .
6 . .
. 9 8
```
Since a 3 × 3 box cannot contain duplicate digits, the board is invalid.

#### 📊 Constraints
- **`board.length == 9`**
- **`board[i].length == 9`**
- **`board[i][j]`** is a digit from **`"1"`** to **`"9"`** or **``**
---