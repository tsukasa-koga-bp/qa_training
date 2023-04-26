import os

import pandas as pd

from qa_training.utils.boundary.usecase.if_usecase_judge_survival import (
    IF_UsecaseJudgeSurvival,
)
from qa_training.utils.config_manager import (
    ConfigManager,
    ConfigManagerRepoCommand,
    ConfigManagerUsecaseCommand,
)
from qa_training.utils.domain_registry import DomainRegistry


class ControllerJudgeSurvival:
    def __init__(
        self,
        usecase_command: ConfigManagerUsecaseCommand,
        repo_command: ConfigManagerRepoCommand,
        customer_info_csv_path: str,
        output_path: str,
    ) -> None:
        self._usecase = self._gene_usecase(
            usecase_command=usecase_command, repo_command=repo_command
        )
        self._customer_info_csv_path = customer_info_csv_path
        self._output_path = output_path

    def run(self):
        df_results = self._usecase.judge_survival()
        self._output(output_path=self._output_path, df_results=df_results)

    def initialize(self):
        self._usecase.initialize()
        if os.path.exists(self._output_path):
            os.remove(self._output_path)

    def _output(self, output_path, df_results):
        df_results.to_csv(output_path, index=False)

    def _load_df_customer_info(self, customer_info_csv_path: str) -> pd.DataFrame:
        df_customer_info = pd.read_csv(
            customer_info_csv_path,
        )
        return df_customer_info

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
