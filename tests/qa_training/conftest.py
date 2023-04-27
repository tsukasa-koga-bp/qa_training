import pytest
from _pytest.fixtures import SubRequest
from py.xml import html
from qa_training.utils.config_manager import (
    ConfigManager,
    ConfigManagerRepoCommand,
    ConfigManagerUsecaseCommand,
)
from qa_training.utils.domain_registry import DomainRegistry

params_yaml = {
    "default": (
        ConfigManagerUsecaseCommand(
            usecase_create_model_yaml_path="tests/common_data/configs/usecase/UsecaseCreateModel.yaml",
            usecase_judge_survival_yaml_path="tests/common_data/configs/usecase/UsecaseJudgeSurvival.yaml",
        ),
        ConfigManagerRepoCommand(
            repo_model_yaml_path="tests/common_data/configs/repo/RepoModel.yaml",
            repo_input_data_yaml_path="tests/common_data/configs/repo/RepoInputData.yaml",
            repo_output_data_yaml_path="tests/common_data/configs/repo/RepoOutputData.yaml",
        ),
    ),
}


@pytest.fixture(
    params=list(params_yaml.values()),
    ids=list(params_yaml.keys()),
)
def commands(
    request: SubRequest,
) -> tuple[ConfigManagerUsecaseCommand, ConfigManagerRepoCommand]:
    usecase_command = request.param[0]
    repo_command = request.param[1]
    return usecase_command, repo_command


@pytest.fixture
def config_manager(
    commands: tuple[ConfigManagerUsecaseCommand, ConfigManagerRepoCommand]
) -> ConfigManager:
    usecase_command = commands[0]
    repo_command = commands[1]
    config_manager = ConfigManager(
        usecase_command=usecase_command, repo_command=repo_command
    )
    return config_manager


@pytest.fixture
def domain_registry(config_manager: ConfigManager) -> DomainRegistry:
    return DomainRegistry(config_manager=config_manager)


def pytest_html_report_title(report):
    report.title = "テスト仕様書"


def pytest_html_results_table_header(cells):
    del cells[1]
    cells.insert(1, html.td("TestFolder"))
    cells.insert(2, html.td("TestScript"))
    cells.insert(3, html.td("TestFunction"))
    cells.insert(4, html.th("Description"))
    cells.insert(5, html.th("Parameter"))
    cells.pop()


def pytest_html_results_table_row(report, cells):
    del cells[1]
    cells.insert(1, html.td(report.test_folder))
    cells.insert(2, html.td(report.test_script))
    cells.insert(3, html.td(report.test_func))
    cells.insert(4, html.td(report.description))
    cells.insert(5, html.td(report.param))
    cells.pop()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    report.test_folder = item.fspath.dirname
    report.test_script = item.fspath.basename
    report.test_func = item.originalname
    report.description = str(item.function.__doc__)
    report.param = item.name.removeprefix(item.originalname)
