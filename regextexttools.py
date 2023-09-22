import re


EMAIL_REGEX = r"\w(?:[-\w+\.]*\w)?@\w[-\w\.]*\.[a-z]+"


def find_emails(text: str, starting_positions: bool=False, ending_positions: bool=False) -> list:
    """"""
    # empty list if no found
    all_emails = re.findall(EMAIL_REGEX, text)
    # return all_emails
    if not starting_positions and not ending_positions:
        return all_emails
    emails_starting_positions = re.finditer(EMAIL_REGEX, text)
    if starting_positions and not ending_positions:
        return list(match.start() for match in emails_starting_positions if match)
    if ending_positions and not starting_positions:
        return list(match.end() - 1 for match in emails_starting_positions if match)
    if starting_positions and ending_positions:
        return list((match.start(), match.end() - 1) for match in emails_starting_positions if match)


def verify_email(text: str) -> bool:
    """"""
    found_email = re.fullmatch(EMAIL_REGEX, text)
    if found_email:
        return True
    return False


if __name__ == "__main__":
    text = "5an-g_ela@gskinner-yes.hu.com. 77-hh@j.ac.uk some-text here@j.ru"
    # text = None
    print(find_emails(text, starting_positions=True, ending_positions=True))
    print(verify_email("5an-g_ela@gskinner-yes.hu.com"))