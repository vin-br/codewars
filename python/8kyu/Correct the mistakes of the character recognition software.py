# Solution
def correct(s: str) -> str:
    """
    Corrects common OCR errors in digitized text:
    - '5' is corrected to 'S'
    - '0' is corrected to 'O'
    - '1' is corrected to 'I'
    The input contains only digits that are misinterpreted.
    """
    modified = s.replace("5", "S").replace("0", "O").replace("1", "I")
    return modified
