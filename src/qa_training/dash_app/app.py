from abc import ABC, abstractmethod

import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html


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


class Sidebar:
    def __init__(self, style=None):
        self.style = style if style else {}
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
                html.H2("Sidebar", className="display-4"),
                html.Hr(),
                html.P(
                    "A simple sidebar layout with navigation links", className="lead"
                ),
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


class Page1(CustomPage):
    def __init__(self, id: str, pathname: str) -> None:
        self._title = "Page 1"
        self._pathname = pathname

    def get_title(self):
        return self._title

    def get_pathname(self):
        return self._pathname

    def render(self):
        return html.P("This is the content of page 1. Yay!")


class Page2(CustomPage):
    def __init__(self, id: str, pathname: str) -> None:
        self._title = "Page 2"
        self._pathname = pathname

    def get_title(self):
        return self._title

    def get_pathname(self):
        return self._pathname

    def render(self):
        return html.P("Oh cool, this is page 2!")


class MyApp:
    def __init__(self):
        self.app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
        self._pages: list[CustomPage] = []

    def set_pages(self, pages: list[CustomPage]):
        self._pages = pages

    def set_layout(self):
        sidebar = self._create_sidebar()
        content = self._create_content()

        for page in self._pages:
            title = page.get_title()
            pathname = page.get_pathname()
            sidebar.add_page(title, pathname)

        self.app.layout = html.Div([dcc.Location(id="url"), sidebar.render(), content])

    def _create_sidebar(self) -> Sidebar:
        sidebar_style = {
            "position": "fixed",
            "top": 0,
            "left": 0,
            "bottom": 0,
            "width": "16rem",
            "padding": "2rem 1rem",
            "background-color": "#f8f9fa",
        }

        return Sidebar(style=sidebar_style)

    def _create_content(self):
        CONTENT_STYLE = {
            "margin-left": "18rem",
            "margin-right": "2rem",
            "padding": "2rem 1rem",
        }
        content = html.Div(id="page-content", style=CONTENT_STYLE)
        return content

    def run(self, debug=False):
        self.set_callbacks()
        self.app.run_server(debug=debug, port=8888)

    def set_callbacks(self):
        @self.app.callback(
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


if __name__ == "__main__":
    homepage = HomePage(id="homepage", pathname="/")
    page1 = Page1(id="page1", pathname="/page-1")
    page2 = Page2(id="page2", pathname="/page-2")
    page3 = Page2(id="page3", pathname="/page-3")

    app = MyApp()
    app.set_pages(pages=[homepage, page1, page2, page3])
    app.set_layout()
    app.run(debug=True)
