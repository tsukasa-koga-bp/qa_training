import os

from qa_training.adapter.controller_create_model import ControllerCreateModel


def test_run(fixture_controller_create_model: ControllerCreateModel):
    controller_create_model = fixture_controller_create_model

    controller_create_model.run()

    assert os.path.exists("tests/output/model.pkl")
