import pytest
from qa_training.adapter.controller_create_model import ControllerCreateModel
from qa_training.adapter.controller_judge_survival import ControllerJudgeSurvival
from qa_training.utils.config_manager import (
    ConfigManagerRepoCommand,
    ConfigManagerUsecaseCommand,
)


@pytest.fixture
def usecase_and_repo_command():
    usecase_command = ConfigManagerUsecaseCommand(
        usecase_create_model_yaml_path="tests/common_data/configs/usecase/UsecaseCreateModel.yaml",
        usecase_judge_survival_yaml_path="tests/common_data/configs/usecase/UsecaseJudgeSurvival.yaml",
    )
    repo_command = ConfigManagerRepoCommand(
        repo_model_yaml_path="tests/common_data/configs/repo/RepoModel.yaml",
        repo_input_data_yaml_path="tests/common_data/configs/repo/RepoInputData.yaml",
        repo_output_data_yaml_path="tests/common_data/configs/repo/RepoOutputData.yaml",
    )
    return usecase_command, repo_command


@pytest.fixture
def fixture_controller_create_model(
    usecase_and_repo_command: tuple[
        ConfigManagerUsecaseCommand, ConfigManagerRepoCommand
    ]
):
    usecase_command, repo_command = usecase_and_repo_command

    controller_create_model = ControllerCreateModel(
        usecase_command=usecase_command, repo_command=repo_command
    )
    yield controller_create_model
    controller_create_model.initialize()


@pytest.fixture
def fixture_judge_survival(
    usecase_and_repo_command: tuple[
        ConfigManagerUsecaseCommand, ConfigManagerRepoCommand
    ],
    fixture_controller_create_model: ControllerCreateModel,
):
    usecase_command, repo_command = usecase_and_repo_command
    controller_create_model = fixture_controller_create_model
    controller_create_model.run()

    controller_judge_survival = ControllerJudgeSurvival(
        usecase_command=usecase_command,
        repo_command=repo_command,
    )

    yield controller_judge_survival
    controller_judge_survival.initialize()
