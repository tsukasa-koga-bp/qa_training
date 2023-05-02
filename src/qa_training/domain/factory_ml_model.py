from typing import Any

from qa_training.domain.ml_model import MLModel
from qa_training.utils.logging import log_decorator
from sklearn.ensemble import RandomForestClassifier


class FactoryMLModel:
    """モデルを生成する"""

    @log_decorator
    def gene_from_parameters(
        self, model_name: str, model_parameters: dict[str, Any]
    ) -> MLModel:
        if model_name == "RandomForest":
            model = RandomForestClassifier(**model_parameters)  # type: ignore
        else:
            raise ValueError
        return self.gene_from_model(model)

    @log_decorator
    def gene_from_model(self, model: Any) -> MLModel:
        return MLModel(model=model)
