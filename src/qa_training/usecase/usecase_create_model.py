from qa_training.domain.service_load_dataset import ServiceLoadDataset
from qa_training.domain.service_make_features import ServiceMakeFeatures
from qa_training.domain.service_train import ServiceTrain
from qa_training.utils.boundary.repo.if_repo_model import IF_RepoModel
from qa_training.utils.boundary.usecase.if_usecase_create_model import (
    IF_UsecaseCreateModel,
)
from qa_training.utils.override_wrappter import override


class UsecaseCreateModel(IF_UsecaseCreateModel):
    """モデル作成ユースケース."""

    def __init__(self, repo_model: IF_RepoModel, csv_path: str, **kwargs) -> None:
        assert isinstance(repo_model, IF_RepoModel)

        self._repo_model = repo_model
        self._csv_path = csv_path

    @override(IF_UsecaseCreateModel.create_model)
    def create_model(self) -> None:
        # データ読み込み
        service_load_dataset = ServiceLoadDataset()
        df_customer_info = service_load_dataset.run(self._csv_path)

        # 特徴量作成
        service_make_features = ServiceMakeFeatures()
        _, df_X, df_y = service_make_features.run(df_customer_info)

        # 学習
        service_train = ServiceTrain(repo_model=self._repo_model)
        ml_model = service_train.run(df_X, df_y)

        # モデルを保存
        self._repo_model.store(ml_model)

    @override(IF_UsecaseCreateModel.initialize)
    def initialize(self) -> None:
        self._repo_model.initialize()
