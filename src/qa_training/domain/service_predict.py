import pandas as pd
from qa_training.domain.ml_model import MLModel


class ServicePredict:
    """
    モデルに予測させる
    """

    def run(self, df_X: pd.DataFrame, ml_model: MLModel) -> pd.DataFrame:
        df_y_pred = ml_model.predict(df_X)
        return df_y_pred
