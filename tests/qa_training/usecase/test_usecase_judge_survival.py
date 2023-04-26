import pandas as pd
from qa_training.utils.boundary.usecase.if_usecase_judge_survival import (
    IF_UsecaseJudgeSurvival,
)
from qa_training.utils.my_assert_frame_equal import MyAssert


def test_judge_survival(
    fixture_judge_survival: tuple[IF_UsecaseJudgeSurvival, pd.DataFrame]
):
    (
        usecase_judge_survival,
        df_results_expected,
    ) = fixture_judge_survival

    df_results = usecase_judge_survival.judge_survival()

    MyAssert().assert_df(df_results, df_results_expected)
