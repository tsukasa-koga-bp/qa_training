import pandas as pd
from qa_training.utils.boundary.repo.if_repo_model import IF_RepoModel


class ServiceTrain:
    def __init__(self, repo_model: IF_RepoModel) -> None:
        self._repo_model = repo_model

    def run(self, df_X: pd.DataFrame, df_y: pd.DataFrame) -> bool:
        return self._repo_model.exist_model()
