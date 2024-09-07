from src.PyQtPath.pyqt6_path import add_one


def test_add_one():
    n: int = add_one(3)
    assert n == 4
