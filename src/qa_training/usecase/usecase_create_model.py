from typing import Any

import pandas as pd
from qa_training.domain.ml_model import MLModel
from qa_training.domain.service_make_features import ServiceMakeFeatures
from qa_training.domain.service_train import ServiceTrain
from qa_training.utils.boundary.repo.if_repo_input_data import IF_RepoInputData
from qa_training.utils.boundary.repo.if_repo_model import IF_RepoModel
from qa_training.utils.boundary.usecase.if_usecase_create_model import (
    IF_UsecaseCreateModel,
)
from qa_training.utils.logging import log_decorator
from qa_training.utils.override_wrappter import override


class UsecaseCreateModel(IF_UsecaseCreateModel):
    """モデル作成ユースケース."""

    def __init__(
        self,
        repo_model: IF_RepoModel,
        repo_input_data: IF_RepoInputData,
        model_name: str,
        model_parameters: dict[str, Any],
        **kwargs
    ) -> None:
        assert isinstance(repo_model, IF_RepoModel)
        assert isinstance(repo_input_data, IF_RepoInputData)

        self._repo_model = repo_model
        self._repo_input_data = repo_input_data
        self._model_name = model_name
        self._model_parameters = model_parameters

    @override(IF_UsecaseCreateModel.create_model)
    def create_model(self) -> None:
        # データ読み込み
        df_customer_info = self.load_train()

        # 特徴量作成
        df_X, df_y = self.make_features(df_customer_info)

        # 学習
        ml_model = self.train(df_X, df_y)

        # モデルを保存
        self.store(ml_model)

    @override(IF_UsecaseCreateModel.load_train)
    @log_decorator
    def load_train(self) -> pd.DataFrame:
        df_customer_info = self._repo_input_data.load_train()
        return df_customer_info

    @override(IF_UsecaseCreateModel.make_features)
    @log_decorator
    def make_features(
        self, df_customer_info: pd.DataFrame
    ) -> tuple[pd.DataFrame, pd.DataFrame]:
        service_make_features = ServiceMakeFeatures()
        _, df_X, df_y = service_make_features.run(df_customer_info)
        return df_X, df_y

    @override(IF_UsecaseCreateModel.train)
    @log_decorator
    def train(self, df_X: pd.DataFrame, df_y: pd.DataFrame) -> MLModel:
        service_train = ServiceTrain(
            model_name=self._model_name, model_parameters=self._model_parameters
        )
        ml_model = service_train.run(df_X, df_y)
        return ml_model

    @override(IF_UsecaseCreateModel.store)
    @log_decorator
    def store(self, ml_model: MLModel) -> None:
        self._repo_model.store(ml_model)

    @override(IF_UsecaseCreateModel.initialize)
    @log_decorator
    def initialize(self) -> None:
        self._repo_model.initialize()
