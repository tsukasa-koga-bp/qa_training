import os
import pickle

from qa_training.domain.factory_ml_model import FactoryMLModel
from qa_training.domain.ml_model import MLModel
from qa_training.utils.boundary.repo.if_repo_model import IF_RepoModel
from qa_training.utils.override_wrappter import override


class RepoModel(IF_RepoModel):
    def __init__(self, model_path, **kwargs) -> None:
        self._model_path = model_path

    @override(IF_RepoModel.load)
    def load(self) -> MLModel:
        with open(self._model_path, "rb") as file:
            model = pickle.load(file)
        return FactoryMLModel().gene_from_model(model=model)

    @override(IF_RepoModel.store)
    def store(self, ml_model: MLModel) -> None:
        with open(self._model_path, "wb") as file:
            pickle.dump(ml_model.get_model(), file)

    @override(IF_RepoModel.exist_model)
    def exist_model(self) -> bool:
        return os.path.exists(self._model_path)

    @override(IF_RepoModel.initialize)
    def initialize(self) -> None:
        if self.exist_model():
            os.remove(self._model_path)
