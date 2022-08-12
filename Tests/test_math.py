import pytest
def test_add_f():
    assert 1 + 1 == 2

def test_two_value():
    a = 0
    b= 0
    c = 0
    assert a + b == c

def test_two_values_true():
    a = 2
    b= 3
    c = 5
    assert a + b == c

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1/0
    assert "division by zero" in str(e.value)

# In order to follow the DRY principle of not constantly repeating oneself
# We have to introduce the use of Parametrized test function.

products = [
    (2,3, 6),
    (-2, 4, -8),
    (1,99,99),
    (0,99, 0),
    (-8,-8, 64),
    (3,-4,-12)
]

@pytest.mark.parametrize("a,b, product", products)
def test_multiplication(a,b,product):
    assert a * b == product