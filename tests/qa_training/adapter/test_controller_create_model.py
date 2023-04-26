from qa_training.adapter.controller_create_model import ControllerCreateModel
from qa_training.utils.config_manager import (
    ConfigManagerRepoCommand,
    ConfigManagerUsecaseCommand,
)


def test_run(
    fixture_run: tuple[
        ControllerCreateModel, ConfigManagerUsecaseCommand, ConfigManagerRepoCommand
    ]
):
    controller_create_model, usecase_command, repo_command = fixture_run

    controller_create_model.run(
        usecase_command=usecase_command, repo_command=repo_command
    )
