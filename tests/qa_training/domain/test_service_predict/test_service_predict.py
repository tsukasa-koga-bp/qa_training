from typing import Tuple

import pandas as pd
import pytest
from qa_training.adapter.repo.repo_model import RepoModel
from qa_training.domain.service_predict import ServicePredict


@pytest.fixture
def fixture_run():
    service_predict = ServicePredict(repo_model=RepoModel())

    df_X_and_y_expected = pd.read_csv(
        "./tests/qa_training/domain/test_service_predict/data/df_X_and_y_expected.csv",
        sep="\t",
    )
    df_X = df_X_and_y_expected.drop("Survived", axis=1)
    list_survival_expected = [True]
    return service_predict, df_X, list_survival_expected


def test_run(fixture_run: Tuple[ServicePredict, pd.DataFrame, list[bool]]):
    (
        service_predict,
        df_X,
        list_survival_expected,
    ) = fixture_run

    list_survival = service_predict.run(df_X=df_X)

    assert list_survival == list_survival_expected
