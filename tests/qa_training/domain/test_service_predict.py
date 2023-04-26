from typing import Tuple

import pandas as pd
import pytest
from qa_training.domain.service_predict import ServicePredict
from qa_training.domain.service_train import ServiceTrain
from qa_training.utils.domain_registry import DomainRegistry


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
    list_survival_expected: list[bool] = df_y_pred_expected["Survived"].to_list()

    service_train.run(df_X, df_y)

    yield service_predict, df_X, list_survival_expected
    repo_model.initialize()


def test_run(fixture_run: Tuple[ServicePredict, pd.DataFrame, pd.DataFrame]):
    (
        service_predict,
        df_X,
        list_survival_expected,
    ) = fixture_run

    list_survival = service_predict.run(df_X=df_X)
    assert list_survival == list_survival_expected
