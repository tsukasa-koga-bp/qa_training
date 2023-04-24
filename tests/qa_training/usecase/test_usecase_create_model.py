from qa_training.utils.boundary.usecase.if_usecase_create_model import (
    IF_UsecaseCreateModel,
)


def fixture_create_model():
    pass


def test_create_model(fixture_create_model: IF_UsecaseCreateModel):
    usecase_create_model = fixture_create_model

    usecase_create_model.create_model()
