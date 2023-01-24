"""
Use pytest to do python tests instead of using unittest
https://www.tutorialspoint.com/pytest/index.htm

Note: pytest requires:
    1. Test files have to have format test_*.py or *_test.py in the current directory and subdirectories.
    2. test function names have to start with test, like testSomething() or test_something.

To run the tests in terminal, first, activate the virtual env. Here, simply type "poetry shell". Poetry
will activate the virtual env it has created in ~/Library/Caches/pypoetry/virtualenvs/pythonproject-xyz...

To run the tests with pytest, simply type "pytest"  or "pytest -v" (for verbose output) in the same dir.
pytest will search for all tests in the same dir and sub-dirs.
    1. pytest -> run all tests in current dir and sub-dirs
    2. pytest -k sqrt -v  -> run all tests that have "sqrt" in their names, make verbose output
"""

import math

def test_sqrt():
    """
    Simply use assert for testing. Pytest will detect and make nice output for tests.
    """
    assert math.sqrt(25) == 5

def testSquare():
    assert 2*2 == 4

def test_failure():
    # assert 2 == 3
    pass

"""
See this for info related to marks: https://docs.pytest.org/en/stable/how-to/mark.html
"""
import pytest

@pytest.mark.skip # this test is skipped
def test_something1():
    assert 1 < 2

@pytest.fixture
def some_setup():
    print("some setup before a test") # I don't see this gets printed, but it does execute. Simply change to 1 == 2 and see it will fail.
    assert 2 == 2

#@pytest.mark.usefixtures("some_setup")
def test_fixture():
    print("this causes the fixture to execute before this test")
    assert 2 == 2

# Test for raising exceptions.
# See here for more: https://docs.pytest.org/en/stable/reference/reference.html#pytest.raises
def test_passes():
    with pytest.raises(Exception) as e_info:
        x = 1 / 0

def test_passes_without_info():
    with pytest.raises(Exception):
        x = 1 / 0

def test_fails():
    with pytest.raises(Exception) as e_info:
        x = 1 / 1

def test_fails_without_info():
    with pytest.raises(Exception):
        x = 1 / 1