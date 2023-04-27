import pandas as pd
from qa_training.domain.ml_model import MLModel


class ServiceTrain:
    def run(self, df_X: pd.DataFrame, df_y: pd.DataFrame) -> MLModel:
        ml_model = MLModel()
        ml_model.train(df_X=df_X, df_y=df_y)

        return ml_model
