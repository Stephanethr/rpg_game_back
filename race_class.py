class Race:
    """Race du joueur."""

    def __init__(self, name, stat):
        self._name = name
        self._stat = stat

    def __str__(self):
        return str(self._name)

