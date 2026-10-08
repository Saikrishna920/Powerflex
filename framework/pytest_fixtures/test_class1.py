import pytest

@pytest.mark.usefixtures('setup')
def test_1():
    print("This is test1")
    assert True

def test_2(setup):
    print("This is test2")
    assert True

def test_3():
    print("This is test3")
    assert True

def test_4():
    print("This is test4")
    assert True
