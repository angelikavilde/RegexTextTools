""""""

import re


EMAIL_REGEX = r"\w(?:[-\w+\.]*\w)?@\w[-\w\.]*\.[a-z]+"


def find_emails(text: str, starting_positions: bool=False, ending_positions: bool=False) -> list:
    """Returns email(s) within provided text or empty list if none are found;
    also returns starting or/and ending positions for the found items"""
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
x = r"(?:https?:\/\/|w{3}\.)\w[-\w]+(?:\.\w+)*\.[a-z]+\S+|https?:\/\/w{3}\.\w[-\w]+(?:\.\w+)*\.[a-z]+"


def find_links(text: str, starting_positions: bool=False, ending_positions: bool=False, query=False) -> list:
    """Returns link(s) within provided text or empty list if none are found;
    also returns starting or/and ending positions for the found items"""
    # query=True returns links with /... or ?query=answer... {when added - upd above}
    if not starting_positions and not ending_positions:
        return re.findall(LINK_REGEX, text)
    link_objects = filter(None, re.finditer(LINK_REGEX, text.lower()))
    if starting_positions and ending_positions:
        return list((match.start(), match.end() - 1) for match in link_objects)
    if starting_positions:
        return list(match.start() for match in link_objects)
    if ending_positions:
        return list(match.end() - 1 for match in link_objects)


def verify_link(text: str) -> bool:
    """Returns True/False depending on if the
    full text is correctly formatted link"""
    return bool(re.fullmatch(LINK_REGEX, text.strip()))


def split_punctuation(text: str) -> list[str]:
    """Returns text split by stop punctuations"""
    split_text = re.split(r"[\,\s\;\.\\\?\!\:]+", text)
    return list(filter(None, split_text))


def ends_with(text: str, e_with: str) -> list:
    """Similar to 'endswith' but finds everything
    in text and quickly"""
    ends_with_regex = r"[^\W_]*" + e_with + r"(?=[,\s;\.\\])"
    return re.findall(ends_with_regex, text + " ")


def starts_with(text: str, s_with: str) -> list:
    """Similar to 'startswith' but finds everything
    in text and quickly"""
    starts_with_regex = r"(?<=[,\s;\.\\])" + s_with + r"[^\W_]*"
    return re.findall(starts_with_regex, " " + text)


def validate_phone_number(text: str, prefix: str, length_range: tuple) -> bool:
    """Validates if the phone number is correct where length
    range accounts for only the number outside of the prefix length
    and the prefix can include the starting digit of the number"""
    phone_number_regex = str(prefix) + r"[\d]" + str(
            {length_range[0],length_range[1]}).replace(" ", "")
    return bool(re.fullmatch(phone_number_regex, text.strip()))


if __name__ == "__main__":
#     a = """https://www.example/com    
# https://www.example.com    
# http://subdomain.example.co.uk   
# https://regexr.com/   
# https://www.example.com:8080/page   
# http://www.example.com/path/with/slashes  
# https://example.com?query=parameter 
# https://sub.example.com/ 
# https://docs.discord.red/en/latest/guide_slash_and_interactions.html 
# https://www.example.com:8080/page#section 
# https://www.example.co.uk.
# https://www.example.co.uk   
# http://subdomain.example.com/path?query=value#fragment"""
    string = '07473703539'
    # print(validate_text(string),string)
    # pass
    print(validate_phone_number(string, 0, (10,11)))