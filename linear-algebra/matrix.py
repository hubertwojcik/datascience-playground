from typing import List, Tuple, Callable

Vector=List[float]
Matrix = List[List[float]]

A = [[1, 2, 3],
     [4, 5, 6]]

B = [[1, 2],
     [3, 4],
     [5, 6]]

def shape(A: Matrix)-> Tuple[int, int]:
    num_rows = len(A)
    num_cols = len(A[0] if A else 0)
    return num_rows, num_cols

def get_row(A: Matrix, i: int)-> Vector:
    return A[i]

def get_column(A: Matrix, j: int)-> Vector:
    return [A_i[j]
            for A_i in A]

def make_matrix(num_rows: int, 
                num_cols: int,
                entry_fn: Callable[[int,int],float]
                )->Matrix:
    return [[entry_fn(i, j)
              for j in num_cols]
                for i in num_rows]

def identity_matrix(n: int)-> Matrix:
    return make_matrix(n, n, lambda i, j:1 if i == j else 0)