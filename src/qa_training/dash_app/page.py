import base64
import datetime
import io
from abc import ABC, abstractmethod

import dash_bootstrap_components as dbc
import pandas as pd
from dash import Dash, Input, Output, State, dash_table, dcc, html
from dash.exceptions import PreventUpdate

from qa_training.adapter.controller_create_model import ControllerCreateModel
from qa_training.adapter.controller_judge_survival import ControllerJudgeSurvival
from qa_training.utils.config_manager import (
    ConfigManagerRepoCommand,
    ConfigManagerUsecaseCommand,
)


class CustomPage(ABC):
    @abstractmethod
    def get_title(self):
        pass

    @abstractmethod
    def get_pathname(self):
        pass

    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def set_callback(self, app: Dash):
        pass


class Sidebar:
    def __init__(self, style=None):
        self._title = "Titanic Survial Judge"
        self._discription = "Machine Learning Application Demo for Quality Assurance Lecture Exercise Assignment"
        self.style = {}
        if style is None:
            style = {
                "position": "fixed",
                "top": 0,
                "left": 0,
                "bottom": 0,
                "width": "16rem",
                "padding": "2rem 1rem",
                "background-color": "#f8f9fa",
            }
            self.style = style
        self._pages = []

    def add_page(self, title, href):
        self._pages.append({"title": title, "href": href})

    def render(self):
        nav_items = [
            dbc.NavLink(page["title"], href=page["href"], active="exact")
            for page in self._pages
        ]

        sidebar = html.Div(
            [
                html.H2(self._title, className="display-4"),
                html.Hr(),
                html.P(self._discription, className="lead"),
                dbc.Nav(nav_items, vertical=True, pills=True),
            ],
            style=self.style,
        )
        return sidebar


class HomePage(CustomPage):
    def __init__(self, id: str, pathname: str) -> None:
        self._title = "HomePage"
        self._pathname = pathname

    def get_title(self):
        return self._title

    def get_pathname(self):
        return self._pathname

    def render(self):
        return html.P("This is home")

    def set_callback(self, app: Dash):
        pass


