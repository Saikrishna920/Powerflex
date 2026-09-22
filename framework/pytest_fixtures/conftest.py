import pytest
@pytest.fixture(scope="function")  # so, by default scope will take function
def setup():
    print("setting  the browser")
    #return "chrome"
    yield
    print("close the browser")



'''
Note: After executing the function, we need to close the browser, so in order to close
the browser instance, we can use yield keyword.
Execution order:
First controller, will execute the setup function (before the yield)------>excute the Test function
----->at last, excute the code after the yield.
'''