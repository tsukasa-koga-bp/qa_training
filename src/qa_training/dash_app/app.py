import dash_bootstrap_components as dbc
from dash import Dash, Input, Output, dcc, html

from qa_training.dash_app.page import (
    CreateModelPage,
    CustomPage,
    HomePage,
    JudgeSurvivalPage,
    Sidebar,
)


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


def dash_main():
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


if __name__ == "__main__":
    dash_main()
