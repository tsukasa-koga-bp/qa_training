from qa_training.domain.ml_model import MLModel
from qa_training.utils.boundary.repo.if_repo_model import IF_RepoModel
from qa_training.utils.override_wrappter import override


class RepoModel(IF_RepoModel):
    def __init__(self, **kwargs) -> None:
        pass

    @override(IF_RepoModel.load)
    def load(self) -> MLModel:
        return MLModel()

    @override(IF_RepoModel.initialize)
    def initialize(self) -> None:
        pass
