from qa_training.utils.config_manager import ConfigManager


def test_config_manager_initialize(config_manager: ConfigManager) -> None:
    """Configを読み込んで, ConfigManagerを初期化できるか."""
    assert type(config_manager) is ConfigManager


# Usecase
def test_params_for_usecase(config_manager: ConfigManager) -> None:
    """Usecase関連のパラメータが正しく読み込めているか."""
    classname, params = config_manager.params_for_usecase_create_model()
    assert type(classname) is str and type(params) is dict

    classname, params = config_manager.params_for_usecase_judge_survival()
    assert type(classname) is str and type(params) is dict


# Repository
def test_params_for_repo(config_manager: ConfigManager) -> None:
    """Repository関連のパラメータが正しく読み込めているか."""
    classname, params = config_manager.params_for_repo_model()
    assert type(classname) is str and type(params) is dict
