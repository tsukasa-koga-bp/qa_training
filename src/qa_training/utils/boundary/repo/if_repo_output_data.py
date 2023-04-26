from abc import ABC, abstractmethod

import pandas as pd


class IF_RepoOutputData(ABC):
    """出力データのリポジトリのインターフェースクラス."""

    @abstractmethod
    def store(self, df_results: pd.DataFrame) -> None:
        pass

    @abstractmethod
    def exist_results(self) -> bool:
        pass

    @abstractmethod
    def initialize(self) -> None:
        """リポジトリを初期化する."""
        pass
