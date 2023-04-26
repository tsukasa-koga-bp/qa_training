from abc import ABC, abstractmethod

import pandas as pd


class IF_UsecaseJudgeSurvival(ABC):
    """生存判定ユースケースのインターフェースクラス.
    整形データを生成する.
    """

    @abstractmethod
    def judge_survival(self) -> pd.DataFrame:
        """生存を判定する."""

    @abstractmethod
    def initialize(self) -> None:
        """リポジトリを初期化する."""
