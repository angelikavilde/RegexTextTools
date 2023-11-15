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


@fixture
def long_text_for_tests():
    """Returns a long story string"""
    return """In a serene, sunlit meadow, 
    Sarah savored the fragrant roses blooming in rows. 
    As she strolled, a gentle breeze rustled through 
    the colorful petals. The tranquil spell was broken when,
    suddenly, Sarah spotted a mischievous squirrel scampering
    up a tall oak. Enchanted, she marveled at nature's whimsical
    ballet, feeling truly spellbound."""