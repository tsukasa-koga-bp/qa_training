import sys

import click

sys.path.append("src/")

from qa_training.adapter.controller_create_model import (
    ControllerCreateModel,
)
from qa_training.adapter.controller_judge_survival import ControllerJudgeSurvival
from qa_training.utils.config_manager import (
    ConfigManagerRepoCommand,
    ConfigManagerUsecaseCommand,
)


@click.command()
@click.option("--enable_create_model", is_flag=True, help="モデル作成するか")
@click.option("--enable_judge_survival", is_flag=True, help="生存判定するか")
@click.option(
    "--configs",
    type=click.Path(exists=True),
    default="configs",
    help="configsフォルダのパス",
)
def main(
    enable_create_model: bool,
    enable_judge_survival: bool,
    configs: str,
):
    usecase_command = ConfigManagerUsecaseCommand(
        usecase_create_model_yaml_path=f"{configs}/usecase/UsecaseCreateModel.yaml",
        usecase_judge_survival_yaml_path=f"{configs}/usecase/UsecaseJudgeSurvival.yaml",
    )

    repo_command = ConfigManagerRepoCommand(
        repo_input_data_yaml_path=f"{configs}/repo/RepoInputData.yaml",
        repo_model_yaml_path=f"{configs}/repo/RepoModel.yaml",
        repo_output_data_yaml_path=f"{configs}/repo/RepoOutputData.yaml",
    )

    if enable_create_model:
        controller = ControllerCreateModel(
            usecase_command=usecase_command, repo_command=repo_command
        )
        controller.run()

    if enable_judge_survival:
        controller = ControllerJudgeSurvival(
            usecase_command=usecase_command, repo_command=repo_command
        )
        controller.run()


if __name__ == "__main__":
    main()
