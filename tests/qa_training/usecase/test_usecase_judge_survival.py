from typing import Tuple

import pandas as pd
from qa_training.utils.boundary.usecase.if_usecase_judge_survival import (
    IF_UsecaseJudgeSurvival,
)


def test_judge_survival(
    fixture_judge_survival: Tuple[IF_UsecaseJudgeSurvival, pd.DataFrame, list[bool]]
):
    (
        usecase_judge_survival,
        df_customer_info,
        list_survival_expected,
    ) = fixture_judge_survival

    list_survival = usecase_judge_survival.judge_survival(df_customer_info)
    assert list_survival == list_survival_expected
