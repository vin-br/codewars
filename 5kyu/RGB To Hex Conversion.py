"""Description:

The rgb function is incomplete. 
Complete it so that passing in RGB decimal values will result in 
a hexadecimal representation being returned. 
Valid decimal values for RGB are 0 - 255. 
Any values that fall out of that range must be rounded to the closest valid value.

Note: 
Your answer should always be 6 characters long, the shorthand with 3 will not work here.

The following are examples of expected output values:

rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3
"""

# Solution 1
def rgb(r, g, b):
    hex_r, hex_g, hex_b = "", "", ""
    hex_conversion = {
        0: "0",
        1: "1",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        10: "A",
        11: "B",
        12: "C",
        13: "D",
        14: "E",
        15: "F",
    }

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
def rgb(r, g, b):
    rgb_list, hex = [r, g, b], ""
    hex_conversion = {
        0: "0",
        1: "1",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        10: "A",
        11: "B",
        12: "C",
        13: "D",
        14: "E",
        15: "F",
    }

    for color in rgb_list:
        if color <= 0:
            hex += "00"
        elif color >= 255:
            hex += "FF"
        else:
            hex += hex_conversion[color // 16] + hex_conversion[color % 16]

    return hex


# Solution 3
def rgb(*args):
    return "".join(map(lambda x: "{:02X}".format(min(max(0, x), 255)), args))


# Solution 4
def rgb(r, g, b):
    return "".join(["%02X" % max(0, min(x, 255)) for x in [r, g, b]])
