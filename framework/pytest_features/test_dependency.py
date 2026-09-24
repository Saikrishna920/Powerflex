import pytest

class TestClass:
    @pytest.mark.dependency()
    def test_open_Application(self):
        assert True

    @pytest.mark.dependency(depends=["TestClass::test_open_Application"])
    def test_login_Application(self):
        assert True

    @pytest.mark.dependency(depends=["TestClass::test_login_Application"])
    def test_search_Application(self):
        assert True

    @pytest.mark.dependency(depends=["TestClass::test_login_Application"])
    def test_logout_Application(self):
        assert True

