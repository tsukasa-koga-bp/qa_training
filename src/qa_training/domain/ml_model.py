from typing import Any

import pandas as pd

from qa_training.utils.logging import log_decorator


class MLModel:
    """
    モデルを管理する
    """

    def __init__(self, model: Any) -> None:
        self._model = model

    @log_decorator
    def get_model(self) -> Any:
        return self._model

    @log_decorator
    def train(self, df_X: pd.DataFrame, df_y: pd.DataFrame) -> None:
        y = df_y["Survived"]
        self._model = self._model.fit(df_X, y)

    @log_decorator
    def predict(self, df_X: pd.DataFrame) -> pd.DataFrame:
        y_pred = self._model.predict(df_X)
        df_y_pred = pd.DataFrame(y_pred, columns=["Survived"])
        return df_y_pred
