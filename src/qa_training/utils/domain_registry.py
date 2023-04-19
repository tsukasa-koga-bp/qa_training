from qa_training.adapter.repo.repo_cleansed_data import RepoCleansedData
from qa_training.adapter.repo.repo_features import RepoFeatures
from qa_training.adapter.repo.repo_model import RepoModel
from qa_training.adapter.repo.repo_raw_data import RepoRawData
from qa_training.usecase.usecase_create_model import UsecaseCreateModel
from qa_training.usecase.usecase_judge_survival import UsecaseJudgeSurvival
from qa_training.utils.boundary.repo.if_repo_features import IF_RepoFeatures
from qa_training.utils.boundary.repo.if_repo_model import IF_RepoModel
from qa_training.utils.boundary.repo.if_repo_raw_data import IF_RepoRawData
from qa_training.utils.boundary.usecase.if_usecase_create_model import (
    IF_UsecaseCreateModel,
)
from qa_training.utils.boundary.usecase.if_usecase_judge_survival import (
    IF_UsecaseJudgeSurvival,
)
from qa_training.utils.config_manager import ConfigManager


class DomainRegistry:
    """CongiManagerの返り値を元に抽象クラスの依存解決をする."""

    def __init__(self, config_manager: ConfigManager) -> None:
        assert type(config_manager) is ConfigManager
        self._config_manager = config_manager

    # Usecase
    def usecase_judge_survival(self) -> IF_UsecaseJudgeSurvival:
        (
            classname,
            dict_params,
        ) = self._config_manager.params_for_usecase_judge_survival()

        if classname == UsecaseJudgeSurvival.__name__:
            repo_model = self.repo_model()
            return UsecaseJudgeSurvival(
                repo_model=repo_model,
                **dict_params,
            )
        else:
            raise ValueError

    def usecase_create_model(self) -> IF_UsecaseCreateModel:
        (
            classname,
            dict_params,
        ) = self._config_manager.params_for_usecase_create_model()

        if classname == UsecaseCreateModel.__name__:
            repo_raw_data = self.repo_raw_data()
            repo_cleansed_repo = self.repo_cleansed_data()
            repo_features = self.repo_features()
            repo_model = self.repo_model()
            return UsecaseCreateModel(
                repo_raw_data=repo_raw_data,
                repo_cleansed_data=repo_cleansed_repo,
                repo_features=repo_features,
                repo_model=repo_model,
                **dict_params,
            )
        else:
            raise ValueError

    # Repository
    def repo_raw_data(self) -> IF_RepoRawData:
        classname, dict_params = self._config_manager.params_for_repo_raw_data()
        if classname == RepoRawData.__name__:
            return RepoRawData(**dict_params)
        else:
            raise ValueError

    def repo_cleansed_data(self) -> IF_RepoRawData:
        classname, dict_params = self._config_manager.params_for_repo_cleansed_data()
        if classname == RepoCleansedData.__name__:
            return RepoCleansedData(**dict_params)
        else:
            raise ValueError

    def repo_features(self) -> IF_RepoFeatures:
        classname, dict_params = self._config_manager.params_for_repo_features()
        if classname == RepoFeatures.__name__:
            return RepoFeatures(**dict_params)
        else:
            raise ValueError

    def repo_model(self) -> IF_RepoModel:
        classname, dict_params = self._config_manager.params_for_repo_model()
        if classname == RepoModel.__name__:
            return RepoModel(**dict_params)
        else:
            raise ValueError
