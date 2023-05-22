import dash_bootstrap_components as dbc
from dash import Dash, Input, Output, html

from qa_training.adapter.controller_judge_survival import ControllerJudgeSurvival
from qa_training.dash_app.custom_page import CustomPage
from qa_training.utils.config_manager import (
    ConfigManagerRepoCommand,
    ConfigManagerUsecaseCommand,
)


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
