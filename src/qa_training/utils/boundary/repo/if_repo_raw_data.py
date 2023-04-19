from abc import ABC, abstractmethod


class IF_RepoRawData(ABC):
    """生データリポジトリのインターフェースクラス.
    生データの永続化を管理する.
    """

    @abstractmethod
    def initialize(self) -> None:
        """初期化"""
        pass
