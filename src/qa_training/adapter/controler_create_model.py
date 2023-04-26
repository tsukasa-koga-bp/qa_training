from qa_training.utils.boundary.usecase.if_usecase_create_model import (
    IF_UsecaseCreateModel,
)
from qa_training.utils.config_manager import (
    ConfigManager,
    ConfigManagerRepoCommand,
    ConfigManagerUsecaseCommand,
)
from qa_training.utils.domain_registry import DomainRegistry


class ControlerCreateModel:
    def run(
        self,
        usecase_command: ConfigManagerUsecaseCommand,
        repo_command: ConfigManagerRepoCommand,
    ):
        usecase = self._gene_usecase(
            usecase_command=usecase_command, repo_command=repo_command
        )

        usecase.create_model()

    def _gene_usecase(
        self,
        usecase_command: ConfigManagerUsecaseCommand,
        repo_command: ConfigManagerRepoCommand,
    ) -> IF_UsecaseCreateModel:
        config_manager = ConfigManager(
            usecase_command=usecase_command, repo_command=repo_command
        )
        domain_registry = DomainRegistry(config_manager=config_manager)
        return domain_registry.usecase_create_model()
