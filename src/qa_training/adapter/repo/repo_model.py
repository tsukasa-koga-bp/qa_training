from qa_training.utils.boundary.repo.if_repo_model import IF_RepoModel
from qa_training.utils.override_wrappter import override


class RepoModel(IF_RepoModel):
    def __init__(self, **kwargs) -> None:
        pass

    @override(IF_RepoModel.gene)
    def gene(self) -> None:
        pass
