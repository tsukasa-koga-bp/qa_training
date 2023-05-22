from abc import ABC, abstractmethod

from dash import Dash


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
