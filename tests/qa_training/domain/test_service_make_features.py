from typing import Tuple

import pandas as pd
import pytest
from qa_training.domain.service_make_features import ServiceMakeFeatures
from qa_training.utils.my_assert_frame_equal import MyAssert


@pytest.fixture
def fixture_run():
    service_make_features = ServiceMakeFeatures()

    df_customer_info = pd.read_csv(
        "./tests/qa_training/domain/data/df_customer_info.csv", sep="\t"
    )
    df_X_and_y_expected = pd.read_csv(
        "./tests/qa_training/domain/data/df_X_and_y_expected.csv", sep="\t"
    )
    df_X_expected = df_X_and_y_expected.drop("Survived", axis=1)
    df_y_expected = df_X_and_y_expected[["Survived"]]
    return service_make_features, df_customer_info, df_X_expected, df_y_expected


def test_run(
    fixture_run: Tuple[ServiceMakeFeatures, pd.DataFrame, pd.DataFrame, pd.DataFrame]
):
    (
        service_make_features,
        df_customer_info,
        df_X_expected,
        df_y_expected,
    ) = fixture_run

    df_X, df_y = service_make_features.run(df_customer_info)

    MyAssert().assert_df(df_X, df_X_expected)
    MyAssert().assert_df(df_y, df_y_expected)
