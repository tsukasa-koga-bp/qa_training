import pandas as pd
import pytest
from qa_training.domain.service_make_features import ServiceMakeFeatures
from qa_training.utils.my_assert_frame_equal import MyAssert


@pytest.fixture()
def fixture_run():
    dtype_dict = {
        "Ticket": "str"
    }
    service = ServiceMakeFeatures()
    df_obeyed = pd.read_csv(
        "tests/qa_training/domain/test_service_make_features/features/df_obeyed.csv",
        dtype=dtype_dict)
    df_expected = pd.read_csv(
        "tests/qa_training/domain/test_service_make_features/features/df_expected.csv",
        dtype=dtype_dict)

    return service, df_obeyed, df_expected

def test_run(fixture_run):
    # Arrange
    service, df_obeyed, df_expected = fixture_run

    # Act
    df_feature_added = service._make_features(df_obeyed=df_obeyed)
    print("aaaaa\n", df_feature_added, "\n\n", df_expected)

    # Assert
    MyAssert().assert_df(df_feature_added, df_expected)
