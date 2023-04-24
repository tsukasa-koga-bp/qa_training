import pandas as pd
from qa_training.utils.boundary.repo.if_repo_model import IF_RepoModel


class ServicePredict:
    def __init__(self, repo_model: IF_RepoModel) -> None:
        self._repo_model = repo_model

    def run(self, df_X: pd.DataFrame) -> list[bool]:  # noqa: N803
        model = self._repo_model.load()
        df_y_predicted = model.predict(df_X)
        return [True]
