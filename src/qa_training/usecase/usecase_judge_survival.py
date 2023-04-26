import pandas as pd
from qa_training.domain.service_make_features import ServiceMakeFeatures
from qa_training.domain.service_predict import ServicePredict
from qa_training.utils.boundary.repo.if_repo_input_data import IF_RepoInputData
from qa_training.utils.boundary.repo.if_repo_model import IF_RepoModel
from qa_training.utils.boundary.repo.if_repo_output_data import IF_RepoOutputData
from qa_training.utils.boundary.usecase.if_usecase_judge_survival import (
    IF_UsecaseJudgeSurvival,
)
from qa_training.utils.override_wrappter import override


class UsecaseJudgeSurvival(IF_UsecaseJudgeSurvival):
    """生存判定ユースケース."""

    def __init__(
        self,
        repo_model: IF_RepoModel,
        repo_input_data: IF_RepoInputData,
        repo_output_data: IF_RepoOutputData,
        **kwargs
    ) -> None:
        assert isinstance(repo_model, IF_RepoModel)
        assert isinstance(repo_input_data, IF_RepoInputData)
        assert isinstance(repo_output_data, IF_RepoOutputData)
        self._repo_model = repo_model
        self._repo_input_data = repo_input_data
        self._repo_output_data = repo_output_data

    @override(IF_UsecaseJudgeSurvival.judge_survival)
    def judge_survival(self) -> None:
        # データ読み込み
        df_customer_info = self._repo_input_data.load_test()

        # 特徴量作成
        service_make_features = ServiceMakeFeatures()
        df_id, df_X, _ = service_make_features.run(df_customer_info)

        # モデルをロード
        ml_model = self._repo_model.load()

        # モデルで予測
        service_predict = ServicePredict()
        df_y_pred = service_predict.run(df_X=df_X, ml_model=ml_model)

        # 結果作成
        df_results = pd.concat([df_id, df_X, df_y_pred], axis=1)

        # 結果保存
        self._repo_output_data.store(df_results=df_results)

    @override(IF_UsecaseJudgeSurvival.initialize)
    def initialize(self) -> None:
        self._repo_model.initialize()
        self._repo_output_data.initialize()
