from qa_training.utils.boundary.repo.if_repo_cleansed_data import IF_RepoCleansedData
from qa_training.utils.override_wrappter import override


class RepoCleansedData(IF_RepoCleansedData):
    def __init__(self, **kwargs) -> None:
        pass

    @override(IF_RepoCleansedData.initialize)
    def initialize(self) -> None:
        pass
