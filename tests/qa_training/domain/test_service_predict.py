from typing import Tuple

import pandas as pd
import pytest
from qa_training.domain.service_predict import ServicePredict
from qa_training.domain.service_train import ServiceTrain
from qa_training.utils.domain_registry import DomainRegistry
from qa_training.utils.my_assert_frame_equal import MyAssert


@pytest.fixture
def fixture_run(domain_registry: DomainRegistry):
    repo_model = domain_registry.repo_model()
    service_train = ServiceTrain(repo_model=repo_model)
    service_predict = ServicePredict(repo_model=repo_model)

    df_X = pd.read_csv(
        "./tests/common_data/df_X.csv",
    )
    df_y = pd.read_csv(
        "./tests/common_data/df_y.csv",
    )

    df_y_pred_expected = pd.read_csv(
        "./tests/common_data/df_y_pred_expected.csv",
    )

    service_train.run(df_X, df_y)

    yield service_predict, df_X, df_y_pred_expected
    repo_model.initialize()


def test_run(fixture_run: Tuple[ServicePredict, pd.DataFrame, pd.DataFrame]):
    (
        service_predict,
        df_X,
        df_y_pred_expected,
    ) = fixture_run

    df_y_pred = service_predict.run(df_X=df_X)

    MyAssert().assert_df(df_y_pred, df_y_pred_expected)
