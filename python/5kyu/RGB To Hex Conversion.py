# Solution 1
def rgb_1(r: int, g: int, b: int) -> str:
    """
    Convert RGB decimal values to a hexadecimal representation.

    Each value must be in the range 0-255, rounding invalid values
    to the nearest valid number. The result should be a 6-character
    hexadecimal string.
    """
    hex_r, hex_g, hex_b = "", "", ""
    # fmt: off
    hex_conversion = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5',
                      6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B',
                      12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    # fmt: on

    if r <= 0:
        hex_r += "00"
    elif r >= 255:
        hex_r += "FF"
    else:
        hex_r = hex_conversion[r // 16] + hex_conversion[r % 16]

    if g <= 0:
        hex_g += "00"
    elif g >= 255:
        hex_g += "FF"
    else:
        hex_g = hex_conversion[g // 16] + hex_conversion[g % 16]

    if b <= 0:
        hex_b += "00"
    elif b >= 255:
        hex_b += "FF"
    else:
        hex_b = hex_conversion[b // 16] + hex_conversion[b % 16]

    return hex_r + hex_g + hex_b


# Solution 2
def rgb_2(r: int, g: int, b: int) -> str:
    """
    Convert RGB decimal values to a hexadecimal representation.

    Each value must be in the range 0-255, rounding invalid values
    to the nearest valid number. The result should be a 6-character
    hexadecimal string.
    """
    rgb_list, hex = [r, g, b], ""
    # fmt: off
    hex_conversion = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5',
                      6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B',
                      12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    # fmt: on

    for color in rgb_list:
        if color <= 0:
            hex += "00"
        elif color >= 255:
            hex += "FF"
        else:
            hex += hex_conversion[color // 16] + hex_conversion[color % 16]

    return hex


# Solution 3
def rgb_3(*args):
    """
    Convert RGB decimal values to a hexadecimal representation.

    Each value must be in the range 0-255, rounding invalid values
    to the nearest valid number. The result should be a 6-character
    hexadecimal string.
    """
    return "".join(map(lambda x: "{:02X}".format(min(max(0, x), 255)), args))


# Solution 4
def rgb_4(r: int, g: int, b: int) -> str:
    """
    Convert RGB decimal values to a hexadecimal representation.

    Each value must be in the range 0-255, rounding invalid values
    to the nearest valid number. The result should be a 6-character
    hexadecimal string.
    """
    return "".join(["%02X" % max(0, min(x, 255)) for x in [r, g, b]])
