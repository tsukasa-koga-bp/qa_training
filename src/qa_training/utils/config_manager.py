from typing import NamedTuple, Union, cast

from omegaconf import DictConfig, ListConfig, OmegaConf

from qa_training.utils.boundary.repo.if_repo_model import IF_RepoModel
from qa_training.utils.boundary.usecase.if_usecase_create_model import (
    IF_UsecaseCreateModel,
)
from qa_training.utils.boundary.usecase.if_usecase_judge_survival import (
    IF_UsecaseJudgeSurvival,
)


class ConfigManagerUsecaseCommand(NamedTuple):
    """各Usecaseクラスに対応したconfigのファイルパスの集合."""

    usecase_judge_survival_yaml_path: str
    usecase_create_model_yaml_path: str


class ConfigManagerRepoCommand(NamedTuple):
    """各Repoクラスに対応したconfigのファイルパスの集合"""

    repo_model_yaml_path: str


class ConfigManager:
    """configを解釈し, ユースケースとリポジトリの依存解決と初期化をする."""

    def __init__(
        self,
        usecase_command: ConfigManagerUsecaseCommand,
        repo_command: ConfigManagerRepoCommand,
    ) -> None:
        assert type(usecase_command) is ConfigManagerUsecaseCommand
        assert type(repo_command) is ConfigManagerRepoCommand

        self._usecase_command = usecase_command
        self._repo_command = repo_command

    def _convert_yaml(self, yaml: Union[DictConfig, ListConfig], type_name: str):
        cfg = cast(dict, OmegaConf.to_container(yaml))
        inner_cfg = cfg[type_name]

        return inner_cfg["classname"], inner_cfg["params"]

    # Usecase
    def params_for_usecase_judge_survival(self) -> tuple[str, dict]:
        """生存判定ユースケースのパラメータを返す

        Returns:
            tuple[str, dict]: _description_
        """
        yaml = OmegaConf.load(self._usecase_command.usecase_judge_survival_yaml_path)
        return self._convert_yaml(yaml, IF_UsecaseJudgeSurvival.__name__)

    def params_for_usecase_create_model(self):
        """モデル作成ユースケースのパラメータを返す

        Returns:
            _type_: _description_
        """
        yaml = OmegaConf.load(self._usecase_command.usecase_create_model_yaml_path)
        return self._convert_yaml(yaml, IF_UsecaseCreateModel.__name__)

    # Repository

    def params_for_repo_model(self):
        """モデルリポジトリのパラメータを返す

        Returns:
            _type_: _description_
        """
        yaml = OmegaConf.load(self._repo_command.repo_model_yaml_path)
        return self._convert_yaml(yaml, IF_RepoModel.__name__)
