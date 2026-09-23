# Need plugin : pytest-order-------->pip install pytest-order
# Even though the order of the functions are different, it will follow based on specified order.
# Here, I have installed one more Plugin "pytest-ordering" --->pip install pytest-ordering

import pytest
@pytest.mark.run(order=4)
def test_1():
    print("This is test1 Tarani")
    assert True
@pytest.mark.run(order=3)
def test_2():
    print("This is test2 Krishna")
    assert True
@pytest.mark.run(order=1)
def test_3():
    print("This is test3 Lakshmi")
    assert True
@pytest.mark.run(order=2)
def test_4():
    print("This is test4 Sai")
    assert True
