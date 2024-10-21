# Solution
def bingo(ticket: list, win: int) -> str:
    mini_wins = 0
    for sublist in ticket:
        if any(ord(char) == sublist[1] for char in sublist[0]):
            mini_wins += 1
    return "Winner!" if mini_wins >= win else "Loser!"
