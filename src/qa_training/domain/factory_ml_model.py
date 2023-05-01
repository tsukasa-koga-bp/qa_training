from typing import Any

from qa_training.domain.ml_model import MLModel
from sklearn.ensemble import RandomForestClassifier


class FactoryMLModel:
    def gene_from_parameters(
        self, model_name: str, model_parameters: dict[str, Any]
    ) -> MLModel:
        if model_name == "RandomForest":
            model = RandomForestClassifier(**model_parameters)  # type: ignore
        else:
            raise ValueError
        return self.gene_from_model(model)

    def gene_from_model(self, model: Any):
        return MLModel(model=model)
