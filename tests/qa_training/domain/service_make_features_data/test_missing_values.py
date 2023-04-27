import pandas as pd
import pytest
from qa_training.domain.service_make_features import ServiceMakeFeatures
from qa_training.utils.my_assert_frame_equal import MyAssert


@pytest.fixture
def fixture_missing_values_in_age():
    service_make_features = ServiceMakeFeatures()

    df_customer_info = pd.read_csv(
        "tests/qa_training/domain/service_make_features_data/missing_values_in_age/df_customer_info.csv",
    )
    df_filled_expected = pd.read_csv(
        "tests/qa_training/domain/service_make_features_data/missing_values_in_age/df_filled_expected.csv",
    )

    return (service_make_features, df_customer_info, df_filled_expected)


def test_missing_values_in_age(
    fixture_missing_values_in_age: tuple[
        ServiceMakeFeatures, pd.DataFrame, pd.DataFrame
    ]
):
    """欠損補完, Ageが20で埋まること"""

    (
        service_make_features,
        df_customer_info,
        df_filled_expected,
    ) = fixture_missing_values_in_age

    df_filled = service_make_features._handle_missing_values(df_customer_info)

    MyAssert().assert_df(df_filled, df_filled_expected)


@pytest.fixture
def fixture_missing_values_in_embarked():
    service_make_features = ServiceMakeFeatures()

    df_customer_info = pd.read_csv(
        "tests/qa_training/domain/service_make_features_data/missing_values_in_embarked/df_customer_info.csv",
    )
    df_filled_expected = pd.read_csv(
        "tests/qa_training/domain/service_make_features_data/missing_values_in_embarked/df_filled_expected.csv",
    )

    return (service_make_features, df_customer_info, df_filled_expected)


def test_missing_values_in_embarked(
    fixture_missing_values_in_embarked: tuple[
        ServiceMakeFeatures, pd.DataFrame, pd.DataFrame
    ]
):
    """欠損補完, EmbarkedがSで埋まること"""

    (
        service_make_features,
        df_customer_info,
        df_filled_expected,
    ) = fixture_missing_values_in_embarked

    df_filled = service_make_features._handle_missing_values(df_customer_info)

    MyAssert().assert_df(df_filled, df_filled_expected)
