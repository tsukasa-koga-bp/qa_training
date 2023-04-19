from abc import ABC, abstractmethod


class IF_UsecaseCreateModel(ABC):
    """モデル作成ユースケースのインターフェースクラス.
    整形データを生成する.
    """

    @abstractmethod
    def initialize(self) -> None:
        """ユースケースの実行による出力を初期化する"""
