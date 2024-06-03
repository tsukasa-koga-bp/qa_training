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
    df_filled = pd.read_csv(
        "tests/qa_training/domain/test_service_make_features/violations/df_filled.csv",
        dtype=dtype_dict)
    df_obeyed_expected = pd.read_csv(
        "tests/qa_training/domain/test_service_make_features/violations/df_obeyed_expected.csv",
        dtype=dtype_dict)

    return service, df_filled, df_obeyed_expected

def test_run(fixture_run):
    # Arrange
    service, df_filled, df_obeyed_expected = fixture_run

    # Act
    df_obeyed = service._handle_violations(df_filled=df_filled)
    print("aaaaa", df_obeyed, df_obeyed_expected)

    # Assert
    MyAssert().assert_df(df_obeyed, df_obeyed_expected)
