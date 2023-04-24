from typing import Tuple

import pandas as pd
import pytest
from qa_training.adapter.repo.repo_model import RepoModel
from qa_training.domain.service_predict import ServicePredict


@pytest.fixture
def fixture_run():
    service_predict = ServicePredict(repo_model=RepoModel())

    df_X = pd.read_csv(
        "./tests/common_data/df_X.csv",
        sep="\t",
    )

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
