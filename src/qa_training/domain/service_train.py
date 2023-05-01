from typing import Any

import pandas as pd
from qa_training.domain.factory_ml_model import FactoryMLModel
from qa_training.domain.ml_model import MLModel


class ServiceTrain:
    """
    モデルを学習させる
    """

    def __init__(self, model_name: str, model_parameters: dict[str, Any]) -> None:
        self._ml_model = FactoryMLModel().gene_from_parameters(
            model_name=model_name, model_parameters=model_parameters
        )

    def run(self, df_X: pd.DataFrame, df_y: pd.DataFrame) -> MLModel:
        self._ml_model.train(df_X=df_X, df_y=df_y)

        return self._ml_model
