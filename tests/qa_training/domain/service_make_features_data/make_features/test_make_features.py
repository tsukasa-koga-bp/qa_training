import pandas as pd
import pytest
from qa_training.domain.service_make_features import ServiceMakeFeatures
from qa_training.utils.my_assert_frame_equal import MyAssert

test_data_common_path = (
    "tests/qa_training/domain/service_make_features_data/make_features"
)


@pytest.fixture
def fixture_make_features_of_sex():
    service_make_features = ServiceMakeFeatures()

    dir_path = "make_features_of_sex"

    df_obeyed = pd.read_csv(f"{test_data_common_path}/{dir_path}/df_obeyed.csv")
    df_X_and_id_expected = pd.read_csv(
        f"{test_data_common_path}/{dir_path}/df_X_and_id_expected.csv"
    )

    return (service_make_features, df_obeyed, df_X_and_id_expected)


def test_make_features_of_sex(
    fixture_make_features_of_sex: tuple[ServiceMakeFeatures, pd.DataFrame, pd.DataFrame]
):
    """特徴量, sexがダミー変数化されること, male -> 0, female -> 1"""

    (
        service_make_features,
        df_obeyed,
        df_X_and_id_expected,
    ) = fixture_make_features_of_sex

    df_X_and_id = service_make_features._make_features(df_obeyed)

    MyAssert().assert_df(df_X_and_id[["Sex"]], df_X_and_id_expected[["Sex"]])


@pytest.fixture
def fixture_make_features_of_embarked():
    service_make_features = ServiceMakeFeatures()

    dir_path = "make_features_of_embarked"

    df_obeyed = pd.read_csv(f"{test_data_common_path}/{dir_path}/df_obeyed.csv")
    df_X_and_id_expected = pd.read_csv(
        f"{test_data_common_path}/{dir_path}/df_X_and_id_expected.csv"
    )

    return (service_make_features, df_obeyed, df_X_and_id_expected)


def test_make_features_of_embarked(
    fixture_make_features_of_embarked: tuple[
        ServiceMakeFeatures, pd.DataFrame, pd.DataFrame
    ]
):
    """特徴量, embarkedがone hot encodingされること"""

    (
        service_make_features,
        df_obeyed,
        df_X_and_id_expected,
    ) = fixture_make_features_of_embarked

    df_X_and_id = service_make_features._make_features(df_obeyed)

    MyAssert().assert_df(
        df_X_and_id[["Embarked_C", "Embarked_Q", "Embarked_S"]],
        df_X_and_id_expected[["Embarked_C", "Embarked_Q", "Embarked_S"]],
    )
