import pandas as pd

from qa_training.utils.boundary.repo.if_repo_input_data import IF_RepoInputData
from qa_training.utils.logging import log_decorator
from qa_training.utils.override_wrappter import override


class RepoInputData(IF_RepoInputData):
    def __init__(self, input_train_csv_path, input_test_csv_path, **kwargs) -> None:
        self._input_train_csv_path = input_train_csv_path
        self._input_test_csv_path = input_test_csv_path

    @override(IF_RepoInputData.load_train)
    @log_decorator
    def load_train(self) -> pd.DataFrame:
        df_customer_info = pd.read_csv(self._input_train_csv_path)
        return df_customer_info

    @override(IF_RepoInputData.load_test)
    @log_decorator
    def load_test(self) -> pd.DataFrame:
        df_customer_info = pd.read_csv(self._input_test_csv_path)
        return df_customer_info
