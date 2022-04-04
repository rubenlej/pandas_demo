import numpy as np
from sklearn.metrics import mean_squared_error
import math

def add(a: int, b: int) -> int:
    """Adds two numbers together"""
    return a + b


def calculate_rmse(predictions, targets):
    return np.sqrt(((predictions - targets) ** 2).mean())


def change_delimiter(line, original_delimiter, replacement_delimiter):
    return line.replace(original_delimiter, replacement_delimiter)


def test_add():
    a = 5
    b = 7
    expected = 12
    assert expected == add(a, b)


def test_change_delimiter():
    line = "Mario; Cynthia; Ruben; Charlotte; Louis"
    expected = "Mario, Cynthia, Ruben, Charlotte, Louis"
    assert expected == change_delimiter(line, ";", ",")


def test_rmse():
    actual = np.array([0, 1, 2, 0, 3])
    predicted = np.array([0.1, 1.3, 2.1, 0.5, 3.1])
    assert math.sqrt(mean_squared_error(actual, predicted)) == calculate_rmse(actual, predicted)
