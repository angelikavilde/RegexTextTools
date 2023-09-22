import re


EMAIL_REGEX = r"\w(?:[-\w+\.]*\w)?@\w[-\w\.]*\.[a-z]+"


def find_emails(text: str, starting_positions: bool=False, ending_positions: bool=False) -> list:
    """Returns email(s) within provided text or empty list if none are found"""
    if not starting_positions and not ending_positions:
        return re.findall(EMAIL_REGEX, text)
    email_objects = re.finditer(EMAIL_REGEX, text)
    if starting_positions and ending_positions:
        return list((match.start(), match.end() - 1) for match in email_objects if match)
    if starting_positions:
        return list(match.start() for match in email_objects if match)
    if ending_positions:
        return list(match.end() - 1 for match in email_objects if match)


def verify_email(text: str) -> bool:
    """Returns True/False depending on if the
    full text is correctly formatted email"""
    found_email = re.fullmatch(EMAIL_REGEX, text.strip())
    if found_email:
        return True
    return False


if __name__ == "__main__":
    pass