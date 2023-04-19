from qa_training.utils.boundary.repo.if_repo_model import IF_RepoModel
from qa_training.utils.boundary.usecase.if_usecase_judge_survival import (
    IF_UsecaseJudgeSurvival,
)
from qa_training.utils.override_wrappter import override


class UsecaseJudgeSurvival(IF_UsecaseJudgeSurvival):
    """生存判定ユースケース"""

    def __init__(self, repo_model: IF_RepoModel, **kwargs) -> None:
        assert isinstance(repo_model, IF_RepoModel)
        self._repo_model = repo_model

    @override(IF_UsecaseJudgeSurvival.judge_survival)
    def judge_survival(self) -> bool:
        return True

    @override(IF_UsecaseJudgeSurvival.initialize)
    def initialize(self) -> None:
        pass
