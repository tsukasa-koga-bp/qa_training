from abc import ABC, abstractmethod

from qa_training.domain.ml_model import MLModel


class IF_RepoModel(ABC):
    """モデルリポジトリのインターフェースクラス.
    モデルの永続化を管理する.
    """

    @abstractmethod
    def load(self) -> MLModel:
        pass

    @abstractmethod
    def exist_model(self) -> bool:
        pass

    @abstractmethod
    def initialize(self) -> None:
        """リポジトリを初期化する"""
        pass
