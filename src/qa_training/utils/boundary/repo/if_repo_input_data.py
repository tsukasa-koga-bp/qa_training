from abc import ABC, abstractmethod

import pandas as pd


class IF_RepoInputData(ABC):
    """入力データのリポジトリのインターフェースクラス."""

    @abstractmethod
    def load_train(self) -> pd.DataFrame:
        pass

    @abstractmethod
    def load_test(self) -> pd.DataFrame:
        pass
