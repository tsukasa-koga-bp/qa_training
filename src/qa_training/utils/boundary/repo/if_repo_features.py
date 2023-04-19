from abc import ABC, abstractmethod


class IF_RepoFeatures(ABC):
    """特徴量リポジトリのインターフェースクラス.
    特徴量の永続化を管理する.
    """

    @abstractmethod
    def initialize(self) -> None:
        """aaa"""
        pass