class CreateModelPage(CustomPage):
    def __init__(self, id: str, pathname: str) -> None:
        self._title = "Create Model"
        self._page_name = "create_model"
        self._pathname = pathname
        self._upload_train_data_id = f"{self._page_name}_upload_train_data"
        self._temp_train_data_id = f"{self._page_name}_temp_train_data"
        self._view_train_data_id = f"{self._page_name}_view_train_data"
        self._make_feature_id = f"{self._page_name}_make_feature"
        self._temp_feature_id = f"{self._page_name}_temp_feature"
        self._train_id = f"{self._page_name}_train"
        self._store_id = f"{self._page_name}_store"

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
                    id=self._upload_train_data_id,
                    children=html.Div(["Drag and Drop or ", html.A("Select CSV")]),
                    style={
                        "width": "80%",
                        "height": "50px",
                        "lineHeight": "60px",
                        "borderWidth": "1px",
                        "borderStyle": "dashed",
                        "borderRadius": "5px",
                        "textAlign": "center",
                        "margin": "5% auto",
                    },
                ),
                dcc.Store(id=self._temp_train_data_id, storage_type="session"),
                html.Div(
                    id=self._view_train_data_id,
                    style={
                        "overflow": "auto",
                    },
                ),
                html.Hr(),
                html.P("特徴量作成", className="lead"),
                dbc.Button(
                    "Run", id=self._make_feature_id, color="primary", n_clicks=0
                ),
                dcc.Store(id=self._temp_feature_id, storage_type="session"),
                html.Div(id="table1"),
                html.Hr(),
                html.P("学習", className="lead"),
                dbc.Button("Run", id=self._train_id, color="primary", n_clicks=0),
                html.Div(id="table1"),
                html.Hr(),
                html.P("モデル保存", className="lead"),
                dbc.Button("Run", id=self._store_id, color="primary", n_clicks=0),
                html.Div(id="table1"),
            ]
        )

    def set_callback(self, app: Dash):
        @app.callback(
            Output(self._temp_train_data_id, "data"),
            Input(self._upload_train_data_id, "contents"),
            State(self._upload_train_data_id, "filename"),
            State(self._upload_train_data_id, "last_modified"),
            State(self._temp_train_data_id, "data"),
        )
        def parse_data(contents, filename, last_modified, data):
            if contents is not None:
                content_type, content_string = contents.split(",")
                decoded = base64.b64decode(content_string)
                try:
                    df = pd.read_csv(io.StringIO(decoded.decode("utf-8")))
                except Exception as e:
                    print(e)
                    return None
                return df.to_dict("records"), filename, last_modified
            elif data is not None:
                return data
            else:
                raise PreventUpdate

        @app.callback(
            Output(self._view_train_data_id, "children"),
            Input(self._temp_train_data_id, "data"),
        )
        def update_view_train_data(data):
            if data is None:
                raise PreventUpdate

            raw_data, filename, last_modified = data
            df = pd.DataFrame.from_records(raw_data)
            return html.Div(
                [
                    html.H5(filename),
                    html.H6(datetime.datetime.fromtimestamp(last_modified)),
                    html.H6("The top 10 lines"),
                    dash_table.DataTable(
                        df[:10].to_dict("records"),
                        [{"name": i, "id": i} for i in df.columns],
                    ),
                ]
            )

        @app.callback(
            Output(self._temp_feature_id, "data"),
            Input(self._make_feature_id, "n_clicks"),
            State(self._temp_train_data_id, "data"),
        )
        def run_make_feature(n_clicks, data):
            if data is None:
                raise PreventUpdate

            configs = "configs"
            raw_data, filename, last_modified = data
            df_customer_info = pd.DataFrame.from_records(raw_data)

            usecase_command = ConfigManagerUsecaseCommand(
                usecase_create_model_yaml_path=f"{configs}/usecase/UsecaseCreateModel.yaml",
                usecase_judge_survival_yaml_path=f"{configs}/usecase/UsecaseJudgeSurvival.yaml",
            )

            repo_command = ConfigManagerRepoCommand(
                repo_input_data_yaml_path=f"{configs}/repo/RepoInputData.yaml",
                repo_model_yaml_path=f"{configs}/repo/RepoModel.yaml",
                repo_output_data_yaml_path=f"{configs}/repo/RepoOutputData.yaml",
            )

            controller = ControllerCreateModel(
                usecase_command=usecase_command, repo_command=repo_command
            )

            df_X, df_y = controller.make_features(df_customer_info)
            return df_X.to_dict("records"), df_y.to_dict("records")


class JudgeSurvivalPage(CustomPage):
    def __init__(self, id: str, pathname: str) -> None:
        self._title = "Judge Survival"
        self._page_name = "judge_survival"
        self._pathname = pathname
        self._run_button_id = f"{self._page_name}_run_button"
        self._run_state_id = f"{self._page_name}_run_state"

    def get_title(self):
        return self._title

    def get_pathname(self):
        return self._pathname

    def render(self):
        return html.Div(
            [
                html.H2(self._title, className="display-3"),
                html.Hr(),
                html.P("生存判定", className="lead"),
                dbc.Button("Run", id=self._run_button_id, color="primary", n_clicks=0),
                html.Div(
                    id=self._run_state_id,
                    children="Try push Run",
                ),
            ]
        )

    def set_callback(self, app: Dash):
        @app.callback(
            Output(self._run_state_id, "children"),
            Input(self._run_button_id, "n_clicks"),
            prevent_initial_call=True,
        )
        def update_output(n_clicks):
            configs = "configs"

            try:
                usecase_command = ConfigManagerUsecaseCommand(
                    usecase_create_model_yaml_path=f"{configs}/usecase/UsecaseCreateModel.yaml",
                    usecase_judge_survival_yaml_path=f"{configs}/usecase/UsecaseJudgeSurvival.yaml",
                )

                repo_command = ConfigManagerRepoCommand(
                    repo_input_data_yaml_path=f"{configs}/repo/RepoInputData.yaml",
                    repo_model_yaml_path=f"{configs}/repo/RepoModel.yaml",
                    repo_output_data_yaml_path=f"{configs}/repo/RepoOutputData.yaml",
                )

                controller = ControllerJudgeSurvival(
                    usecase_command=usecase_command, repo_command=repo_command
                )

                controller.run()
                return "success"
            except Exception:
                return "failed"
