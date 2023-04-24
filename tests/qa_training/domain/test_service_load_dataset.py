import pandas as pd
import pytest
from qa_training.domain.service_load_dataset import ServiceLoadDataset
from qa_training.utils.my_assert_frame_equal import MyAssert


@pytest.fixture
def fixture_run():
    service_load_dataset = ServiceLoadDataset()
    csv_path = "./tests/common_data/train.csv"
    df_customer_info_expected = pd.read_csv(
        "./tests/common_data/train.csv",
        sep="\t",
    )

    return service_load_dataset, csv_path, df_customer_info_expected


def test_run(fixture_run):
    service_load_dataset, csv_path, df_customer_info_expected = fixture_run

    df_customer_info = service_load_dataset.run(csv_path)

    MyAssert().assert_df(
        df_results=df_customer_info, df_expected=df_customer_info_expected
    )
