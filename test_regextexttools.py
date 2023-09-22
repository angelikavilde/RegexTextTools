import pytest

from regextexttools import find_emails, verify_email


def test_verify_email_correct_email():
    """Verifies that correct emails are identified"""
    assert verify_email("test@test.com")
    assert verify_email("test.2@test.com")
    assert verify_email("2.2@test.com")
    assert verify_email("test.testing+test@test.testing.test")
    assert verify_email("test_testing@test.test_test.lv")
    assert verify_email("     test@test.test    ")


def test_verify_email_errors():
    """Verifies that wrong data type raises an error"""
    incorrect_inputs = [[], dict(), None, set(), 1, True, (1,2), 1.1]
    for input in incorrect_inputs:
        with pytest.raises(AttributeError):
            verify_email(input)
    with pytest.raises(TypeError):
        verify_email(b'test')