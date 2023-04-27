import pandas as pd
from sklearn.ensemble import RandomForestClassifier as RandomForest


class MLModel:
    def __init__(self, model=RandomForest()) -> None:
        self._model = model

    def get_model(self) -> RandomForest:
        return self._model

    def train(self, df_X: pd.DataFrame, df_y: pd.DataFrame) -> None:
        y = df_y["Survived"]
        self._model = RandomForest(n_estimators=100).fit(df_X, y)

    def predict(self, df_X: pd.DataFrame) -> pd.DataFrame:
        y_pred = self._model.predict(df_X)
        df_y_pred = pd.DataFrame(y_pred, columns=["Survived"])
        return df_y_pred
