import pytest


def test_Loginbymail():
    print("This is loginbymail")
    assert True


def test_Loginbyfacebook():
    print("This is loginbyfacebook")
    assert True

@pytest.mark.skip
def test_Loginbytwitter():
    print("This is loginbytwitter")
    assert True

@pytest.mark.skip
def test_Loginbygoogle():
    print("This is loginbygoogle")
    assert True

@pytest.mark.skip
def test_Loginbyyoutube():
    print("This is loginbyyoutube")
    assert True


def test_singupbymail():
    print("This is singupbymail")
    assert True


def test_singupfacebook():
    print("This is singupfacebook")
    assert True

@pytest.mark.skip
def test_singuptwitter():
    print("This is singuptwitter")
    assert True

@pytest.mark.skip
def test_singupgoogle():
    print("This is singupgoogle")
    assert True

@pytest.mark.skip
def test_singupyoutube():
    print("This is singupyoutube")
    assert True
