import re

street_regex = '[a-zA-Z\-]+\s[0-9a-z\-]*,\s[0-9]{4}\s[a-zA-z]*'
street_prog = re.compile(street_regex)


def is_address(street_string):
    return street_prog.search(street_string) is not None


def remove_white(str):
    return re.sub('\s+', ' ', str)
