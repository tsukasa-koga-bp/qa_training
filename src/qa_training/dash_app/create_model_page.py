import base64
import datetime
import io

import dash_bootstrap_components as dbc
import pandas as pd
from dash import Dash, Input, Output, State, dash_table, dcc, html

from qa_training.adapter.controller_create_model import ControllerCreateModel
from qa_training.dash_app.custom_page import CustomPage
from qa_training.utils.config_manager import (
    ConfigManagerRepoCommand,
    ConfigManagerUsecaseCommand,
)


class CreateModelPage(CustomPage):
    def __init__(self, id: str, pathname: str) -> None:
        self._title = "Create Model"
        self._page_name = "create_model"
        self._pathname = pathname
        self._drag_and_drop_train_data_id = (
            f"{self._page_name}_drag_and_drop_train_data"
        )
        self._view_train_data_id = f"{self._page_name}_view_train_data"
        self._make_features_button_id = f"{self._page_name}_make_features_button"
        self._temp_features_id = f"{self._page_name}_temp_features"
        self._view_features_id = f"{self._page_name}_view_features"
        self._train_button_id = f"{self._page_name}_train_button"
        self._temp_model_id = f"{self._page_name}_temp_model"
        self._view_model_id = f"{self._page_name}_view_model"

        self._train_data = pd.DataFrame()
        self._train_data_file_name = ""
        self._train_data_last_modified = 0
        self._change_train_data_id = f"{self._page_name}_change_train_data"

        self._set_controller()

    def _set_controller(self):
        configs = "configs"
        usecase_command = ConfigManagerUsecaseCommand(
            usecase_create_model_yaml_path=f"{configs}/usecase/UsecaseCreateModel.yaml",
            usecase_judge_survival_yaml_path=f"{configs}/usecase/UsecaseJudgeSurvival.yaml",
        )

        repo_command = ConfigManagerRepoCommand(
            repo_input_data_yaml_path=f"{configs}/repo/RepoInputData.yaml",
            repo_model_yaml_path=f"{configs}/repo/RepoModel.yaml",
            repo_output_data_yaml_path=f"{configs}/repo/RepoOutputData.yaml",
        )

        self._controller = ControllerCreateModel(
            usecase_command=usecase_command, repo_command=repo_command
        )

    def get_title(self):
        return self._title

    def get_pathname(self):
        return self._pathname

    def render(self):
        return html.Div(
            [
                html.H2(self._title, className="display-3"),
                html.Hr(),
                html.P("学習データ読み込み", className="lead"),
                dcc.Upload(
                    id=self._drag_and_drop_train_data_id,
                    children=html.Div(["Drag and Drop or ", html.A("Select CSV")]),
                    style={
                        "width": "80%",
                        "height": "50px",
                        "lineHeight": "60px",
                        "borderWidth": "1px",
                        "borderStyle": "dashed",
                        "borderRadius": "5px",
                        "textAlign": "center",
                        "margin": "1% auto",
                    },
                ),
                html.Div(
                    id=self._view_train_data_id,
                ),
                dcc.Store(id=self._change_train_data_id),
                html.Hr(),
                html.P("特徴量作成", className="lead"),
                dbc.Button(
                    "Run",
                    id=self._make_features_button_id,
                    color="primary",
                    n_clicks=0,
                    outline=True,
                ),
                # dcc.Store(id=self._temp_features_id, storage_type="local"),
                html.Br(),
                html.Br(),
                html.Div(
                    id=self._view_features_id,
                    style={
                        "overflow": "auto",
                    },
                ),
                html.Hr(),
                html.P("学習", className="lead"),
                dbc.Button(
                    "Run",
                    id=self._train_button_id,
                    color="primary",
                    n_clicks=0,
                    outline=True,
                ),
                # dcc.Store(id=self._temp_model_id, storage_type="local"),
                html.Br(),
                html.Br(),
                html.Div(
                    id=self._view_model_id,
                    style={
                        "overflow": "auto",
                    },
                ),
            ]
        )

    def set_callback(self, app: Dash):
        self._set_callback_from_drag_and_drop(app)
        # self._set_callback_from_push_make_feature_button(app)
        # self._set_callback_from_push_train(app)

    def _set_callback_from_drag_and_drop(self, app):
        @app.callback(
            Output(self._view_train_data_id, "children"),
            Output(self._change_train_data_id, "data"),
            Input(self._drag_and_drop_train_data_id, "contents"),
            State(self._drag_and_drop_train_data_id, "filename"),
            State(self._drag_and_drop_train_data_id, "last_modified"),
        )
        def on_drag_and_drop(contents, filename, last_modified):
            """csvファイルがD&Dされると読込む."""
            line_num = 5

            # データ更新
            if contents is not None:  # 新しいデータがアップロード
                try:
                    if ".csv" not in filename:
                        raise Exception("csvファイルでない")

                    content_type, content_string = contents.split(",")
                    decoded = base64.b64decode(content_string)
                    df = pd.read_csv(io.StringIO(decoded.decode("utf-8")))

                    self._train_data = df
                    self._train_data_file_name = filename
                    self._train_data_last_modified = last_modified
                except Exception:
                    self._train_data = pd.DataFrame()
                    self._train_data_file_name = ""
                    self._train_data_last_modified = 0

            # データ表示
            if len(self._train_data) > 0:  # データが存在する
                df = self._train_data

                return (
                    html.Div(
                        [
                            dbc.Badge("Completed", color="success", className="me-1"),
                            html.H5(self._train_data_file_name),
                            html.H6(
                                datetime.datetime.fromtimestamp(
                                    self._train_data_last_modified
                                )
                            ),
                            html.H6(f"The top {line_num} lines"),
                            html.Div(
                                [
                                    dash_table.DataTable(
                                        df[:line_num].to_dict("records"),
                                        [{"name": i, "id": i} for i in df.columns],
                                    ),
                                ],
                                style={
                                    "overflow": "auto",
                                },
                            ),
                        ]
                    ),
                    True,
                )

            return (
                dbc.Badge("Not Completed", color="danger", className="me-1"),
            ), False

    """
    def _set_callback_from_push_make_feature_button(self, app):
        @app.callback(
            Output(self._temp_features_id, "data"),
            Input(self._make_features_button_id, "n_clicks"),
            State(self._temp_train_data_id, "data"),
        )
        def on_make_feature_button(n_clicks, train_data):
            if train_data is None:
                return None

            raw_data, filename, last_modified = train_data
            try:
                df_customer_info = pd.DataFrame.from_records(raw_data)

                df_X, df_y = self._controller.make_features(df_customer_info)
                return df_X.to_dict("records"), df_y.to_dict("records")
            except Exception as e:
                print(e)
                return "Error"

        @app.callback(
            Output(self._view_features_id, "children"),
            Input(self._temp_features_id, "data"),
            Input(self._temp_train_data_id, "data"),
        )
        def update_view_features_data(features_data, train_data):
            line_num = 5

            if train_data is None or features_data == "Error" or features_data is None:
                return (
                    dbc.Badge(
                        "Not Completed",
                        color="danger",
                        className="me-1",
                    ),
                )

            df_X_raw, df_y_raw = features_data

            if len(df_y_raw) == 0:
                return (
                    dbc.Badge(
                        "Not Completed",
                        color="danger",
                        className="me-1",
                    ),
                )

            df_X = pd.DataFrame.from_records(df_X_raw)
            df_y = pd.DataFrame.from_records(df_y_raw)

            return html.Div(
                [
                    dbc.Badge("Completed", color="success", className="me-1"),
                    html.H6(f"The top {line_num} lines"),
                    dbc.Row(
                        [
                            dbc.Col(html.H5("特徴量"), width=6),
                            dbc.Col(html.H5("ラベル"), width=6),
                        ]
                    ),
                    dbc.Row(
                        [
                            dbc.Col(
                                dash_table.DataTable(
                                    data=df_X[:line_num].to_dict("records"),
                                    columns=[
                                        {"name": i, "id": i} for i in df_X.columns
                                    ],
                                ),
                                width=6,
                            ),
                            dbc.Col(
                                dash_table.DataTable(
                                    data=df_y[:line_num].to_dict("records"),
                                    columns=[
                                        {"name": i, "id": i} for i in df_y.columns
                                    ],
                                ),
                                width=6,
                            ),
                        ]
                    ),
                ]
            )

    def _set_callback_from_push_train(self, app):
        @app.callback(
            Output(self._temp_model_id, "data"),
            Input(self._train_button_id, "n_clicks"),
            Input(self._temp_features_id, "data"),
        )
        def on_train_button(n_clicks, features_data):
            if features_data is None or features_data == "Error":
                return None

            df_X_raw, df_y_raw = features_data

            try:
                df_X = pd.DataFrame.from_records(df_X_raw)
                df_y = pd.DataFrame.from_records(df_y_raw)

                ml_model = self._controller.train(df_X=df_X, df_y=df_y)
                self._controller.store(ml_model=ml_model)
                return "Success"
            except Exception as e:
                print(e)
                return "Error"

        @app.callback(
            Output(self._view_model_id, "children"),
            Input(self._temp_model_id, "data"),
            Input(self._temp_features_id, "data"),
            Input(self._temp_train_data_id, "data"),
        )
        def update_view_model(model_data, features_data, train_data):
            if (
                train_data is None
                or features_data is None
                or features_data == "Error"
                or model_data == "Error"
                or model_data is None
            ):
                return (
                    dbc.Badge(
                        "Not Completed",
                        color="danger",
                        className="me-1",
                    ),
                )

            if model_data == "Success":
                return (
                    dbc.Badge(
                        "Completed",
                        color="success",
                        className="me-1",
                    ),
                )
    """
