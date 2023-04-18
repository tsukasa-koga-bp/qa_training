from abc import ABC, abstractmethod


class IF_UsecaseJudgeSurvival(ABC):
    """生存判定ユースケースのインターフェースクラス.
    整形データを生成する.
    """

    @abstractmethod
    def init_output(self) -> None:
        """ユースケースの実行による出力を初期化する"""
