""""""

from pytest import raises

from regextexttools import find_emails, verify_email


class TestVerifyEmail:
    """Class that verifies that verify_email
    function works correctly"""
    def test_verify_email_correct_email(self):
        """Verifies that correct emails are identified"""
        assert verify_email("test@test.com")
        assert verify_email("test.2@test.com")
        assert verify_email("2.2@test.com")
        assert verify_email("test.testing+test@test.testing.test")
        assert verify_email("test_testing@test.test_test.lv")
        assert verify_email("     test@test.test    ")
        assert verify_email(" t@test.tes")


    def test_verify_email_incorrect_email(self):
        """Verifies that incorrect emails are identified"""
        assert not verify_email("test@test.2")
        assert not verify_email("test.@test.com")
        assert not verify_email(".2@test.com")
        assert not verify_email("test.testing+test@test")
        assert not verify_email("test_testing@test.test_test._")
        assert not verify_email("@")
        assert not verify_email(" s test@test.com")


    def test_verify_email_errors(self, incorrect_inputs):
        """Verifies that wrong data type raises an error"""
        for input in incorrect_inputs:
            with raises(AttributeError):
                verify_email(input)
        with raises(TypeError):
            verify_email(b'test')


class TestFindEmails:
    """Class that verifies that find_emails
    function works as expected"""
    # Since it uses the same regex as the verify_email,
    # no need to test the regex again
    def test_find_emails(self, email_text):
        """Verifies that correct emails are identified"""
        assert find_emails(email_text) == email_text.split(" ")[:-1]
        assert not find_emails(" ")


    def test_find_emails_starting_pos(self, email_text):
        """Verifies that starting positions of emails are identified"""
        assert find_emails(email_text, starting_positions=True) == [0, 16]
        assert not find_emails(" ", starting_positions=True)


    def test_find_emails_ending_pos(self, email_text):
        """Verifies that ending positions of emails are identified"""
        assert find_emails(email_text, ending_positions=True) == [14, 28]
        assert not find_emails(" ", ending_positions=True)


    def test_find_emails_ending_pos(self, email_text):
        """Verifies that starting and ending positions of emails are identified"""
        assert find_emails(email_text, ending_positions=True,
                           starting_positions=True) == [(0, 14), (16, 28)]
        assert not find_emails(" ", ending_positions=True, starting_positions=True)


    def test_find_emails_errors(self, incorrect_inputs):
        """Verifies that correct errors are raised with wrong input types"""
        for input in incorrect_inputs:
            with raises(AttributeError):
                find_emails(input)
                find_emails(input, starting_positions=True)
                find_emails(input, starting_positions=True, ending_positions=True)
                find_emails(input, ending_positions=True)
        input = b'test'
        with raises(TypeError):
            find_emails(input)
            find_emails(input, starting_positions=True)
            find_emails(input, starting_positions=True, ending_positions=True)
            find_emails(input, ending_positions=True)