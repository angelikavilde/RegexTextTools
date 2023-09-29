"""File containing fixtures for tests"""

from pytest import fixture


@fixture
def email_text():
    """Returns test string with 2 emails"""
    return "test.2@test.com test@test.com @test.test"


@fixture
def incorrect_inputs():
    """Returns a list of non string data types"""
    return [[], dict(), None, set(), 1, True, (1,2), 1.1]