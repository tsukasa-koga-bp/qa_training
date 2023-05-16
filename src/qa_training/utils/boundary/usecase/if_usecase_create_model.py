from abc import ABC, abstractmethod

import pandas as pd

from qa_training.domain.ml_model import MLModel


class IF_UsecaseCreateModel(ABC):
    """モデル作成ユースケースのインターフェースクラス.
    整形データを生成する.
    """

    @abstractmethod
    def create_model(self):
        """モデル作成する."""
        pass

    @abstractmethod
    def load_train(self) -> pd.DataFrame:
        """学習データを読み込む."""
        pass

    @abstractmethod
    def make_features(
        self, df_customer_info: pd.DataFrame
    ) -> tuple[pd.DataFrame, pd.DataFrame]:
        """特徴量を作成する."""
        pass

    @abstractmethod
    def train(self, df_X: pd.DataFrame, df_y: pd.DataFrame) -> MLModel:
        """学習する."""
        pass

    @abstractmethod
    def store(self, ml_model: MLModel) -> None:
        """モデルを保存する."""
        pass

    @abstractmethod
    def initialize(self) -> None:
        """ユースケースの実行による出力を初期化する."""
