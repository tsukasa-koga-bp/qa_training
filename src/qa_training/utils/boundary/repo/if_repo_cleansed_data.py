from abc import ABC, abstractmethod


class IF_RepoCleansedData(ABC):
    """整形データリポジトリのインターフェースクラス.
    整形データの永続化を管理する.
    """

    @abstractmethod
    def gene(self) -> None:
        """aaa"""
        pass
