# Solution
class Automaton:
    """
    A finite automaton with three states: q1 (start), q2 (accept),
    and q3. It processes commands from {0, 1} and transitions as follows:
    - q1 moves to q2 on '1', stays on '0'.
    - q2 moves to q3 on '0', stays on '1'.
    - q3 moves to q2 on '0' or '1'.
    The automaton returns True if it ends in state q2, otherwise returns False.
    """

    _transitions = {
        "q10": "q1",
        "q11": "q2",
        "q20": "q3",
        "q21": "q2",
        "q30": "q2",
        "q31": "q2",
    }

    def __init__(self):
        self.state = "q1"
        self.final_state = "q2"

    def read_commands(self, commands):
        for cmd in commands:
            self.state = self._transitions[self.state + cmd]
        return self.state == self.final_state


my_automaton = Automaton()
