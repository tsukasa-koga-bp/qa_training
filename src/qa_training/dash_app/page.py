from abc import ABC, abstractmethod

import dash_bootstrap_components as dbc
from dash import Dash, Input, Output, html

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
                html.P("モデル作成", className="lead"),
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

                controller = ControllerCreateModel(
                    usecase_command=usecase_command, repo_command=repo_command
                )

                controller.run()
                return "success"
            except Exception:
                return "failed"


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
