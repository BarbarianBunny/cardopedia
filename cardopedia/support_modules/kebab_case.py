import re


def kebab_case(text):
    return re.sub(r"[-_ :&?]+", "-", text.lower())