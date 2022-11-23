# Solution 1
import re

def to_camel_case(text):
    modified_text = re.sub('[-]', '_', text).split('_')
    return modified_text[0] + "".join(i.capitalize() for i in modified_text[1:])

# Solution 2
def to_camel_case(text):
    return text[:1] + text.title()[1:].replace('_', '').replace('-', '')