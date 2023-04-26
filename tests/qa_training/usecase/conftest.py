import pandas as pd
import pytest
from qa_training.utils.boundary.usecase.if_usecase_create_model import (
    IF_UsecaseCreateModel,
)
from qa_training.utils.domain_registry import DomainRegistry


@pytest.fixture
def fixture_create_model(domain_registry: DomainRegistry):
    usecase_create_model = domain_registry.usecase_create_model()
    yield usecase_create_model
    usecase_create_model.initialize()


@pytest.fixture
def fixture_judge_survival(
    domain_registry: DomainRegistry, fixture_create_model: IF_UsecaseCreateModel
):
    fixture_create_model.create_model()

    usecase_judge_survival = domain_registry.usecase_judge_survival()

    df_results_expected = pd.read_csv(
        "./tests/common_data/df_results_expected.csv",
    )

    yield usecase_judge_survival, df_results_expected
    usecase_judge_survival.initialize()
