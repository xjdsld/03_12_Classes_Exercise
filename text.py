pytest

from main import add

def test_add_positiv():
    assert add(3,5) == 8

def test_add_neg():
    assert add(-3,-5) == 8

pip install pytest
