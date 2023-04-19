from qa_training.utils.boundary.repo.if_repo_model import IF_RepoModel
from qa_training.utils.boundary.usecase.if_usecase_create_model import (
    IF_UsecaseCreateModel,
)
from qa_training.utils.override_wrappter import override


class UsecaseCreateModel(IF_UsecaseCreateModel):
    """モデル作成ユースケース"""

    def __init__(self, repo_model: IF_RepoModel, **kwargs) -> None:
        assert isinstance(repo_model, IF_RepoModel)

        self._repo_model = repo_model

    @override
    def init_output(self) -> None:
        pass
