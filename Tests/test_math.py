import pytest
def test_add_f():
    assert 1 + 1 == 2

def test_two_value():
    a = 2
    b= 3
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