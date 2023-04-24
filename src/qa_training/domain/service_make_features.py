from typing import Tuple

import pandas as pd


class ServiceMakeFeatures:
    def run(self, df_customer_info: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
        df_X = self._make_X(df_customer_info)
        df_y = self._make_y(df_customer_info)
        return df_X, df_y

    def _make_X(self, df_customer_info: pd.DataFrame) -> pd.DataFrame:
        # df_X = pd.get_dummies(df_customer_info[["Pclass", "Sex", "SibSp", "Parch"]])
        df_X = df_customer_info[["Pclass", "Sex", "SibSp", "Parch"]]
        return df_X

    def _make_y(self, df_customer_info: pd.DataFrame) -> pd.DataFrame:
        df_y = df_customer_info[["Survived"]]
        return df_y

    """
    def _make_survived(self, df_origin: pd.DataFrame):
        pass

    def _make_familiy_size(self, df_origin: pd.DataFrame) -> pd.DataFrame:
        return pd.DataFrame()

    def _make_is_alone(self, df_origin: pd.DataFrame) -> pd.DataFrame:
        return pd.DataFrame()

    """
