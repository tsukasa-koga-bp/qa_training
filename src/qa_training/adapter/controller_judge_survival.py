from qa_training.utils.boundary.usecase.if_usecase_judge_survival import (
    IF_UsecaseJudgeSurvival,
)
from qa_training.utils.config_manager import (
    ConfigManager,
    ConfigManagerRepoCommand,
    ConfigManagerUsecaseCommand,
)
from qa_training.utils.domain_registry import DomainRegistry
from qa_training.utils.logging import log_decorator


class ControllerJudgeSurvival:
    def __init__(
        self,
        usecase_command: ConfigManagerUsecaseCommand,
        repo_command: ConfigManagerRepoCommand,
    ) -> None:
        self._usecase = self._gene_usecase(
            usecase_command=usecase_command, repo_command=repo_command
        )

    @log_decorator
    def run(self):
        self._usecase.judge_survival()

    @log_decorator
    def initialize(self):
        self._usecase.initialize()

    def _gene_usecase(
        self,
        usecase_command: ConfigManagerUsecaseCommand,
        repo_command: ConfigManagerRepoCommand,
    ) -> IF_UsecaseJudgeSurvival:
        config_manager = ConfigManager(
            usecase_command=usecase_command, repo_command=repo_command
        )
        domain_registry = DomainRegistry(config_manager=config_manager)
        return domain_registry.usecase_judge_survival()
