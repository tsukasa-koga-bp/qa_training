import dash_bootstrap_components as dbc
from dash import html


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
