from typing import Tuple

import pandas as pd
from qa_training.utils.boundary.usecase.if_usecase_judge_survival import (
    IF_UsecaseJudgeSurvival,
)
from qa_training.utils.my_assert_frame_equal import MyAssert


def test_judge_survival(
    fixture_judge_survival: Tuple[IF_UsecaseJudgeSurvival, pd.DataFrame, pd.DataFrame]
):
    (
        usecase_judge_survival,
        df_customer_info,
        df_results_expected,
    ) = fixture_judge_survival

    df_results = usecase_judge_survival.judge_survival(df_customer_info)
    
    MyAssert().assert_df(df_results, df_results_expected)
