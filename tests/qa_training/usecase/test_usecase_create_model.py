import pytest
from qa_training.utils.boundary.usecase.if_usecase_create_model import (
    IF_UsecaseCreateModel,
)
from qa_training.utils.domain_registry import DomainRegistry


@pytest.fixture
def fixture_create_model(domain_registry: DomainRegistry):
    usecase_create_model = domain_registry.usecase_create_model()
    return usecase_create_model


def test_create_model(fixture_create_model: IF_UsecaseCreateModel):
    usecase_create_model = fixture_create_model

    usecase_create_model.create_model()
