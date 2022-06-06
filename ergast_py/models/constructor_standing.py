""" ConstructorStanding class """

from dataclasses import dataclass

from ergast_py.models.constructor import Constructor


@dataclass
class ConstructorStanding():
    """
    Representation of a Formula One Constructor's standing in a Season

    Constructor Standings may contain:
        position: Integer
        position_text: String
        points: Float
        wins: Integer
        constructor: Constructor
    """

    def __init__(self, position: int, position_text: str, points: float, wins: int, #pylint: disable=too-many-arguments
                 constructor: Constructor) -> None:
        self.position = position
        self.position_text = position_text
        self.points = points
        self.wins = wins
        self.constructor = constructor

    def __repr__(self) -> str:
        members = ', '.join(f"{key}={value}" for key, value in self.__dict__.items())
        return f"{type(self).__name__}({members})"
