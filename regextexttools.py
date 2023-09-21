import re

def find_email(text: str, return_multiple: bool=True) -> str:
    """"""
    email_regex = r"((?:(?:[\w-]+)\.?)+@\b\w+(?:(?:[-\w]+)?\.[\w-]+)+[a-z]\b)"
    if return_multiple:
        return re.findall(email_regex, text)
    

if __name__ == "__main__":
    print(find_email("5an-g_ela.@gskinner-yes.hu.com. 77-hh@j.ac.uk some-text here.@j"))