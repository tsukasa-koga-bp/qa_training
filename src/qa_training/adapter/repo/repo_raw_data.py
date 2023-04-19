from qa_training.utils.boundary.repo.if_repo_raw_data import IF_RepoRawData
from qa_training.utils.override_wrappter import override


class RepoRawData(IF_RepoRawData):
    def __init__(self, **kwargs) -> None:
        pass

    @override(IF_RepoRawData.initialize)
    def initialize(self) -> None:
        pass
