from qa_training.utils.boundary.repo.if_repo_features import IF_RepoFeatures
from qa_training.utils.override_wrappter import override


class RepoFeatures(IF_RepoFeatures):
    def __init__(self, **kwargs) -> None:
        pass

    @override(IF_RepoFeatures.initialize)
    def initialize(self) -> None:
        pass
