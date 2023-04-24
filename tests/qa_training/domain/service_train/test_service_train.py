import pandas as pd
import pytest
from qa_training.adapter.repo.repo_model import RepoModel
from qa_training.domain.service_train import ServiceTrain


@pytest.fixture
def fixture_run():
    repo_model = RepoModel()
    service_train = ServiceTrain(repo_model=repo_model)

    df_X_and_y_expected = pd.read_csv(
        "./tests/qa_training/domain/service_train/data/df_X_and_y.csv",
        sep="\t",
    )
    df_X = df_X_and_y_expected.drop("Survived", axis=1)
    df_y = df_X_and_y_expected[["Survived"]]

    return service_train, df_X, df_y


def test_run(fixture_run):
    service_train, df_X, df_y = fixture_run

    service_train.run(df_X, df_y)
