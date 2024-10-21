# Solution 1
def DNA_strand_1(dna: str) -> str:
    """
    Given a DNA strand as a string, return its complementary strand.
    In a DNA sequence, "A" pairs with "T" and "C" pairs with "G".
    """
    return (
        dna.replace("A", "t")
        .replace("T", "A")
        .replace("C", "g")
        .replace("G", "C")
        .upper()
    )


# Solution 2
def DNA_strand_2(dna: str) -> str:
    """
    Given a DNA strand as a string, return its complementary strand.
    In a DNA sequence, "A" pairs with "T" and "C" pairs with "G".
    """
    return dna.translate(dna.maketrans("ATCG", "TAGC"))
