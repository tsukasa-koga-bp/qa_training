import pandas as pd
from qa_training.utils.boundary.repo.if_repo_model import IF_RepoModel


class ServicePredict:
    def __init__(self, repo_model: IF_RepoModel) -> None:
        pass

    def run(self, X: pd.DataFrame, y: pd.Series) -> list[bool]:  # noqa: N803
        return [True]
