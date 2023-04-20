from qa_training.domain.customer_info import CustomerInfo
from qa_training.domain.service_make_features import ServiceMakeFeatures
from qa_training.domain.service_predict import ServicePredict
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
    def judge_survival(self, list_customer_info: list[CustomerInfo]) -> bool:
        # 特徴量作成
        service_make_features = ServiceMakeFeatures()
        y, X = service_make_features.run(list_customer_info)  # noqa: N806

        # モデルで予測
        service_predict = ServicePredict(repo_model=self._repo_model)
        list_survival = service_predict.run(y, X)
        is_survival = list_survival[0]

        return is_survival

    @override(IF_UsecaseJudgeSurvival.initialize)
    def initialize(self) -> None:
        self._repo_model.initialize()
