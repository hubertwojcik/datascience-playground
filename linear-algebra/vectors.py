from typing import List
import math 

Vector = List[float]

height_weight_age=[170,80,40]

grades=[95, 80, 75, 65]

def  add_vectors(v:Vector, w :Vector)->Vector:
    assert len(v) == len(w), "Vectors must have the same length"
    return [v_i + w_i for v_i, w_i in zip(v, w)]

def substract_vectors(v:Vector, w:Vector)->Vector:
    assert len(v) == len(w), "Vectors must have the same length"
    return [v_i - w_i for v_i,w_i in zip(v, w)]


def vector_sum(vectors:List[Vector]) -> Vector:
    assert vectors, "No vectors!"
    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors), "Different sizes"

    return [
        sum(vector[i] for vector in vectors)
        for i in range(num_elements)
    ]

assert vector_sum([[1,2],[3,4],[5,6],[7,8]])

def scalar_multiplty(c:float,v:Vector)->Vector:
    return [c * v_i  for v_i in v ]

def vector_mean(vectors:List[Vector])->Vector:
    n = len(vectors)
    return scalar_multiplty(1 / n, vector_sum(vectors))

def dot(v: Vector, w: Vector)->float:
    assert len(v) == len(w), "Different sizes"
    return sum(v_i * w_i for v_i, w_i in zip(v,  w))

def sum_of_squares(v: Vector) ->float:
    return dot(v,v)

def magnitude(v: Vector)->float:
    return math.sqrt(sum_of_squares(v))

def squared_distance(v: Vector, w: Vector)->float:
    return sum_of_squares(substract_vectors(v, w))

def distance(v: Vector, w: Vector)->float:
    return math.sqrt(squared_distance(v,w))