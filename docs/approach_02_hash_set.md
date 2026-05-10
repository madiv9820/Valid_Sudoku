## 📦 Approach 2: Hash Set Tracking

### 🎯 Goal

Traverse the board once and track which digits have already appeared in:

- each row
- each column
- each `3 x 3` box

If a digit is seen again in any of those groups, the board is invalid.

### 💡 Intuition

Instead of repeatedly scanning the board around each filled cell, we remember what we have already seen.

That means every new filled cell can be validated in constant time using set membership checks.

This approach trades a little extra memory for cleaner and faster validation logic.

### 🪜 Pseudocode

```text
create 9 row sets
create 9 column sets
create 9 box sets

for each row in board:
    for each col in board:
        value = board[row][col]

        if value is empty:
            continue

        box_index = (row // 3) * 3 + (col // 3)

        if value already exists in row_sets[row]:
            return false

        if value already exists in column_sets[col]:
            return false

        if value already exists in box_sets[box_index]:
            return false

        add value to row_sets[row]
        add value to column_sets[col]
        add value to box_sets[box_index]

return true
```

### 🔍 Step-by-Step Explanation

1. Create three collections of sets:
   - `rows`
   - `columns`
   - `boxes`
2. Traverse every cell in the board once.
3. Skip empty cells represented by `"."`.
4. Compute the `3 x 3` box index using:
   `box_index = (row // 3) * 3 + (col // 3)`
5. Before inserting the digit, check whether it already exists in:
   - the row set
   - the column set
   - the box set
6. If it exists anywhere, return `false`.
7. Otherwise, record it in all three sets.
8. If traversal finishes without duplicates, return `true`.

### ✅ Why It Works

Each set stores the digits that have already appeared in a particular row, column, or box.

If a duplicate appears, one of those sets will already contain the value, which immediately proves the board is invalid.

If no duplicate is found by the end, then all Sudoku constraints are satisfied.

### ⏱️ Time Complexity

`O(9 * 9)`

Why:

- each cell is visited once
- each set lookup and insertion is `O(1)` on average

For a fixed `9 x 9` Sudoku board, this is constant overall and more efficient than re-scanning around each cell.

### 💾 Space Complexity

`O(9 * 9)`

Why:

- extra sets are used to store seen digits
- in practice the total stored values are bounded by the fixed board size

For this specific problem size, it also simplifies to `O(1)` in the strict constant-size sense.

### ✅ Pros

- Cleaner validation flow
- Avoids repeated scans
- More efficient in practice

### ⚠️ Cons

- Uses extra memory
- Slightly more abstract than the brute-force solution
