import os

import pandas as pd

from qa_training.utils.boundary.repo.if_repo_output_data import IF_RepoOutputData
from qa_training.utils.logging import log_decorator
from qa_training.utils.override_wrappter import override


class RepoOutputData(IF_RepoOutputData):
    def __init__(self, output_csv_path, **kwargs) -> None:
        self._output_csv_path = output_csv_path

    @override(IF_RepoOutputData.store)
    @log_decorator
    def store(self, df_results: pd.DataFrame) -> None:
        df_results.to_csv(self._output_csv_path, index=False)

    @override(IF_RepoOutputData.exist_results)
    @log_decorator
    def exist_results(self) -> bool:
        return os.path.exists(self._output_csv_path)

    @override(IF_RepoOutputData.initialize)
    @log_decorator
    def initialize(self) -> None:
        if self.exist_results():
            os.remove(self._output_csv_path)
