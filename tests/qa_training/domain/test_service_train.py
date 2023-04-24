import pandas as pd
import pytest
from qa_training.adapter.repo.repo_model import RepoModel
from qa_training.domain.service_train import ServiceTrain


@pytest.fixture
def fixture_run():
    repo_model = RepoModel()
    service_train = ServiceTrain(repo_model=repo_model)

    df_X = pd.read_csv(
        "./tests/common_data/df_X.csv",
        sep="\t",
    )
    df_y = pd.read_csv(
        "./tests/common_data/df_y.csv",
        sep="\t",
    )

    return service_train, df_X, df_y


def test_run(fixture_run):
    service_train, df_X, df_y = fixture_run

    is_success = service_train.run(df_X, df_y)
    assert is_success
