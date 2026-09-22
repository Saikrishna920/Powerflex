# Need plugin : pytest-order-------->pip install pytest-order
# Even though the order of the functions are different, it will follow based on specified order.
import pytest
@pytest.mark.order(4)
def test_1():
    print("This is test1")
    assert True
@pytest.mark.order(3)
def test_2():
    print("This is test2")
    assert True
@pytest.mark.order(1)
def test_3():
    print("This is test3")
    assert True
@pytest.mark.order(2)
def test_4():
    print("This is test4")
    assert True
