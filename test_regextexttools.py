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
    assert verify_email(" t@test.tes")


def test_verify_email_incorrect_email():
    """Verifies that incorrect emails are identified"""
    assert not verify_email("test@test.2")
    assert not verify_email("test.@test.com")
    assert not verify_email(".2@test.com")
    assert not verify_email("test.testing+test@test")
    assert not verify_email("test_testing@test.test_test._")
    assert not verify_email("@")
    assert not verify_email(" s test@test.com")


def test_verify_email_errors():
    """Verifies that wrong data type raises an error"""
    incorrect_inputs = [[], dict(), None, set(), 1, True, (1,2), 1.1]
    for input in incorrect_inputs:
        with pytest.raises(AttributeError):
            verify_email(input)
    with pytest.raises(TypeError):
        verify_email(b'test')