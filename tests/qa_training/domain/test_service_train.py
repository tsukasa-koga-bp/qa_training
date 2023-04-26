import pandas as pd
import pytest
from qa_training.domain.service_train import ServiceTrain
from qa_training.utils.domain_registry import DomainRegistry


@pytest.fixture
def fixture_run(domain_registry: DomainRegistry):
    service_train = ServiceTrain()

    df_X = pd.read_csv(
        "./tests/common_data/df_X.csv",
    )
    df_y = pd.read_csv(
        "./tests/common_data/df_y.csv",
    )

    return service_train, df_X, df_y


def test_run(fixture_run: tuple[ServiceTrain, pd.DataFrame, pd.DataFrame]):
    service_train, df_X, df_y = fixture_run

    is_success = service_train.run(df_X, df_y)
    assert is_success
