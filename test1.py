import pytest

#Тесты с параметрами типа float

def float_division(a,b):
        return a/b

@pytest.mark.parametrize("a,b,result", [(2.5,0.5,5),(1.6, 2, 0.8),(10.6, 5, 2.12)])
def test_float_division(a,b,result):
        assert float_division(a,b)==result

def test_except_float_division():
        with pytest.raises(TypeError):
                float_division(4.2, "7.6") #Cделаем через assert

def test_except_float_division_without_raises():
        try:
                assert float_division(8.4, "4.2") == 2.0
        except:
                pass

def test ():
    assert 1/0
def test ():
    try:
        assert 1/0
    except ZeroDivisionError:
        pass