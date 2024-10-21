# Solution 1
def score_1(dice: int) -> int:
    """
    Calculate the score of a throw in the Greed dice game based on the rules.

    Scoring rules:
    - Three of a kind yield points based on the die value:
      - Three 1's = 1000 points
      - Three 6's = 600 points
      - Three 5's = 500 points
      - Three 4's = 400 points
      - Three 3's = 300 points
      - Three 2's = 200 points
    - Additional points for single dice:
      - One 1 = 100 points
      - One 5 = 50 points

    Each die can only contribute to one score calculation per roll.
    For instance, a die showing "5" can either count as part of a triplet or
    as a single, not both.
    """
    points = 0

    if dice.count(1) == 6:
        points += 1300
    elif dice.count(1) == 5:
        points += 1200
    elif dice.count(1) == 4:
        points += 1100
    elif dice.count(1) == 3:
        points += 1000
    elif dice.count(1) == 2:
        points += 200
    elif dice.count(1) == 1:
        points += 100

    if dice.count(5) == 6:
        points += 650
    elif dice.count(5) == 5:
        points += 600
    elif dice.count(5) == 4:
        points += 550
    elif dice.count(5) == 3:
        points += 500
    elif dice.count(5) == 2:
        points += 100
    elif dice.count(5) == 1:
        points += 50

    if dice.count(6) >= 3:
        points += 600

    if dice.count(4) >= 3:
        points += 400

    if dice.count(3) >= 3:
        points += 300

    if dice.count(2) >= 3:
        points += 200

    return points


# Solution 2
def score_2(dice: int) -> int:
    """
    Calculate the score of a throw in the Greed dice game based on the rules.

    Scoring rules:
    - Three of a kind yield points based on the die value:
      - Three 1's = 1000 points
      - Three 6's = 600 points
      - Three 5's = 500 points
      - Three 4's = 400 points
      - Three 3's = 300 points
      - Three 2's = 200 points
    - Additional points for single dice:
      - One 1 = 100 points
      - One 5 = 50 points

    Each die can only contribute to one score calculation per roll.
    For instance, a die showing "5" can either count as part of a triplet or
    as a single, not both.
    """
    points, ones, fives = 0, dice.count(1), dice.count(5)

    if ones >= 3:
        points += 1000 + 100 * (ones - 3)
    else:
        points += 100 * ones

    if fives >= 3:
        points += 500 + 50 * (fives - 3)
    else:
        points += 50 * fives

    if dice.count(6) >= 3:
        points += 600
    if dice.count(4) >= 3:
        points += 400
    if dice.count(3) >= 3:
        points += 300
    if dice.count(2) >= 3:
        points += 200

    return points
