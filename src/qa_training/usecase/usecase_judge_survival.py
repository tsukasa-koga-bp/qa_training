from qa_training.utils.boundary.repo.if_repo_cleansed_data import IF_RepoCleansedData
from qa_training.utils.boundary.repo.if_repo_features import IF_RepoFeatures
from qa_training.utils.boundary.repo.if_repo_model import IF_RepoModel
from qa_training.utils.boundary.repo.if_repo_raw_data import IF_RepoRawData
from qa_training.utils.boundary.usecase.if_usecase_judge_survival import (
    IF_UsecaseJudgeSurvival,
)
from qa_training.utils.override_wrappter import override


class UsecaseJudgeSurvival(IF_UsecaseJudgeSurvival):
    """生存判定ユースケース"""

    def __init__(
        self,
        repo_raw_data: IF_RepoRawData,
        repo_cleansed_data: IF_RepoCleansedData,
        repo_features: IF_RepoFeatures,
        repo_model: IF_RepoModel,
        **kwargs
    ) -> None:
        assert isinstance(repo_raw_data, IF_RepoRawData)
        assert isinstance(repo_cleansed_data, IF_RepoCleansedData)
        assert isinstance(repo_features, IF_RepoFeatures)
        assert isinstance(repo_model, IF_RepoModel)

        self._repo_raw_data = repo_raw_data
        self._repo_cleansed_data = repo_cleansed_data
        self._repo_features = repo_features
        self._repo_model = repo_model

    @override
    def init_output(self) -> None:
        pass
