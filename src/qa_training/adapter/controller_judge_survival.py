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


class ControllerCreateModel:
    def run(
        self,
        usecase_command: ConfigManagerUsecaseCommand,
        repo_command: ConfigManagerRepoCommand,
        customer_info_csv_path: str,
        output_path: str,
    ):
        usecase = self._gene_usecase(
            usecase_command=usecase_command, repo_command=repo_command
        )

        df_customer_info = self._load_df_customer_info(customer_info_csv_path)

        df_results = usecase.judge_survival(df_customer_info=df_customer_info)
        self._output(output_path=output_path, df_results=df_results)

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
