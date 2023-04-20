from typing import Tuple

import pandas as pd
from qa_training.domain.customer_info import CustomerInfo


class ServiceMakeFeatures:
    def run(
        self, list_customer_info: list[CustomerInfo]
    ) -> Tuple[pd.Series, pd.DataFrame]:
        df_origin = self._convert_to_dataframe(list_customer_info)

        y = df_origin["Survived"]
        X = pd.get_dummies(df_origin[["Pclass", "Sex", "SibSp", "Parch"]])  # noqa: N806
        return y, X

    def _convert_to_dataframe(
        self, list_customer_info: list[CustomerInfo]
    ) -> pd.DataFrame:
        return pd.DataFrame()

    """
    def _make_survived(self, df_origin: pd.DataFrame):
        pass

    def _make_familiy_size(self, df_origin: pd.DataFrame) -> pd.DataFrame:
        return pd.DataFrame()

    def _make_is_alone(self, df_origin: pd.DataFrame) -> pd.DataFrame:
        return pd.DataFrame()

    """
