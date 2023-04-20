from typing import NamedTuple


class CustomerInfo(NamedTuple):
    """乗員情報"""

    PassengerId: int
    Survived: int
    Pclass: int
    Name: str
    Sex: str
    Age: int
    SibSp: int
    Parch: int
    Ticket: str
    Fare: float
    Cabin: str
    Embarked: str
