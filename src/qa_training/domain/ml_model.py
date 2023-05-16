from typing import Any

import pandas as pd


class MLModel:
    """
    モデルを管理する
    """

    def __init__(self, model: Any) -> None:
        self._model = model

    def get_model(self) -> Any:
        return self._model

    def train(self, df_X: pd.DataFrame, df_y: pd.DataFrame) -> None:
        y = df_y["Survived"]
        self._model = self._model.fit(df_X, y)

    def predict(self, df_X: pd.DataFrame) -> pd.DataFrame:
        y_pred = self._model.predict(df_X)
        df_y_pred = pd.DataFrame(y_pred, columns=["Survived"])
        return df_y_pred
