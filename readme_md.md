# NumPy Data Analytics CLI

A menu-driven command-line interface (CLI) application built with Python and NumPy for creating, manipulating, transforming, and performing statistical operations on N-dimensional arrays.

---

## Features

- **Array Creation & Subsetting**
  - Create 1D, 2D, and 3D arrays with custom dimensions and data.
  - Multi-dimensional indexing support.
  - Slicing using standard Python slice notation (`start:end` or `start:end:step`).
- **Mathematical Operations**
  - Element-wise arithmetic: Addition, Subtraction, Multiplication, Division.
  - Linear algebra: Dot product and 2D Matrix multiplication (`np.matmul`).
- **Array Manipulation**
  - Stacking/combining arrays along vertical or horizontal axes.
  - Splitting arrays into equal/sub-sections along specified axes.
- **Search, Sort & Filter**
  - Search for values and return matching index tuples.
  - Sort arrays along chosen axes in ascending or descending order.
  - Dynamic condition-based filtering (e.g., `> 20`, `<= 5`).
- **Aggregates & Summary Statistics**
  - Sum, Mean, Median, Standard Deviation, and Variance.
  - Min/Max identification.
  - Arbitrary percentile calculation ($0 \le q \le 100$).
  - Pearson correlation coefficient between arrays.

---

## Requirements

- **Python**: 3.8 or higher
- **NumPy**: `numpy >= 1.20.0`

Install the required dependency:

```bash
pip install numpy
```

---

## Getting Started

Run the program directly from your terminal:

```bash
python Analyzer.py
```

---

## Usage Guide & Menu Options

When the script starts, you will be presented with the main menu:

```text
Welcome to the NumPy Analyzer!
==============================================

Choose an option:
1. Create a Numpy Array
2. Perform Mathematical Operations
3. Combine or Split Arrays
4. Search, Sort, or Filter Arrays
5. Compute Aggregates and Statistics
6. Exit
```

### 1. Create a NumPy Array
- **1D Array**: Provide the element count $n$ followed by $n$ space-separated values.
- **2D Array**: Provide row count $r$ and column count $c$, then supply $r \times c$ space-separated numbers.
- **3D Array**: Provide dimensions $d_1, d_2, d_3$, followed by $d_1 \times d_2 \times d_3$ numbers.
- After creation, you can immediately test **Indexing** (e.g., `0,1`) or **Slicing** (e.g., `0:2`).

### 2. Mathematical Operations
Requires an array to be created first. You will be prompted to enter a second array matching the dimensions of the primary array:
- `1`: Addition (`A + B`)
- `2`: Subtraction (`A - B`)
- `3`: Multiplication (`A * B`)
- `4`: Division (`A / B`)
- `5`: Matrix Multiplication (`A @ B` for 2D arrays) or Dot Product (`np.dot`)

### 3. Combine or Split Arrays
- **Combine**: Vertically stacks (`axis=0`) a secondary array of compatible shape with your current array.
- **Split**: Divides the array into $k$ sub-arrays along the primary axis using `np.array_split`.

### 4. Search, Sort, or Filter Arrays
- **Search**: Enter a target numerical value to receive coordinate indices where the value exists.
- **Sort**: Performs row-wise sort along axis `-1`.
- **Filter**: Enter an expression predicate relative to the elements, such as `> 10`, `% 2 == 0`, or `< 50`.

### 5. Aggregates and Statistics
Calculates statistical metrics over the entire dataset:
- Sum, Mean, Median, Std Dev, Variance, Min, Max, and arbitrary Percentiles.

---

## Class Architecture: `DataAnalytics`

The core logic is encapsulated within the `DataAnalytics` class in `Analyzer.py`:

| Method | Description |
| :--- | :--- |
| `data` (getter/setter) | Encapsulates the internal NumPy array (`__data`). |
| `index_element(indices)` | Accesses an item at a multi-index tuple. |
| `slice_array(slices)` | Slices the array across one or more dimensions. |
| `combine(other_array, axis=0)` | Stacks the array with another array using `np.vstack` or `np.hstack`. |
| `split(sections, axis=0)` | Splits array into multiple chunks using `np.array_split`. |
| `add`, `subtract`, `multiply`, `divide` | Element-wise vectorized arithmetic. |
| `dot_product`, `matrix_multiply` | Dot product and matrix multiplication routines. |
| `search_value(value)` | Locates values using `np.where`. |
| `sort_array(axis=-1, ascending=True)`| Sorts with optional axis flipping. |
| `filter_values(condition_str)` | Applies boolean mask derived from a condition string. |
| `get_sum`, `get_mean`, `get_median`, etc. | Statistical and reduction routines. |
| `parse_range(range_str)` | Static helper parsing string slices like `1:4` into `slice` objects. |

---

## License

This project is licensed under the MIT License - feel free to modify and use it in your own projects.