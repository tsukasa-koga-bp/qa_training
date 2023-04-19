from typing import Any


def override(abstract_method: Any):
    """overrideしているメソッドを明示するwrapper関数. 抽象メソッドとメソッド名が異なる場合,

    Args:
        abstract_method: overrideしている抽象メソッド

    """

    def overrider(method: Any):
        assert method.__name__ == abstract_method.__name__
        return method

    return overrider
