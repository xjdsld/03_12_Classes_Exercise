from main import calc

def test_zero_divisions():
  assert calc(10, '/', 2) == 5

def test_division():
  assert calc(20, '/', 5) == 4

def test_squaring():
  assert calc(2, '^', 2) == 4