## 🧠 Approach 1: Brute Force Scan

### 🎯 Goal

For every filled cell, verify that the same digit does not appear again in:

- the current row
- the current column
- the current `3 x 3` box

If any duplicate is found, the Sudoku board is invalid.

### 💡 Intuition

This approach directly follows the Sudoku rules.

Instead of storing previously seen values, we inspect the board around each filled cell and confirm that the digit is unique in all three required directions.

It is the most straightforward way to translate the problem statement into code.

### 🪜 Pseudocode

```text
for each row in board:
    for each col in board:
        if board[row][col] is empty:
            continue

        value = board[row][col]

        scan the current row
        if value appears elsewhere:
            return false

        scan the current column
        if value appears elsewhere:
            return false

        scan the current 3 x 3 box
        if value appears elsewhere:
            return false

return true
```

### 🔍 Step-by-Step Explanation

1. Traverse every cell in the board.
2. Skip empty cells represented by `"."`.
3. For each filled cell:
   - check the full row
   - check the full column
   - check the `3 x 3` box it belongs to
4. If any check finds the same digit again, return `false`.
5. If the whole board is processed without conflicts, return `true`.

### ✅ Why It Works

Sudoku validity depends on three rules only:

- no duplicate in a row
- no duplicate in a column
- no duplicate in a `3 x 3` box

This method explicitly validates all three rules for each filled cell, so any invalid placement is caught immediately.

### ⏱️ Time Complexity

`O(9 * 9 * 9)`

Why:

- there are `81` cells
- each filled cell can trigger up to `9` row checks
- `9` column checks
- and `9` box checks

For a fixed `9 x 9` Sudoku board, this is still constant overall, but the repeated scanning makes it less efficient than the hash-set method.

### 💾 Space Complexity

`O(1)`

Why:

- no extra data structure grows with the board
- only helper variables and loop counters are used


### ✅ Pros

- Very easy to understand
- Mirrors Sudoku rules directly
- Good for beginners and debugging

### ⚠️ Cons

- Repeats the same scanning work many times
- Less elegant than a tracking-based solution
