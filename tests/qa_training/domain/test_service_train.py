import pandas as pd
import pytest
from _pytest.fixtures import SubRequest
from qa_training.domain.service_train import ServiceTrain
from qa_training.utils.domain_registry import DomainRegistry

params = {
    "RandomForest": (
        "RandomForest",
        {
            "criterion": "entropy",
            "max_depth": 4,
            "n_estimators": 100,
            "random_state": 62,
        },
    ),
    "LogisticRegression": (
        "LogisticRegression",
        {
            "penalty": "l2",
            "tol": 0.0001,
            "max_iter": 100,
            "multi_class": "auto",
            "random_state": None,
        },
    ),
}


@pytest.fixture(params=params.values(), ids=params.keys())  # type: ignore
def fixture_run(domain_registry: DomainRegistry, request: SubRequest):
    model_name = request.param[0]
    model_parameters = request.param[1]

    service_train = ServiceTrain(
        model_name=model_name, model_parameters=model_parameters
    )

    df_X = pd.read_csv(
        "tests/common_data/df_X.csv",
    )
    df_y = pd.read_csv(
        "tests/common_data/df_y.csv",
    )

    return service_train, df_X, df_y


def test_run(fixture_run: tuple[ServiceTrain, pd.DataFrame, pd.DataFrame]):
    service_train, df_X, df_y = fixture_run

    is_success = service_train.run(df_X, df_y)
    assert is_success
