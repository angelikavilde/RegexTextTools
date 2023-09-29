""""""

import re


EMAIL_REGEX = r"\w(?:[-\w+\.]*\w)?@\w[-\w\.]*\.[a-z]+" # TODO [-\w\.] -> (?:\.[-\w])* ish to avoid ".."


def find_emails(text: str, starting_positions: bool=False, ending_positions: bool=False) -> list:
    """Returns email(s) within provided text or empty list if none are found""" # TODO not finished text
    if not starting_positions and not ending_positions:
        return re.findall(EMAIL_REGEX, text.lower())
    email_objects = filter(None, re.finditer(EMAIL_REGEX, text.lower()))
    if starting_positions and ending_positions:
        return list((match.start(), match.end() - 1) for match in email_objects)
    if starting_positions:
        return list(match.start() for match in email_objects)
    if ending_positions:
        return list(match.end() - 1 for match in email_objects)


def verify_email(text: str) -> bool:
    """Returns True/False depending on if the
    full text is correctly formatted email"""
    return bool(re.fullmatch(EMAIL_REGEX, text.strip()))


LINK_REGEX = r"(?:https?:\/\/(?:w{3}.)?|w{3}.)\w[-\w]+(?:\.\w+)+\S*"


def find_links(text: str, starting_positions: bool=False, ending_positions: bool=False, query=False) -> list:
    """"""
    # query=True returns links with /... or ?query=answer...
    if not starting_positions and not ending_positions:
        return re.findall(LINK_REGEX, text)
    pass


def verify_link(text: str) -> bool:
    """Returns True/False depending on if the
    full text is correctly formatted link"""
    return bool(re.fullmatch(LINK_REGEX, text.strip()))


def split_punctuation(text: str) -> list[str]:
    """Returns text split by stop punctuations"""
    split_text = re.split(r"[,\s;\.]+", text)
    return list(filter(None, split_text))


if __name__ == "__main__":
    a = """https://www.example/com    
https://www.example.com    
http://subdomain.example.co.uk   
https://regexr.com/   
https://www.example.com:8080/page   
http://www.example.com/path/with/slashes  
https://example.com?query=parameter 
https://sub.example.com/ 
https://docs.discord.red/en/latest/guide_slash_and_interactions.html 
https://www.example.com:8080/page#section 
https://www.example.co.uk.
https://www.example.co.uk   
http://subdomain.example.com/path?query=value#fragment"""

    print(find_links(a))
    print(split_punctuation("iuy"))