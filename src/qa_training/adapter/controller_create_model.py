import pandas as pd

from qa_training.domain.ml_model import MLModel
from qa_training.utils.boundary.usecase.if_usecase_create_model import (
    IF_UsecaseCreateModel,
)
from qa_training.utils.config_manager import (
    ConfigManager,
    ConfigManagerRepoCommand,
    ConfigManagerUsecaseCommand,
)
from qa_training.utils.domain_registry import DomainRegistry


class ControllerCreateModel:
    def __init__(
        self,
        usecase_command: ConfigManagerUsecaseCommand,
        repo_command: ConfigManagerRepoCommand,
    ) -> None:
        self._usecase = self._gene_usecase(
            usecase_command=usecase_command, repo_command=repo_command
        )

    def run(self):
        self._usecase.create_model()

    def make_features(
        self, df_customer_info: pd.DataFrame
    ) -> tuple[pd.DataFrame, pd.DataFrame]:
        df_X, df_y = self._usecase.make_features(df_customer_info)
        return df_X, df_y

    def train(self, df_X: pd.DataFrame, df_y: pd.DataFrame) -> MLModel:
        ml_model = self._usecase.train(df_X=df_X, df_y=df_y)
        return ml_model

    def store(self, ml_model: MLModel) -> None:
        self._usecase.store(ml_model=ml_model)

    def initialize(self):
        self._usecase.initialize()

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
