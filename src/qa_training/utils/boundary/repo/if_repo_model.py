from abc import ABC, abstractmethod


class IF_RepoModel(ABC):
    """モデルリポジトリのインターフェースクラス.
    モデルの永続化を管理する.
    """

    @abstractmethod
    def initialize(self) -> None:
        """リポジトリを初期化する"""
        pass
