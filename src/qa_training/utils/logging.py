import inspect
import time
from functools import wraps

import pandas as pd

from qa_training.utils.factory_logger import FactoryLogger

general_logger = FactoryLogger().get_general_logger()


def log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        try:
            result = func(*args, **kwargs)
            end_time = time.time()
            # 計測
            total_time = round(end_time - start_time, 4)

            # クラス名取得
            class_name = (
                args[0].__class__.__name__
                if args and hasattr(args[0], "__class__")
                else "No class"
            )

            non_self_kwargs = _get_non_self_kwargs(func=func, args=args, kwargs=kwargs)

            args_for_logging = _transform_kwargs(True, non_self_kwargs)

            general_logger.info(
                {
                    "message": "",
                    "funcName": class_name + "." + func.__name__,
                    "time": total_time,
                    "args": args_for_logging,
                }
            )
            return result
        except Exception as e:
            general_logger.error(
                {"message": e.__class__.__name__, "funcName": func.__name__}
            )
            raise

    return wrapper


def _get_non_self_kwargs(func, args: tuple, kwargs: dict):
    # funcの引数情報を取得
    sig = inspect.signature(func)
    parameters = sig.parameters

    # self以外の引数を取得
    non_self_kwargs = {
        k: v for k, v in list(zip(parameters.keys(), args)) if k != "self"
    }
    non_self_kwargs.update(kwargs)

    return non_self_kwargs


def _transform_kwargs(with_kwargs: bool, kwargs: dict) -> list:
    """ロギング用　引数変換

    出力が長くなる型の引数を型名に変換する(引数保存がない場合は引数を無視）

    Args:
        with_args (bool): 引数保存の有無
        args (tuple): 元々の引数

    Returns:
        list: 変換後の引数
    """

    if with_kwargs is False:
        return ["not_recoded"]
    if len(kwargs) == 0:
        return []

    args_for_logging = []
    for k, v in kwargs.items():
        if type(v) in [list, pd.DataFrame, dict, bytes]:
            args_for_logging.append(k)
        else:
            args_for_logging.append(v)

    return args_for_logging
