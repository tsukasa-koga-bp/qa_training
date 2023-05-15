from abc import ABC, abstractmethod

import dash_bootstrap_components as dbc
from dash import Dash, Input, Output, State, dcc, html


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
                    children="Enter a value and press submit",
                ),
            ]
        )

    def set_callback(self, app: Dash):
        @app.callback(
            Output(self._run_state_id, "children"),
            Input(self._run_button_id, "n_clicks"),
        )
        def update_output(n_clicks):
            return f"The button has been clicked {n_clicks} times"


class JudgeSurvivalPage(CustomPage):
    def __init__(self, id: str, pathname: str) -> None:
        self._title = "Judge Survival"
        self._pathname = pathname

    def get_title(self):
        return self._title

    def get_pathname(self):
        return self._pathname

    def render(self):
        return html.P("Oh cool, this is page 2!")

    def set_callback(self, app: Dash):
        pass


class MyApp:
    def __init__(self):
        self._app = Dash(
            external_stylesheets=[dbc.themes.BOOTSTRAP],
            suppress_callback_exceptions=True,
        )
        self._pages: list[CustomPage] = []
        self._sidebar: Sidebar

    def set_pages(self, pages: list[CustomPage]):
        self._pages = pages

    def set_sidebar(self, sidebar: Sidebar):
        self._sidebar = sidebar

    def set_layout(self):
        content = self._create_content()

        for page in self._pages:
            title = page.get_title()
            pathname = page.get_pathname()
            self._sidebar.add_page(title, pathname)

        self._app.layout = html.Div(
            [dcc.Location(id="url"), self._sidebar.render(), content]
        )

    def _create_content(self):
        CONTENT_STYLE = {
            "margin-left": "18rem",
            "margin-right": "2rem",
            "padding": "2rem 1rem",
        }
        content = html.Div(id="page-content", style=CONTENT_STYLE)
        return content

    def run(self, debug=False):
        self._set_callbacks()
        self._app.run_server(debug=debug, port=8888)

    def _set_callbacks(self):
        @self._app.callback(
            Output("page-content", "children"), [Input("url", "pathname")]
        )
        def render_page_content(pathname):
            for page in self._pages:
                if pathname == page.get_pathname():
                    return page.render()

            # If the user tries to reach a different page, return a 404 message
            return html.Div(
                [
                    html.H1("404: Not found", className="text-danger"),
                    html.Hr(),
                    html.P(f"The pathname {pathname} was not recognised..."),
                ],
                className="p-3 bg-light rounded-3",
            )

        for page in self._pages:
            page.set_callback(self._app)


if __name__ == "__main__":
    sidebar = Sidebar()
    homepage = HomePage(id="homepage", pathname="/")
    create_model_page = CreateModelPage(
        id="create_model_page", pathname="/create_model_page"
    )
    judge_survival_page = JudgeSurvivalPage(
        id="judge_survival_page", pathname="/judge_survival_page"
    )

    app = MyApp()
    app.set_pages(pages=[homepage, create_model_page, judge_survival_page])
    app.set_sidebar(sidebar=sidebar)
    app.set_layout()
    app.run(debug=True)
