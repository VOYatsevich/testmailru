import pytest

#Тесты с параметрами типа float

def float_division(a,b):
        return a/b

@pytest.mark.parametrize("a,b,result", [(1.5,0.2,7.5),(2.5, 5, 0.5),(11.6,5,2.32)])
def test_float_division(a,b,result):
        assert float_division(a,b)==result

def test_except_float_division():
        with pytest.raises(TypeError):
                float_division(4.2, "7.6") #Cделаем через assert

def test_except_float_division_without_raises():
        try:
                assert float_division(6.2, "3.1") == 2.0
        except:
                pass

def test ():
    assert 1/0
def test ():
    try:
        assert 1/0
    except ZeroDivisionError:
        pass