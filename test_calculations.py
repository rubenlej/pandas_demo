def add(a: int, b: int) -> int:
    """Adds two numbers together"""
    return a + b


def test_add():
    a = 5
    b = 7
    expected = 12
    assert expected == add(a, b)
