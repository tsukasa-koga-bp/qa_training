import json
import logging
from logging.handlers import TimedRotatingFileHandler

from pythonjsonlogger import jsonlogger

log_path = "log"


class FactoryLogger:
    """ロガーを生成する"""

    def __init__(self) -> None:
        self._general_logger = self._gene_general_logger()

    def get_general_logger(self):
        """ロガーの取得"""
        return self._general_logger

    def _gene_general_logger(self):
        # 汎用ロガーの生成
        logger = logging.getLogger("General")

        # ロギングレベルの設定（デフォルト）
        logger.setLevel(logging.INFO)

        # json形式のログフォーマット　参考URL：https://github.com/madzak/python-json-logger
        formatter = jsonlogger.JsonFormatter(
            "%(asctime)s %(levelname)8s %(message)s %(funcName)s %(args)s %(time)f %(processName)s %(threadName)s",
            json_ensure_ascii=False,
        )

        # ファイル出力系ハンドラ
        file_handler = self._get_file_handler(f"{log_path}/general-log.log")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        return logger

    def get_error_logger(self) -> logging.Logger:
        """Error用ロガー生成"""

        # ロガーの生成
        logger = logging.getLogger("ERROR")

        # ロギングレベルの設定（デフォルト）
        logger.setLevel(logging.ERROR)

        # ファイル出力系ハンドラ
        file_handler = self._get_file_handler(f"{log_path}/error-log")
        file_handler.setFormatter(CustomLogFormatter())
        logger.addHandler(file_handler)

        return logger

    def _get_file_handler(self, log_name: str) -> TimedRotatingFileHandler:
        """ファイル出力用のハンドラー取得

        Args:
            log_name (str): ログファイル出力先

        Returns:
            TimedRotatingFileHandler: ハンドラー
        """

        handler = TimedRotatingFileHandler(
            log_name,  # TimeRotationgFileHandler使用時は拡張子をつけない
            when="M",
            backupCount=10,  # 保持数
            interval=60,  # 保持単位
            encoding="utf-8",
        )

        return handler


# 参考元: https://qiita.com/hoto17296/items/fa840823245fa4e7517d
class CustomLogFormatter(logging.Formatter):
    """ログをJSONで出力するフォーマッタ"""

    def format(self, record: logging.LogRecord) -> str:
        try:
            data = vars(record)
            if "exc_info" in data:
                # exc_infoはjson形式にできないので抽出して変換
                exc_info = data["exc_info"]
                data["traceback"] = self.formatException(exc_info).splitlines()
                # exc_infoがないとテストコードでエラーになるので空のデータにする
                data["exc_info"] = ""
            return json.dumps(data, ensure_ascii=False)
        except Exception:
            return super().format(record)
