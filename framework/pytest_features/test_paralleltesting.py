# Need plugin : pytest-xdist-------->pip install pytest-xdist
# cmd : pytest .\framework\pytest_features\test_paralleltesting.py -s -v -n 2
import pytest

def test_1():
    print("Running Test1")
    assert True

def test_2():
    print("Running Test2")
    assert True

def test_3():
    print("Running Test3")
    assert True

def test_4():
    print("Running Test4")
    assert True