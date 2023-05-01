import pandas as pd
import pytest
from _pytest.fixtures import SubRequest
from qa_training.domain.ml_model import MLModel
from qa_training.domain.service_predict import ServicePredict
from qa_training.domain.service_train import ServiceTrain
from qa_training.utils.domain_registry import DomainRegistry
from qa_training.utils.my_assert_frame_equal import MyAssert

params = {
    "RandomForest": (
        "RandomForest",
        {
            "criterion": "entropy",
            "max_depth": 4,
            "n_estimators": 100,
            "random_state": 62,
        },
    )
}


@pytest.fixture(params=params.values(), ids=params.keys())  # type: ignore
def fixture_run(domain_registry: DomainRegistry, request: SubRequest):
    model_name = request.param[0]
    model_parameters = request.param[1]

    service_train = ServiceTrain(
        model_name=model_name, model_parameters=model_parameters
    )
    service_predict = ServicePredict()

    df_X = pd.read_csv(
        "tests/common_data/df_X.csv",
    )
    df_y = pd.read_csv(
        "tests/common_data/df_y.csv",
    )
    df_y_pred_expected = pd.read_csv(
        "tests/common_data/df_y_pred_expected.csv",
    )

    ml_model = service_train.run(df_X, df_y)

    return service_predict, df_X, ml_model, df_y_pred_expected


def test_run(fixture_run: tuple[ServicePredict, pd.DataFrame, MLModel, pd.DataFrame]):
    (
        service_predict,
        df_X,
        ml_model,
        df_y_pred_expected,
    ) = fixture_run

    df_y_pred = service_predict.run(df_X=df_X, ml_model=ml_model)
    MyAssert().assert_df(df_results=df_y_pred, df_expected=df_y_pred_expected)
