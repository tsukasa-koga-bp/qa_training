import pandas as pd
import pytest
from qa_training.domain.service_make_features import ServiceMakeFeatures
from qa_training.utils.my_assert_frame_equal import MyAssert


@pytest.fixture
def fixture_run():
    service_make_features = ServiceMakeFeatures()

    df_customer_info = pd.read_csv(
        "tests/common_data/df_customer_info.csv",
    )
    df_id_expected = pd.read_csv(
        "tests/common_data/df_id.csv",
    )
    df_X_expected = pd.read_csv(
        "tests/common_data/df_X.csv",
    )
    df_y_expected = pd.read_csv(
        "tests/common_data/df_y.csv",
    )
    return (
        service_make_features,
        df_customer_info,
        df_id_expected,
        df_X_expected,
        df_y_expected,
    )


def test_run(
    fixture_run: tuple[
        ServiceMakeFeatures, pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame
    ]
):
    (
        service_make_features,
        df_customer_info,
        df_id_expected,
        df_X_expected,
        df_y_expected,
    ) = fixture_run

    df_id, df_X, df_y = service_make_features.run(df_customer_info)

    MyAssert().assert_df(df_id, df_id_expected)
    MyAssert().assert_df(df_X, df_X_expected)
    MyAssert().assert_df(df_y, df_y_expected)


@pytest.fixture
def fixture_missing_values_in_age():
    service_make_features = ServiceMakeFeatures()

    df_customer_info = pd.read_csv(
        "tests/qa_training/domain/service_make_features_data/missing_values_in_age/df_customer_info.csv",
    )
    df_id_expected = pd.read_csv(
        "tests/qa_training/domain/service_make_features_data/missing_values_in_age/df_id.csv",
    )
    df_X_expected = pd.read_csv(
        "tests/qa_training/domain/service_make_features_data/missing_values_in_age/df_X.csv",
    )
    df_y_expected = pd.read_csv(
        "tests/qa_training/domain/service_make_features_data/missing_values_in_age/df_y.csv",
    )
    return (
        service_make_features,
        df_customer_info,
        df_id_expected,
        df_X_expected,
        df_y_expected,
    )


def test_missing_values_in_age(
    fixture_missing_values_in_age: tuple[
        ServiceMakeFeatures, pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame
    ]
):
    """欠損補完, Ageが10で埋まること"""

    (
        service_make_features,
        df_customer_info,
        df_id_expected,
        df_X_expected,
        df_y_expected,
    ) = fixture_missing_values_in_age

    df_id, df_X, df_y = service_make_features.run(df_customer_info)

    MyAssert().assert_df(df_id, df_id_expected)
    MyAssert().assert_df(df_X, df_X_expected)
    MyAssert().assert_df(df_y, df_y_expected)


@pytest.fixture
def fixture_missing_values_in_cabin():
    service_make_features = ServiceMakeFeatures()

    df_customer_info = pd.read_csv(
        "tests/qa_training/domain/service_make_features_data/missing_values_in_cabin/df_customer_info.csv",
    )
    df_id_expected = pd.read_csv(
        "tests/qa_training/domain/service_make_features_data/missing_values_in_cabin/df_id.csv",
    )
    df_X_expected = pd.read_csv(
        "tests/qa_training/domain/service_make_features_data/missing_values_in_cabin/df_X.csv",
    )
    df_y_expected = pd.read_csv(
        "tests/qa_training/domain/service_make_features_data/missing_values_in_cabin/df_y.csv",
    )
    return (
        service_make_features,
        df_customer_info,
        df_id_expected,
        df_X_expected,
        df_y_expected,
    )


def test_missing_values_in_cabin(
    fixture_missing_values_in_age: tuple[
        ServiceMakeFeatures, pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame
    ]
):
    """欠損補完, cabinがSで埋まること"""

    (
        service_make_features,
        df_customer_info,
        df_id_expected,
        df_X_expected,
        df_y_expected,
    ) = fixture_missing_values_in_age

    df_id, df_X, df_y = service_make_features.run(df_customer_info)

    MyAssert().assert_df(df_id, df_id_expected)
    MyAssert().assert_df(df_X, df_X_expected)
    MyAssert().assert_df(df_y, df_y_expected)
