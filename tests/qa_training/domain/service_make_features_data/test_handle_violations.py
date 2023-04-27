import pandas as pd
import pytest
from qa_training.domain.service_make_features import ServiceMakeFeatures
from qa_training.utils.my_assert_frame_equal import MyAssert


@pytest.fixture
def fixture_handle_violations_in_pclass():
    service_make_features = ServiceMakeFeatures()

    df_customer_info = pd.read_csv(
        "tests/qa_training/domain/service_make_features_data/handle_violations_in_pclass/df_customer_info.csv",
    )
    df_obeyed_expected = pd.read_csv(
        "tests/qa_training/domain/service_make_features_data/handle_violations_in_pclass/df_obeyed_expected.csv",
    )

    return (service_make_features, df_customer_info, df_obeyed_expected)


def test_handle_violations_in_pclass(
    fixture_handle_violations_in_pclass: tuple[
        ServiceMakeFeatures, pd.DataFrame, pd.DataFrame
    ]
):
    """制約違反処理, pclassが1,2,3以外の行が削除されること"""

    (
        service_make_features,
        df_customer_info,
        df_obeyed_expected,
    ) = fixture_handle_violations_in_pclass

    df_obeyed = service_make_features._handle_violations(df_customer_info)

    MyAssert().assert_df(df_obeyed, df_obeyed_expected)
